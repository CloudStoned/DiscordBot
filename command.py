import discord
from discord.ext import commands
import random

TOKEN = 'MTExODA1MjI5NzM3Nzg1MzUyMA.GfoqyJ.k42M9Ghy_hoYEf-6gYo8_zE5IUCp6zQFron9Os'
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
    

@bot.event
async def on_ready():
    print("Bot is online")


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong!{round(bot.latency * 1000)}ms")

@bot.command(aliases = ['8ball' ,'test'])
async def eightball(ctx,*,question):
    responses = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it',
               'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again',
               'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
               'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

    await ctx.send(f"**Question**: {question}\n **Answer**: {random.choice(responses)}")


bot.run(TOKEN)
