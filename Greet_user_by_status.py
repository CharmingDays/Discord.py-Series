import discord
from discord.ext import commands
import asyncio
yakumo = commands.Bot(command_prefix='y.')


@yakumo.event
async def on_ready():
    print(yakumo.user.name)


@yakumo.event
async def on_member_update(before:discord.Member,after:discord.Member): # YOU CAN CUSTOMIZE YOUR OWN MESSAGES AND EVENTS
    if before.status == discord.Status.offline and after.status == discord.Status.online:
        await yakumo.send_message(before,'Welcome back online {}!'.format(before.name))
    
    if before.status == discord.Status.online and after.status == discord.Status.offline:
        await yakumo.send_message(before,'See you next time {}!'.format(before.name))

    if before.status == discord.Status.online and after.status == discord.Status.idle:
        await yakumo.send_message(before,'See around')

    if before.status == discord.Status.online and after.status == discord.Status.dnd:
        await yakumo.send_message(after,'Okay, I\'ll message you later then {}'.format(before.name))

yakumo.run('BOT TOKEN HERE')
