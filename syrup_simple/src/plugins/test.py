from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
from nonebot import CommandGroup

test1=on_command('test1')

@test1.handle()
async def test1_handle(bot:Bot,event:Event):
    await test1.pause('give your cmd')

@test1.handle()
async def test1_handle(bot:Bot,event:Event):
    await test1.send(str(event.get_message))
    await test1.send(str(event.get_plaintext))
    await test1.send(str(event.get_event_name))
    await test1.finish()