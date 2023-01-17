from email import message
import re
import random
from tokenize import group
import requests
import json

from datetime import date
from nonebot import on_keyword,on_fullmatch
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message

#    if list['data']==[]:
#        await rdsetu.finish(message=Message(f'[CQ:at,qq={event.get_user_id()}]'))

orisrc = 'https://api.lolicon.app/setu/v2'


rdsetu = on_fullmatch('随机涩图')
taggedsetu = on_keyword([])

file=open('priority.json','r')
able_group=json.load(file)["randomsetu"]

@rdsetu.handle()
async def rdsetu_handle(bot:Bot,event:Event):
    list1=str(event.get_session_id).split(',')
    group_id_manage1=list1[24]
    group_id=re.findall('\d*$',group_id_manage1)[0]
    if 'GroupMessageEvent' in str(event.get_session_id):
        if group_id not in able_group:
            await rdsetu.finish(message=Message(f'[CQ:at,qq={event.get_user_id()}]该群无此功能权限'))



        r = requests.get(orisrc).text

        list=json.loads(r)



        pname=list['data'][0]['title']
        pid=list['data'][0]['pid']
        pauthor=list['data'][0]['author']
        url=f'http://pixiv.re/{pid}.jpg'

        await rdsetu.finish(message=Message(f'[CQ:at,qq={event.get_user_id()}]')+Message(f'\n{url}\n作品标题:{pname}\nid:{pid}\n画师昵称:{pauthor}'))

