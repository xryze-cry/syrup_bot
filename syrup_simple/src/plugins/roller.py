from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, Message, Event
import random

roller=on_keyword(['。rd'])

@roller.handle()
async def numbers(bot: Bot, event: Event, state: T_State):
    allstr = str ( event.get_message () ).strip ()
    mngstr = allstr.strip ( '。rd' )
    explaintext=''
    for i in range (len(mngstr)):
        if mngstr[i] not in '0123456789':
            toprange=int(mngstr[0:i])
            explaintext=mngstr[i:]
            break
    if explaintext == '':
        toprange=int(mngstr)
    rolled_number=random.randint(1,toprange)
    if explaintext=='':
        await roller.finish (Message(f'[CQ:at,qq={event.get_user_id()}]\n火中的骰子缓缓浮现出了数字:{rolled_number}')) 
    else:
        await roller.finish (Message(f'[CQ:at,qq={event.get_user_id()}]\n{explaintext}:\n火中的骰子缓缓浮现出了数字:{rolled_number}')) 
