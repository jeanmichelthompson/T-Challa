import discord
from discord.ext import commands
from commands import handle_message
import config

# Initialize the bot with necessary intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=config.COMMAND_PREFIX, intents=intents)

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Event handler for when a message is received
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await handle_message(bot, message)

# Run the bot with the token from environment variables
bot.run(str(config.DISCORD_TOKEN))
