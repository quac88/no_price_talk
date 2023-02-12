import discord
from discord.ext import commands

TOKEN = "MTA2ODYxNTMwMzI2MjYzNDA5NQ.GQKExA.c9FV3RjqpHqE3PMClwn3s_eLUDGtgLFidQgBCA"

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
@bot.command(name='test')
async def chat(ctx ):
    await ctx.send( "hello world" )

bot.run(TOKEN)


# https://discord.com/developers/applications