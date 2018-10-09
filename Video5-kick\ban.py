import discord
import asyncio
from discord.ext import commands


bot=commands.Bot(command_prefix='y.)






@bot.event
async def on_ready():
    print(bot.user.name)



@bot.command(pass_context=True)
async def kick(con,user:discord.Member):
    pass







bot.run('BOT TOKEN HERE')
