import discord
import asyncio
import datetime
from discord.ext import commands

TOKEN = 'MTExODA1MjI5NzM3Nzg1MzUyMA.GfoqyJ.k42M9Ghy_hoYEf-6gYo8_zE5IUCp6zQFron9Os'
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Define your keyword and response mappings
    keyword_responses = {
        'hello': 'Hi there!',
        'python': 'Python is awesome!',
        'discord': 'Discord is a great platform!',
    }

    for keyword, response in keyword_responses.items():
        if keyword in message.content.lower():
            await message.channel.send(response)

    await bot.process_commands(message)

bot.run(TOKEN)
