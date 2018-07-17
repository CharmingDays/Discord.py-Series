import discord
from discord.ext import commands
import asyncio




#DEFINE BOT NAME AND PREFIX HERE
yakumo=commands.Bot(command_prefix='y.')




#PRINTS THE BOT NAME WHEN READY
@yakumo.event
async def on_ready():
    print(yakumo.user.name)



#PINGS AND MENTIONS USER
@yakumo.command(pass_context=True)
async def ping(msg,user:discord.Member):
    await yakumo.say("{} pinged you {}".format(msg.message.author.mention,user.mention))

#REPEATS WHAT THE USER SAYS
@yakumo.command(pass_context=True)
async def say(ctx,*msg):
    user_msg=ctx.message
    await yakumo.say("{}".format(" ".join(msg)))
    await asyncio.sleep(3)
    await yakumo.delete_message(user_msg)


#SAYS HELLO THERE BACK TO WHO EVER SAYS HI
@yakumo.event
async def on_message(msg):
    if msg.content.upper() == "HI":
        await yakumo.send_message(msg.channel,'Hi there {}!'.format(msg.author.name))
    await yakumo.process_commands(msg)




#GETS INFO OF A TAGGED USER
@yakumo.command(pass_context=True)
async def info(msg,user:discord.Member):
    await yakumo.say("{}\n{}".format(user.id,user.nick))




#RUNS THE BOT.
#PLEASE MAKE SURE YOU PUT BOT_NAME.RUN('BOT TOKEN') AT THE END OF YOUR CODE LIKE MINE OR IT WILL CAUSE ISSUES
yakumo.run('Your Bot Token Here')
