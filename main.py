import discord
from discord import app_commands
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="", intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    await tree.sync()
    print(f"✅ Bot online: {bot.user.name}")
    print("✅ Slash commands synced")

# --------------------------
# SLASH COMMANDS ONLY
# --------------------------

@tree.command(name="say", description="Bot sends your message")
@app_commands.describe(message="What you want the bot to say")
async def say(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(message)

@tree.command(name="about", description="Info about 60 Mirage")
async def about(interaction: discord.Interaction):
    e = discord.Embed(
        title="60 MIRAGE",
        description="Street raised, self-made. Seen it all, done it all.",
        color=discord.Color.dark_red()
    )
    e.add_field(name="Code", value="Loyalty > everything\nNo cap, no fakes", inline=False)
    e.add_field(name="Motto", value="Silent moves, loud results", inline=False)
    e.set_footer(text="Trust few, fear none")
    await interaction.response.send_message(embed=e)

@tree.command(name="code", description="The street code")
async def code(interaction: discord.Interaction):
    e = discord.Embed(
        title="THE CODE",
        description="Live right or die wrong",
        color=discord.Color.black()
    )
    e.add_field(name="•", value="Small circle, heavy trust", inline=False)
    e.add_field(name="•", value="Speak less, let work show", inline=False)
    e.add_field(name="•", value="Respect is earned, not given", inline=False)
    e.set_footer(text="60 Mirage | Out of sight, never out of mind")
    await interaction.response.send_message(embed=e)

@tree.command(name="embed", description="Send a custom embed")
@app_commands.describe(title="Title of the box", text="Message inside")
async def embed(interaction: discord.Interaction, title: str, text: str):
    e = discord.Embed(
        title=title.upper(),
        description=text,
        color=discord.Color.dark_grey()
    )
    await interaction.response.send_message(embed=e)

@tree.command(name="commands", description="List all available commands")
async def commands(interaction: discord.Interaction):
    e = discord.Embed(title="COMMANDS LIST", color=discord.Color.blue())
    e.add_field(name="/say", value="Bot repeats your text", inline=False)
    e.add_field(name="/about", value="Bot info", inline=False)
    e.add_field(name="/code", value="Street rules", inline=False)
    e.add_field(name="/embed", value="Make your own message box", inline=False)
    await interaction.response.send_message(embed=e)

# --------------------------
# Keep Render alive
# --------------------------
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot running ✅"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    Thread(target=run, daemon=True).start()

keep_alive()

bot.run(os.getenv("MTUxNTc2MzMzNDkxMjQxMzg3Ng.G6yWWf.TwA5DdQIEoab5Ap5qhN02Phafb0T5XchDyrolY"), reconnect=True)
