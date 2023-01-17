import random
from datetime import date
from nonebot import on_keyword
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message



def ys_simple(ys):
    if ys < 20:
        return '大吉'
    elif ys < 55:
        return '吉'
    elif ys < 60:
        return '中平'
    elif ys < 67:
        return '凶'
    elif ys < 73:
        return '大凶'
    else:
        return '寄'
    

jrys = on_keyword(['今日运势','运势'])
drys = on_keyword(['明日运势','后日运势'])

unable_user=['2150738692']


@jrys.handle()
async def jrys_handle(bot: Bot, event: Event):
    if event.get_user_id() not in unable_user:
        rnd = random.Random()
        rnd.seed(( int(date.today().strftime("%y%m%d"))*45 )*( int(event.get_user_id())*55 ))
        yunshi = rnd.randint(1,100)
    
        await jrys.finish(message = Message(f'[CQ:at,qq={event.get_user_id()}]您今日的运势为"{ys_simple(yunshi)}"'))


@drys.handle()
async def drys_handle(bot:Bot,event:Event):
    await drys.finish(message=Message(f'[CQ:at,qq={event.get_user_id()}]😅您搁这预知未来呢'))