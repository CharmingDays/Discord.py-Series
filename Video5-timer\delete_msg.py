tc=[]
@yakumo.command(pass_context=True)
async def timer(con,time=10):
    timer = time
    ct = con.message.channel.id
    if ct in tc:
        await yakumo.send_message(con.message.channel, "Please wait for the current timer to complete.")
    elif ct not in tc:
        msg = await yakumo.send_message(con.message.channel, time)
        tc.append(con.message.channel.id)
        for i in range(time):
            await asyncio.sleep(1)
            timer -= 1
            await yakumo.edit_message(msg, new_content=timer)
        num = tc.index(ct)
        del tc[num]
        await yakumo.send_message(con.message.channel, "{} seconds timer complete in the channel!".format(time))
