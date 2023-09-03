import discord
from discord.ext import commands
import random

TOKEN = 'MTExODA1MjI5NzM3Nzg1MzUyMA.GfoqyJ.k42M9Ghy_hoYEf-6gYo8_zE5IUCp6zQFron9Os'
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print('Bot is Online')


@bot.command()
async def embed(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author

    name = member.display_name
    profile_pic = member.default_avatar

    embed = discord.Embed(title = 'This is my embed', description= 'COOL EMBED',colour=discord.Colour.random())
    embed.set_thumbnail(url=profile_pic)
    embed.set_footer(text=name)
    await ctx.send(embed=embed)

bot.run(TOKEN)
