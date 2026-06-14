import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Bot online: {bot.user.name}")

# Your commands
@bot.command()
async def about(ctx):
    await ctx.send("60 Mirage • Street raised, self made. Trust few, fear none.")

@bot.command()
async def code(ctx):
    await ctx.send("Live right or die wrong. Loyalty > everything. No cap, no fakes.")

@bot.command()
async def status(ctx):
    await ctx.send("Silent moves, loud results. Out of sight, never out of mind.")

@bot.command()
async def help(ctx):
    await ctx.send("Commands: !about | !code | !status")

# Keep Render alive
app = Flask('')
@app.route('/')
def home(): return "Bot running"
def run(): app.run(host="0.0.0.0", port=8080)
def keep_alive(): Thread(target=run).start()
keep_alive()

bot.run(os.getenv("MTUxNTc2MzMzNDkxMjQxMzg3Ng.G6yWWf.TwA5DdQIEoab5Ap5qhN02Phafb0T5XchDyrolY"))
