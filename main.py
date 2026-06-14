import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Bot online | Logged in as: {bot.user.name}")

@bot.command(name="say")
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)

@bot.command(name="about")
async def about(ctx):
    embed = discord.Embed(
        title="60 MIRAGE",
        description="Street raised, self-made. Seen it all, done it all.",
        color=discord.Color.dark_red()
    )
    embed.add_field(name="Code", value="Loyalty > everything\nNo cap, no fakes", inline=False)
    embed.add_field(name="Motto", value="Silent moves, loud results", inline=False)
    embed.set_footer(text="Trust few, fear none")
    await ctx.send(embed=embed)

@bot.command(name="code")
async def code(ctx):
    embed = discord.Embed(
        title="THE CODE",
        description="Live right or die wrong",
        color=discord.Color.black()
    )
    embed.add_field(name="•", value="Small circle, heavy trust", inline=False)
    embed.add_field(name="•", value="Speak less, let work show", inline=False)
    embed.add_field(name="•", value="Respect is earned, not given", inline=False)
    embed.set_footer(text="60 Mirage | Out of sight, never out of mind")
    await ctx.send(embed=embed)

@bot.command(name="embed")
async def custom_embed(ctx, title, *, content):
    embed = discord.Embed(
        title=title.upper(),
        description=content,
        color=discord.Color.dark_grey()
    )
    await ctx.send(embed=embed)

@bot.command(name="help")
async def help_cmd(ctx):
    embed = discord.Embed(
        title="📜 COMMAND LIST",
        color=discord.Color.blue()
    )
    embed.add_field(name="!say [text]", value="Bot repeats your message", inline=False)
    embed.add_field(name="!about", value="Info about 60 Mirage", inline=False)
    embed.add_field(name="!code", value="The street code", inline=False)
    embed.add_field(name="!embed [title] [message]", value="Make your own custom embed", inline=False)
    await ctx.send(embed=embed)

app = Flask('')
@app.route('/')
def home():
    return "Bot is running ✅"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    Thread(target=run).start()

keep_alive()

bot.run(os.getenv("MTUxNTc2MzMzNDkxMjQxMzg3Ng.G6yWWf.TwA5DdQIEoab5Ap5qhN02Phafb0T5XchDyrolY"))
