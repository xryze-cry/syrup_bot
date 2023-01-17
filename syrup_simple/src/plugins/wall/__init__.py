from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message,MessageSegment
from nonebot.permission import SUPERUSER
from nonebot import CommandGroup
import requests

from .find_url import fr,dd,li
from .message_dealing import md

text=''
img=[]
addtopic=on_command('添加话题')
looktopic=on_command('查看话题',permission=SUPERUSER)

@addtopic.handle()
async def addtopic_handle(bot:Bot,event:Event):
    await addtopic.pause('请给出内容')

@addtopic.handle()
async def addtopic_handle(bot:Bot,event:Event):
    url=fr()
    No=url[len(url)-7:]
    text=f'这是墙上的第{No}张留言'
    so=str(event.get_message())
    await addtopic.send(so)
    text_add,img=md(so)
    if text_add=='取消':
        dd("C:\\Users\\Administrator\\Desktop\\syrup\\func\\wall\\"+str(url))
        await addtopic.finish("任务已取消~")
    text+='\n'+text_add
    if len(img) != 0:
        imgattr=''
        for i in range(len(img)):
            if i>=9:
                break
            imgattr+=img[i]+'\n'
        with open("C:\\Users\\Administrator\\Desktop\\syrup\\func\\wall\\"+str(url)+"\\img.txt","w") as f:
            f.write(imgattr)



    if text_add != '':
        with open("C:\\Users\\Administrator\\Desktop\\syrup\\func\\wall\\"+str(url)+"\\text.txt","w") as f:
            f.write(text)

    with open("C:\\Users\\Administrator\\Desktop\\syrup\\func\\wall\\"+str(url)+"\\info.txt","w") as f:
        f.write(str(event.get_user_id()+'\n'+'0')) #0→undeal 1→dealed 2→deleted
    await addtopic.finish('已储存')

@looktopic.handle()
async def looktopic_handle(bot:Bot,event:Event):
    No=str(event.get_message()).strip('/查看话题 ')
    if len(No) != 6:
        for i in range(0,6-len(No)):
            No='0'+No
        url=f'C:\\Users\\Administrator\\Desktop\\syrup\\func\\wall\\{No}'
    with open(str(url)+"\\text.txt","r") as f:
        text=f.read()
    await looktopic.send(text)
    if li(url)==1:
        with open(str(url)+"\\img.txt","r") as f:
            img=f.read()
    await looktopic.send(img)

    await looktopic.finish('finish')