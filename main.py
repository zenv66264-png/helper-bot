import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connected as: {bot.user.name}")

@bot.command()
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)

@bot.command()
async def about(ctx):
    e = discord.Embed(title="60 MIRAGE", description="Street raised, self-made. Seen it all, done it all.", color=discord.Color.dark_red())
    e.add_field(name="Code", value="Loyalty > everything\nNo cap, no fakes", inline=False)
    e.add_field(name="Motto", value="Silent moves, loud results", inline=False)
    e.set_footer(text="Trust few, fear none")
    await ctx.send(embed=e)

@bot.command()
async def code(ctx):
    e = discord.Embed(title="THE CODE", description="Live right or die wrong", color=discord.Color.black())
    e.add_field(name="•", value="Small circle, heavy trust", inline=False)
    e.add_field(name="•", value="Speak less, let work show", inline=False)
    e.add_field(name="•", value="Respect is earned, not given", inline=False)
    e.set_footer(text="60 Mirage | Out of sight, never out of mind")
    await ctx.send(embed=e)

@bot.command()
async def embed(ctx, title, *, content):
    e = discord.Embed(title=title.upper(), description=content, color=discord.Color.dark_grey())
    await ctx.send(embed=e)

@bot.command()
async def help(ctx):
    e = discord.Embed(title="COMMANDS", color=discord.Color.blue())
    e.add_field(name="!say [text]", value="Repeat your message", inline=False)
    e.add_field(name="!about", value="Bot info", inline=False)
    e.add_field(name="!code", value="Street rules", inline=False)
    e.add_field(name="!embed [title] [text]", value="Custom box", inline=False)
    await ctx.send(embed=e)

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot running ✅"

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    Thread(target=run, daemon=True).start()

keep_alive()

bot.run(os.getenv("MTUxNTc2MzMzNDkxMjQxMzg3Ng.G6yWWf.TwA5DdQIEoab5Ap5qhN02Phafb0T5XchDyrolY"), reconnect=True)
