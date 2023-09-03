import discord
from discord.ext import commands
import random

TOKEN = 'MTExODA1MjI5NzM3Nzg1MzUyMA.GfoqyJ.k42M9Ghy_hoYEf-6gYo8_zE5IUCp6zQFron9Os'
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


class abot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=886887548381696040))
        self.synced = True
        print("BOT IS ONLINE")


bot = abot()
tree = commands.CommandTree(bot)


@tree.command(name="Ping", description='Pings the user', guild_ids=[886887548381696040])
async def ping_command(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong')


@tree.command(name="eightball", description='gives you an answer', guild_ids=[886887548381696040])
async def eightball_command(interaction: discord.Interaction, question: str):
    responses = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it',
                 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again',
                 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
                 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

    await interaction.response.send_message(f'**QUESTION: ** {question}\n **ANSWER:: **{random.choice(responses)}')


bot.run(TOKEN)
