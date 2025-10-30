import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
from utils.extract_DaggerHeart_Database_sheets import get_void_content

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename="ribba.log",encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")
    print(f"{bot.command_prefix}")

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

@bot.command()
async def void(context):
    df = get_void_content()
    for _, row in df.iterrows():
        await context.send(f'{row["Content Type"]} Version:{row["Version"]} -> {row["URL"]}', delete_after=30)

@bot.command()
async def clear_chat(context):
    try:
        await context.send("Okay.... Bye!", delete_after=10)
        await context.channel.purge(limit=None)
    except:
        pass

bot.run(token, log_handler=handler, log_level=logging.DEBUG)