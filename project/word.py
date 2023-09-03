import discord
from discord.ext import commands
from docx import Document

TOKEN = 'MTExODA1MjI5NzM3Nzg1MzUyMA.GfoqyJ.k42M9Ghy_hoYEf-6gYo8_zE5IUCp6zQFron9Os'
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Bot is ready: {bot.user.name}')


@bot.command()
async def generate_word(ctx, text: str):
    # Create a new Word document
    document = Document()
    document.add_paragraph(text)

    # Save the Word document on the bot's server
    file_name = 'generated_file.docx'
    document.save(file_name)

    # Open the Word file and send it as an attachment to the user
    with open(file_name, 'rb') as file:
        await ctx.send(file=discord.File(file))

bot.run(TOKEN)
