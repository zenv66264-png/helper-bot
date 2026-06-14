import discord
from discord import app_commands
import os

TOKEN = os.getenv("MTUxNTc2MzMzNDkxMjQxMzg3Ng.G6yWWf.TwA5DdQIEoab5Ap5qhN02Phafb0T5XchDyrolY")  # Put your bot token in Render Environment Variables

class MyBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print("Slash commands synced!")

bot = MyBot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="ping", description="Check bot latency")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"🏓 Pong! {round(bot.latency * 1000)}ms"
    )

@bot.tree.command(name="hello", description="Say hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Hello {interaction.user.mention}! 👋"
    )

@bot.tree.command(name="say", description="Make the bot say something")
@app_commands.describe(message="Message to send")
async def say(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(message)

bot.run(TOKEN)
