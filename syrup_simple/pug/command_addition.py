import json
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message

def find_key(s,a):
    for i in range(len(s)):
        if s[i] in a:
            return i

ctlprt=on_command('ctlprt')

@ctlprt.handle()
async def ctlprt_handle(bot:Bot,event:Event):
    full_manage=str(event.get_message())
    ctlcontent=full_manage.strip('/ctlprt ')
    key_position=find_key(ctlcontent,['+'])
    key=ctlcontent[:key_position]
    ctl=ctlcontent[key_position+1:]
    operation=ctlcontent[key_position]
    file=open('priority.json','w+')
    ori=json.load(file)
    if event.get_user_id() not in ori['Master']:
        await ctlprt.finish(message=Message("you ** who"))
    if operation=='+':
        addtext={key:ctl}
        json.dump(addtext,file,ensure_ascii=False)
        await ctlprt.finish(message=Message(f"{ctl} append in {key} already"))