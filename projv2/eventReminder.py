import discord
import asyncio
import datetime
from discord.ext import commands

TOKEN = 'MTExODA1MjI5NzM3Nzg1MzUyMA.GfoqyJ.k42M9Ghy_hoYEf-6gYo8_zE5IUCp6zQFron9Os'
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Bot is ready!')


@bot.command()
async def setevent(ctx):
    try:
        # Prompt the user to enter the event time
        await ctx.send("Enter the event time (YYYY-MM-DD HH:MM): ")
        event_time_input = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30)

        # Convert the user input to a datetime object
        event_time = datetime.datetime.strptime(event_time_input.content, "%Y-%m-%d %H:%M")

        # Get the current time in Philippine Standard Time (UTC+8)
        current_time = datetime.datetime.utcnow() + datetime.timedelta(hours=8)

        # Calculate the delay until the event time
        time_until_event = (event_time - current_time).total_seconds()
        await ctx.send(f'Event set at {ctx}')

        if time_until_event > 0:
            # Wait until the event time
            await asyncio.sleep(time_until_event)

            # Find the desired server and channel
            server = bot.get_guild(886887548381696040)
            channel = discord.utils.get(server.channels, name='test')

            # Send the "@everyone" message
            await channel.send("@everyone ```EVENT NA``` ")
        else:
            await ctx.send("Event time has already passed.")
    except asyncio.TimeoutError:
        await ctx.send("Timeout: No response received.")
    except ValueError:
        await ctx.send("Invalid date/time format. Please try again.")


bot.run(TOKEN)
