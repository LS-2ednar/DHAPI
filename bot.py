import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import requests
import tempfile
from utils.extract_DaggerHeart_Database_sheets import get_void_content, extract_domains, extract_abilities, extract_classes, extract_subclasses, extract_ancestries, extract_communities
from utils.character_creator import new_char

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
handler = logging.FileHandler(filename="ribba.log",encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!",intents=intents)

"""
Events
"""
@bot.event
async def on_ready():
    print("\n-----------------------------")
    print(f"STARTING DISCORD BOT: {bot.user.name}")
    print("-----------------------------\n")


    print("--------------------")
    print("Loading Datasources:")
    print("--------------------\n")
    
    try:
        global df_domaincards 
        df_domaincards = extract_abilities()
        print("loaded: Domaincards")
    except:
        print("Could not load Domaincards")
        pass

    try:
        global df_classes
        df_classes = extract_classes()
        print("loaded: Classes")
    except:
        print("Could not load Classcards")
        pass

    try:
        global df_subclasses
        df_subclasses = extract_subclasses()
        print("loaded: Subclasses")
    except:
        print("Could not load Subclassescards")
        pass

    try:
        global df_ancestries
        df_ancestries = extract_ancestries()
        print("loaded: Ancestries")
    except:
        print("Could not load Ancestriescards")
        pass

    try:
        global df_communities
        df_communities = extract_communities()
        print("loaded: Communities")
    except:
        print("Could not load Communitycards")

    print(f"\n{bot.user.name} is ready\n")
    print(f"USE {bot.command_prefix}help FOR COMMAND OVERVIEW")

@bot.event
async def on_member_join(member):
    await member.send(f"Hi, {member.name}!")

@bot.event
async def on_message(message: discord.Message):
    TRIGGERS = {"cc", "cls", "clear chat", "clear_chat"}
    if message.author == bot.user:
        return

    content = message.content.lower().strip()

    if isinstance(message.channel, (discord.TextChannel, discord.Thread)) and content in TRIGGERS:
        try:
            msg = await message.channel.send("Okay… Bye! This will be wiped in a moment.", delete_after=3)
            # Requires Manage Messages permission. Purge removes all users' messages; consider a smaller limit.
            await message.channel.purge(limit=None)
        except discord.Forbidden:
            await message.channel.send("⚠️ I need Manage Messages permission to purge here.", delete_after=5)
        except Exception:
            pass
        return

    await bot.process_commands(message)

"""
Commands
"""
@bot.command(help='Display official Playtest Material from the "Void" in the chat.',
             description="Display additional Void Material via downloadable PDF.")
async def void(ctx):
    df = get_void_content()

    for _, row in df.iterrows():
        url = row["URL"]
        filename = url.split("/")[-1]

        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()

            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(response.content)
                tmp_file_path = tmp_file.name

            file = discord.File(tmp_file_path, filename=filename)
            await ctx.send(
                content=f'{row["Content Type"]} Version:{row["Version"]}',
                file=file
            )

        except Exception as e:
            await ctx.send(f"❌ Error downloading {url}: {e}", delete_after=30)

@bot.command(help="Displays Domain infromation", description=f"Please try: {bot.command_prefix}domain class | {bot.command_prefix}domain DOMAINNAME | {bot.command_prefix}domain card CARDNAME")
async def domain(ctx, *args): 
    arguments = ' '.join(args).lower()
    if len(args) == 0:
        df = extract_domains()
        text = "\n".join(df["Domain"])
        await ctx.send(f'Available Domains are:\n{text}')

    if len(args) == 1:
        try:
            mask = df_domaincards["Domain"] == args[0].capitalize()
            df = df_domaincards.loc[mask]
            text = ""
            for _, row in df.iterrows():
                text += f'{row["Ability"]} - {row["Level"]}\n'
            await ctx.send(text)
        except:
            pass

    if "card" in args:
        card = arguments.replace("card","").strip().title()
        mask = df_domaincards["Ability"] == card
        df_card = df_domaincards.loc[mask]
        idx = df_card.index[0]
        await ctx.send(f'![{df_card["Ability"][idx]}]({df_card["URL"][idx]})',)
        text = f'**{df_card["Ability"][idx]}** - **{df_card["Domain"][idx]}** - **{df_card["Level"][idx]}**\n\n{df_card["Features"][idx]}'
        await ctx.send(text)

    if "class" in args:
        table = ""
        for _, row in df_classes.iterrows():
            Class, D1, D2 = row["Class"], row["Domain_1"], row["Domain_2"] 
            table+= f'**{Class}** \n- {D1} & {D2}\n'
        await ctx.send(table)

@bot.command(help="Displays a specific card in the chat", description="Given a proper <CARDNAME> the card details get displayed in the chat")
async def card(ctx, *args):

    cardname = ' '.join(args).title()

    if len(cardname) == 0:
        await ctx.send(f"Use one of the following keywords to learn about available cards per cardtype:\n\n{bot.command_prefix}card domain or {bot.command_prefix}card domains\n{bot.command_prefix}card subclass or {bot.command_prefix}card subclasses\n{bot.command_prefix}card ancestry or {bot.command_prefix}card ancestries\n{bot.command_prefix}card community or {bot.command_prefix}card communities")

    if cardname == "Domain" or cardname == "Domains":
        text = f"There are way to many domaincards!!\n\nuse **{bot.command_prefix}domain**\n\nand learn about the different domains and there cards. Here are some domaincard examples:\n" 
        text += "\n- ".join(df_domaincards["Ability"].tolist())
        await ctx.send(text[0:499]+"\n... and more")
        
    if cardname == "Subclass" or cardname == "Subclasses":
        text = "Here are all Subclasscards:\n"
        text += "\n- ".join(df_subclasses["Subclass"].tolist())
        await ctx.send(text)

    if cardname == "Ancestry" or cardname == "Ancestries":
        text = "Here are all Ancestycards:\n"
        text += "\n- ".join(df_ancestries["Ancestry"].tolist())
        await ctx.send(text)

    if cardname == "Community" or cardname == "Communities":
        text = "Here are all Communiycards:\n"
        text += "\n- ".join(df_communities["Community"].tolist())
        await ctx.send(text)

    if cardname in df_domaincards["Ability"].tolist():
        mask = df_domaincards["Ability"] == cardname
        df_card = df_domaincards.loc[mask]
        idx = df_card.index[0]
        img = f'[{df_card["Ability"][idx]}]({df_card["URL"][idx]})'
        text = f'**{df_card["Ability"][idx]}** - **{df_card["Domain"][idx]}** - **{df_card["Level"][idx]}**\n\n{df_card["Features"][idx]}'
        await ctx.send(img)
        await ctx.send(text)

    elif cardname in df_subclasses["Subclass"].tolist():
        mask = df_subclasses["Subclass"] == cardname
        df_card = df_subclasses.loc[mask]
        idx = df_card.index[0]
        img = f'[{df_card["Subclass"][idx]}]({df_card["URL"][idx]})'
        text = f'**{df_card["Class"][idx]} - Subclass: {df_card["Subclass"][idx]}**\n\n**Foundation:**\n{df_card["Foundation Features"][idx]}\n\n**Specialization:**\n{df_card["Specialization Features"][idx]}\n\n**Mastery:**\n{df_card["Mastery Features"][idx]}'
        await ctx.send(img)
        await ctx.send(text)

    elif cardname in df_ancestries["Ancestry"].tolist():
        mask = df_ancestries["Ancestry"] == cardname
        df_card = df_ancestries.loc[mask]
        idx = df_card.index[0]
        img = f'[{df_card["Ancestry"][idx]}]({df_card["URL"][idx]})'
        text = f'**Ancestry: {df_card["Ancestry"][idx]}**\n\n**Features:**\n{df_card["Features"][idx]}\n\n**Description:**\n{df_card["Description"][idx]}'
        await ctx.send(img)
        await ctx.send(text)

    elif cardname in df_communities["Community"].tolist():
        mask = df_communities["Community"] == cardname
        df_card = df_communities.loc[mask]
        idx = df_card.index[0]
        img = f'[{df_card["Community"][idx]}]({df_card["URL"][idx]})'
        text = f'**Community: {df_card["Community"][idx]}**\n\n**Features:**\n{df_card["Features"][idx]}\n\n**Description:**\n{df_card["Description"][idx]}'
        await ctx.send(img)
        await ctx.send(text)

@bot.command(help="Creates a new character pdf file", description="available parameters are: <NAME>, <LEVEL>, <CLASS>, <COMMUNITY>, <ANCESTRY>, <CLASS>, <SUBCLASS> seperate the parameters by comma. Example: !newchar Name=Ribba, Class=Wizard, Level=3, SUBCLASS=School of War")
async def newchar(ctx, *args):

    data = {
        'charname':'',
        'heritage':'',
        'class':'',
        'subclass':'',
        'agility':'', 
        'strength':'',  
        'finesse':'', 
        'instinct':'', 
        'presence':'', 
        'knowledge':'', 
        'evasion':'',
        'maxHP':'',
        'maxStress':'6',
        'hopefeature':'',
        'classfeatures':'',
        'questions':'',
        'connections':'',
        'domain1':'',
        'domain2':'',
        'level':'1'
    }

    arguments_raw = " ".join(args)
    argument_pairs = arguments_raw.lower().split(",")
    heritage_l = ['','']
    features = ['','','','']
    """
    Sorting arguments to avoid wrong number of features added -> ensure level is checked first!!!
    """
    sorting_element = "level"
    for i, s in enumerate(argument_pairs):
        if sorting_element in s:
            argument_pairs.insert(0,argument_pairs.pop(i))


    for argument in argument_pairs:

        if "name" in argument:
            data["charname"] = argument.split("=")[1].strip().title()

        if "ancestry" in argument:
            heritage_l[0] = argument.split("=")[1].strip().title()

        if "community" in argument:
            heritage_l[1] = argument.split("=")[1].strip().title()

        if "class" in argument and "subclass" not in argument:
            mask = df_classes["Class"] == argument.split("=")[1].strip().title()
            df_card = df_classes.loc[mask]
            idx = df_card.index[0]

            data["class"] = argument.split("=")[1].strip().title()
            data["evasion"] = str(df_card["Starting Evasion"][idx])
            data["maxHP"] = str(df_card["Starting HP"][idx])
            data["hopefeature"] = df_card["Hope Feature"][idx] 
            features[0] = df_card["Class Features"][idx]
            data["questions"] = df_card["Questions"][idx]
            data["connections"] = df_card["Connections"][idx]
            data["domain1"] = df_card["Domain_1"][idx]
            data["domain2"] = df_card["Domain_2"][idx]

            """
            Check the recommended values for agility, strength, finesse, instinct, presence, knowledge 
            This section might be updated in the future to ensure it works more efficient.
            """
            if argument.split("=")[1].strip().title() == "Bard":
                data["agility"] = "0"
                data["strength"] = "-1"
                data["finesse"] = "+1"
                data["instinct"] = "0"
                data["presence"] = "+2"
                data["knowledge"] = "+1"

            if argument.split("=")[1].strip().title() == "Druid":
                data["agility"] = "+1"
                data["strength"] = "0"
                data["finesse"] = "+1"
                data["instinct"] = "+2"
                data["presence"] = "-1"
                data["knowledge"] = "0"

            if argument.split("=")[1].strip().title() == "Guardian":
                data["agility"] = "+1"
                data["strength"] = "+2"
                data["finesse"] = "-1"
                data["instinct"] = "0"
                data["presence"] = "+1"
                data["knowledge"] = "0"

            if argument.split("=")[1].strip().title() == "Ranger":
                data["agility"] = "+2"
                data["strength"] = "0"
                data["finesse"] = "+1"
                data["instinct"] = "+1"
                data["presence"] = "-1"
                data["knowledge"] = "0"

            if argument.split("=")[1].strip().title() == "Rogue":
                data["agility"] = "+1"
                data["strength"] = "-1"
                data["finesse"] = "+2"
                data["instinct"] = "0"
                data["presence"] = "+1"
                data["knowledge"] = "0"

            if argument.split("=")[1].strip().title() == "Seraph":
                data["agility"] = "0"
                data["strength"] = "+2"
                data["finesse"] = "0"
                data["instinct"] = "+1"
                data["presence"] = "+1"
                data["knowledge"] = "-1"

            if argument.split("=")[1].strip().title() == "Sorcerer":
                data["agility"] = "0"
                data["strength"] = "-1"
                data["finesse"] = "+1"
                data["instinct"] = "+2"
                data["presence"] = "+1"
                data["knowledge"] = "0"

            if argument.split("=")[1].strip().title() == "Warrior":
                data["agility"] = "+2"
                data["strength"] = "+1"
                data["finesse"] = "0"
                data["instinct"] = "+1"
                data["presence"] = "-1"
                data["knowledge"] = "0"

            if argument.split("=")[1].strip().title() == "Wizard":
                data["agility"] = "-1"
                data["strength"] = "0"
                data["finesse"] = "0"
                data["instinct"] = "+1"
                data["presence"] = "+1"
                data["knowledge"] = "+2"
            
        if "subclass" in argument:
            mask = df_subclasses["Subclass"] == argument.split("=")[1].strip().title()
            df_card = df_subclasses.loc[mask]
            idx = df_card.index[0]

            data["subclass"] = argument.split("=")[1].strip().title()
            features[1] = f'{df_card["Foundation Features"][idx]}'
            if int(data["level"]) >= 5:
                features[2] = f'{df_card["Specialization Features"][idx]}'
            if int(data["level"]) >= 8:
                features[2] = f'{df_card["Mastery Features"][idx]}'

        if "level" in argument:
            data["level"] = argument.split("=")[1].strip().title()

    data["classfeatures"] = "\n".join(features)
    data["heritage"] = f'{heritage_l[0]} | {heritage_l[1]}'
    char_file = new_char(data)
    user = ctx.author 
    try:
        await ctx.send(
            content=f"Hey {user.name} here is your new charactersheet.\n\nNOTE\n\nThis is still a work in progress. Check your Evasion and stress values",
            file=discord.File(char_file))
    except:
        pass
    
"""
Run the Bot
"""
bot.run(token, log_handler=handler, log_level=logging.DEBUG)