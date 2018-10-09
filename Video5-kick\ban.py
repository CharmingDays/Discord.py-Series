import discord
import asyncio
from discord.ext import commands
from discord.utils import *

bot=commands.Bot(command_prefix='y.)






@bot.event
async def on_ready():
    print(bot.user.name)



@bot.command(pass_context=True)
async def kick(con,user:discord.Member):
    name=user.name
    await bot.kick(user)
    await bot.say("User {} has been kicked by {}".format(name,con.message.author.name))

@bot.command(pass_context=True)
async def ban(con,user:discord.Member):
    name=user.name
    await bot.ban(user)
    await bot.say("{} has been banned by {} from {}".format(name,con.message.author.name,con.message.server.name))



bot.run('BOT TOKEN HERE')
