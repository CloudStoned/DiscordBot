import discord
import asyncio
import datetime
from discord.ext import commands

TOKEN = 'MTExODA1MjI5NzM3Nzg1MzUyMA.GfoqyJ.k42M9Ghy_hoYEf-6gYo8_zE5IUCp6zQFron9Os'
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Bot is ready!')

    # Set the time for the event in Philippine Standard Time (UTC+8)
    event_time = datetime.datetime(2023, 7, 13, 19, 1)

    # Get the current time in Philippine Standard Time (UTC+8)
    current_time = datetime.datetime.utcnow() + datetime.timedelta(hours=8)

    # Calculate the delay until the event time
    time_until_event = (event_time - current_time).total_seconds()

    # Wait until the event time
    await asyncio.sleep(time_until_event)

    # Find the desired server and channel
    server = bot.get_guild(886887548381696040)
    channel = discord.utils.get(server.channels, name='test')

    # Send the "@everyone" message
    await channel.send("@everyone ```PE NA``` \n https://meet.google.com/txj-uaer-cbw ")


bot.run(TOKEN)
