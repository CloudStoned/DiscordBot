import discord
from discord.ext import commands
import random

TOKEN = 'MTExODA1MjI5NzM3Nzg1MzUyMA.GfoqyJ.k42M9Ghy_hoYEf-6gYo8_zE5IUCp6zQFron9Os'
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@client.command()
async def syntax(ctx, *, syntax_type):
    if syntax_type in ["for loop", "if statement", "while loop", "for loop ex"]:
        await ctx.send(f"``` {syntax_type}: \n {random.choice(syntax_type_code[syntax_type])}```")
    else:
        await ctx.send("Invalid syntax type.")


@client.command()
async def syntax_ex(ctx, *, syn_ex):
    if syn_ex in ["for loop ex"]:
        await ctx.send(f"```{syn_ex}: \n {random.choice(syntax_ex_code[syn_ex])}```")
    else:
        await ctx.send("Invalid syntax type")


syntax_type_code = {
    "for loop": [
        "for i in range(10): \n print(i)",
        "for i in range(10): \n do something"
    ],
    "if statement": [
        "if condition: \n do something",
        "if condition: \n else: \n do something else"
    ],
    "while loop": [
        "while condition: \n do something",
        "while condition: \n else: \n do something else"
    ]
}

syntax_ex_code = {
    # EXAMPLES
    "for loop ex": [
        "for i in range(10): \n print(i) \n output: 1,2,3,4,5,6,7,8,9,10"

    ]
}

client.run(TOKEN)
