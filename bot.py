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
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content == "cc" or message.content == "cls" or message.content == "clear chat" or message.content == "clear_chat":
        try:
            await message.channel.send("Okay.... Bye!", delete_after=10)
            await message.channel.purge(limit=None)
        except:
            pass

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

    cardname = ' '.join(args).title()

    if len(cardname) == 0:
        await cxt.send(f"Use one of the following keywords to learn about available cards per cardtype:\n\n{bot.command_prefix}card domain or {bot.command_prefix}card domains\n{bot.command_prefix}card subclass or {bot.command_prefix}card subclasses\n{bot.command_prefix}card ancestry or {bot.command_prefix}card ancestries\n{bot.command_prefix}card community or {bot.command_prefix}card communities")

    if cardname == "Domain" or cardname == "Domains":
        text = f"There are way to many domaincards!!\n\nuse **{bot.command_prefix}domain**\n\nand learn about the different domains and there cards. Here are some domaincard examples:\n" 
        text += "\n- ".join(df_domaincards["Ability"].tolist())
        await cxt.send(text[0:499]+"\n... and more")
        
    if cardname == "Subclass" or cardname == "Subclasses":
        text = "Here are all Subclasscards:\n"
        text += "\n- ".join(df_subclasses["Subclass"].tolist())
        await cxt.send(text)

    if cardname == "Ancestry" or cardname == "Ancestries":
        text = "Here are all Ancestycards:\n"
        text += "\n- ".join(df_ancestries["Ancestry"].tolist())
        await cxt.send(text)

    if cardname == "Community" or cardname == "Communities":
        text = "Here are all Communiycards:\n"
        text += "\n- ".join(df_communities["Community"].tolist())
        await cxt.send(text)

    if cardname in df_domaincards["Ability"].tolist():
        mask = df_domaincards["Ability"] == cardname
        df_card = df_domaincards.loc[mask]
        idx = df_card.index[0]
        img = f'[{df_card["Ability"][idx]}]({df_card["URL"][idx]})'
        text = f'**{df_card["Ability"][idx]}** - **{df_card["Domain"][idx]}** - **{df_card["Level"][idx]}**\n\n{df_card["Features"][idx]}'
        await cxt.send(img)
        await cxt.send(text)

    elif cardname in df_subclasses["Subclass"].tolist():
        mask = df_subclasses["Subclass"] == cardname
        df_card = df_subclasses.loc[mask]
        idx = df_card.index[0]
        img = f'[{df_card["Subclass"][idx]}]({df_card["URL"][idx]})'
        text = f'**{df_card["Class"][idx]} - Subclass: {df_card["Subclass"][idx]}**\n\n**Foundation:**\n{df_card["Foundation Features"][idx]}\n\n**Specialization:**\n{df_card["Specialization Features"][idx]}\n\n**Mastery:**\n{df_card["Mastery Features"][idx]}'
        await cxt.send(img)
        await cxt.send(text)

    elif cardname in df_ancestries["Ancestry"].tolist():
        mask = df_ancestries["Ancestry"] == cardname
        df_card = df_ancestries.loc[mask]
        idx = df_card.index[0]
        img = f'[{df_card["Ancestry"][idx]}]({df_card["URL"][idx]})'
        text = f'**Ancestry: {df_card["Ancestry"][idx]}**\n\n**Features:**\n{df_card["Features"][idx]}\n\n**Description:**\n{df_card["Description"][idx]}'
        await cxt.send(img)
        await cxt.send(text)

    elif cardname in df_communities["Community"].tolist():
        mask = df_communities["Community"] == cardname
        df_card = df_communities.loc[mask]
        idx = df_card.index[0]
        img = f'[{df_card["Community"][idx]}]({df_card["URL"][idx]})'
        text = f'**Community: {df_card["Community"][idx]}**\n\n**Features:**\n{df_card["Features"][idx]}\n\n**Description:**\n{df_card["Description"][idx]}'
        await cxt.send(img)
        await cxt.send(text)

"""
Rune the Bot
"""
bot.run(token, log_handler=handler, log_level=logging.DEBUG)