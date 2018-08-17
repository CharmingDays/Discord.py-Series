import discord
from discord.ext import commands
import asyncio
import random
from discord.utils import *

yakumo = commands.Bot(command_prefix='y.')

# PRINT READY WHEN BOT IS READY
@yakumo.event
async def on_ready():
    print(yakumo.user.name)

#THE MIN1 AND MAX1 MUST HAVE A DEFAULT INT VALUE OR IT WILL CAUSE AN ERROR
@yakumo.command(pass_context=True)
async def dice(con,min1=1,max1=6):
    await yakumo.say("**{}**".format(random.randint(min1,max1))) #I PUT IT THIS WAY TO MAKE IT BOLD IN DISCORD


#PINS THE MESSAGE YOU WRITE    
@yakumo.command(pass_context=True) #THE FIRST PARAMETER IS THE CONTEXT, YOU CAN CHOOSE OTHER NAMES INSTEAD OF "con"
async def pin(con,*,msg):
    await yakumo.pin_message(con.message)
@yakumo.command(pass_context=True)
async def kick(con,user:discord.Member):
    await yakumo.kick(user)
    await yakumo.say("{} has been kicked from {}".format(user.name,con.message.server.name))


@yakumo.command(pass_context=True)
async def react(con,msg_id,emoji):
    try:
        emote= get(yakumo.get_all_emojis(),name=emoji) #FIND THE EMOJI THAT IS GIVEN BY NAME
        msg= await yakumo.get_message(con.message.channel,msg_id) #FIND THE MESSSAGE TO REACT 
        await yakumo.add_reaction(msg,emoji=emote)
    except:
        await yakumo.say("Reaction not found") # ERROR MESSAGE FOR WHEN SOMETHING GOES WRONG

yakumo.run('YOUR BOT TOKEN HERE')
