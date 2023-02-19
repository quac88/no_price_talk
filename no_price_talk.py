import discord
from discord.ext import commands

TOKEN = "<>"

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

welcome_message = "Welcome to the server! Please read the rules and confirm that you have read them by clicking the :thumbsup: reaction below."

@bot.event
async def on_member_join(member):
    message = await member.send("Welcome to the official Bittensor Discord! Please read and agree to the rules by clicking the :thumbsup: reaction below.")
    await message.add_reaction("👍")

@bot.event
async def on_reaction_add(reaction, user):
    if str(reaction.emoji) == "👍" and reaction.message.author == bot.user and isinstance(reaction.message.channel, discord.DMChannel):
        guild = bot.guilds[0]  # assume the bot is only in one guild
        member = guild.get_member(user.id)
        if member is not None:
            pleb_role = discord.utils.get(guild.roles, name="Pleb")
            if pleb_role is not None:
                await member.add_roles(pleb_role)
                await member.send("Welcome Pleb! You may now join the official discord.")

bot.run(TOKEN)
