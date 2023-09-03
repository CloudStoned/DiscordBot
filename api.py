import discord
import requests
from discord.ext import commands
import random

TOKEN = 'MTExODA1MjI5NzM3Nzg1MzUyMA.GfoqyJ.k42M9Ghy_hoYEf-6gYo8_zE5IUCp6zQFron9Os'
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Bot is online")


@bot.command()
async def dog(ctx):
    req = requests.get("https://dog.ceo/api/breeds/image/random")
    res = req.json()
    embed = discord.Embed()
    embed.set_image(url=res['message'])
    await ctx.send(embed=embed)


@bot.command()
async def truth(ctx):
    r = requests.get('https://api.truthordarebot.xyz/v1/wyr')
    res = r.json()
    await ctx.send(res['question'])


bot.run(TOKEN)
