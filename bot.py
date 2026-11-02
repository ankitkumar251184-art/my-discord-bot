import os
import discord
from discord.ext import commands

# Enable necessary intents
intents = discord.Intents.default()
intents.message_content = True  # Required so the bot can read message text

# Create bot instance with a command prefix "!"
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in successfully as {bot.user.name} (ID: {bot.user.id})!')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong! 🏓 Your bot is live and running on Kerit Cloud via Python.')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}! Hope you're having a great day.")

# Run the bot securely using the environment variable token
token = os.getenv('')
if token:
    bot.run(token)
else:
    print("Error: DISCORD_TOKEN environment variable is missing.")
