import discord
from discord.ext import commands
import asyncio
import random





yakumo=commands.Bot(command_prefix='y.')



#BT DEFAULT WIHTOUT A TYPE IT WILL EQUAL TO PLAYING
#TYPE 3 = WATCHING
async def watch():
    #YOU CAN MAKE YOUR OWN LIST, BUT FEEL FREE TO USE MINE
    watch_list = ['Man vs Wild', 'Supernatural', 'Trick2g', 'RIOT GAMES', 'You', '@everyone', 'Silent Hill', 'The Grudge', 'Mouse Trap Mondays:Shawn Woods']
    while True:
        await asyncio.sleep(8)
        await yakumo.change_presence(game=discord.Game(name=random.choice(watch_list),type=3))

#TYPE 2 = LISTENING
async def listen():
    #YOU CAN MAKE YOUR OWN LIST, BUT FEEL FREE TO USE MINE
    listen_list = ['Alan Walker Faded', 'Trick2g\'s Scream', 'Apink','Twice:Knock Knock', 'Let it go:Meiko', 'I Dreamed a Dream, Susan Boyle']
    while True:
        await yakumo.change_presence(game=discord.Game(name=random.choice(listen_list), type=2))
        await asyncio.sleep(15)





#COLLECTS THE TWO FUNCTIONS INTO ONE
async def change_status():
    bot.loop.create_task(watch())
    bot.loop.create_task(listen())


@yakumo.event
async def on_ready():
    print(yakumo.user.name)
    #RUN YOUR BACKGROUND TASK HERE
    bot.loop.create_task(change_status())



#REPLACE BOT_TOKEN WITH YOUR ACTUAL BOT TOKEN
yakumo.run('BOT_TOKEN')
