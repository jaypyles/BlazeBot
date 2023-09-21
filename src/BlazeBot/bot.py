# STL
import os
import logging

# PDM
import discord
from dotenv import load_dotenv
from discord.ext import commands

# LOAD ENV
load_dotenv()
token = os.getenv("DEV_TOKEN")
LOG = logging.getLogger(__name__)


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.typing = True
intents.members = True
bot = commands.Bot(command_prefix="**", intents=intents)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("doom scrolling"))
    print(f"Logged in as {bot.user}")


if token:
    bot.run(token)
