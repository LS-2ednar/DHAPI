import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
from utils.extract_DaggerHeart_Database_sheets import get_void_content, extract_domains, extract_abilities, extract_classes, extract_subclasses, extract_ancestries, extract_communities

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
    print(f"\n{bot.user.name} is ready\n")
    print(f"USE {bot.command_prefix}help FOR COMMAND OVERVIEW")
    print("\n--------------------")
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
    

@bot.event
async def on_member_join(member):
    await member.send(f"Hi, {member.name}!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "Zitronensorbet" in message.content:
        await message.delete()
        await message.channel.send(f"Psst... {message.author.mention} this opens the Door to Dumbledoors Office!") 

    await bot.process_commands(message)

"""
Commands
"""
@bot.command(help='Display official Playtest Material from the "Void".', description="Display additional Void Material via hyperlink.")
async def void(cxt):
    df = get_void_content()
    for _, row in df.iterrows():
        await cxt.send(f'{row["Content Type"]} Version:{row["Version"]} -> {row["URL"]}', delete_after=60)

@bot.command(help="Displays Domain infromation", description=f"Please try: {bot.command_prefix}domain class | {bot.command_prefix}domain DOMAINNAME | {bot.command_prefix}domain card CARDNAME")
async def domain(cxt, *args): 
    arguments = ' '.join(args).lower()
    if len(args) == 0:
        df = extract_domains()
        text = "\n".join(df["Domain"])
        await cxt.send(f'Available Domains are:\n{text}')

    if len(args) == 1:
        try:
            mask = df_domaincards["Domain"] == args[0].capitalize()
            df = df_domaincards.loc[mask]
            text = ""
            for _, row in df.iterrows():
                text += f'{row["Ability"]} - {row["Level"]}\n'
            await cxt.send(text)
        except:
            pass

    if "card" in args:
        card = arguments.replace("card","").strip().title()
        mask = df_domaincards["Ability"] == card
        df_card = df_domaincards.loc[mask]
        idx = df_card.index[0]
        await cxt.send(f'![{df_card["Ability"][idx]}]({df_card["URL"][idx]})',)
        text = f'**{df_card["Ability"][idx]}** - **{df_card["Domain"][idx]}** - **{df_card["Level"][idx]}**\n\n{df_card["Features"][idx]}'
        await cxt.send(text)

    if "class" in args:
        table = ""
        for _, row in df_classes.iterrows():
            Class, D1, D2 = row["Class"], row["Domain_1"], row["Domain_2"] 
            table+= f'**{Class}** \n- {D1} & {D2}\n'
        await cxt.send(table)

@bot.command(help="123", description="123")
async def card(cxt, *args):
    """
    1. TRY TO FIND THE MATCHING DATABASE OF THE CARDNAME PROVIDED
    2. CREATE A MESSAGE TO SEND THE MESSAGE TO THE SERVER
    3. PROVIDE IMAGE AND MESSAGE TO DISCORD
    """
    cardname = ' '.join(args).title()
    text  = ""
    if cardname in df_domaincards["Ability"].tolist():
        mask = df_domaincards["Ability"] == cardname
        df_card = df_domaincards.loc[mask]
        idx = df_card.index[0]
        img = f'[{df_card["Ability"][idx]}]({df_card["URL"][idx]})'
        text = f'**{df_card["Ability"][idx]}** - **{df_card["Domain"][idx]}** - **{df_card["Level"][idx]}**\n\n{df_card["Features"][idx]}'
        await cxt.send(img)
        await cxt.send(text)
        """
    elif cardname in df_classes["Class"].tolist():
        print(df_subclasses.keys())
        mask = df_classes["Class"] == cardname
        df_card = df_classes.loc[mask]
        idx = df_card.index[0]
        img = f'[{df_card["Class"][idx]}]({df_card["URL"][idx]})'
        text = f'**{df_card["Class"][idx]}** - **{df_card["Domain"][idx]}** - **{df_card["Level"][idx]}**\n\n{df_card["Features"][idx]}'
        await cxt.send(img)
        await cxt.send(text)
        """
    elif cardname in df_subclasses["Subclass"].tolist():
        print(df_subclasses.keys())
        mask = df_subclasses["Subclass"] == cardname
        df_card = df_subclasses.loc[mask]
        idx = df_card.index[0]
        img = f'[{df_card["Subclass"][idx]}]({df_card["URL"][idx]})'
        text = f'**{df_card["Subclass"][idx]}**\n**Foundation**\n{df_card["Foundation Features"][idx]} - **{df_card["Specialization Features"][idx]}**\n\n{df_card["Mastery Features"][idx]}'
        await cxt.send(img)
        await cxt.send(text)

    elif cardname in df_ancestries["Ancestry"].tolist():
        text = "Ancestry"
        await cxt.send(text)

    elif cardname in df_communities["Community"].tolist():
        text = "Community"
        await cxt.send(text)
        
    else:
        print("something went wrong")

    

"""
Cleaning the Chat
"""  
@bot.command()
async def clear_chat(cxt):
    try:
        await cxt.send("Okay.... Bye!", delete_after=10)
        await cxt.channel.purge(limit=None)
    except:
        pass

@bot.command()
async def cc(cxt):
    try:
        await cxt.send("Okay.... Bye!", delete_after=10)
        await cxt.channel.purge(limit=None)
    except:
        pass

"""
Rune the Bot
"""
bot.run(token, log_handler=handler, log_level=logging.DEBUG)