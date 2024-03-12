from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import discord

load_dotenv()

def get_token():
    return os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot.activity = discord.Game("go fuck urself")

@bot.event
async def on_ready():
    print(f'You have logged in as {bot.user}')

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
        print("Worked")

@bot.event
async def on_message(message):
  message.reply("Go fuck yourself.")

@bot.event
async def startup():
    async with aiohttp.ClientSession() as session:
        bot.session = session

        await bot.start(get_token())

asyncio.run(startup())
