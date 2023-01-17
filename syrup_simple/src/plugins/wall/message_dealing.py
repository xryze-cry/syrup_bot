import re
def md(s):
    text=''
    imglist=re.findall('url=.*]',s)
    drop=re.findall('[CQ.*]',s)
    a=s
    for i in range(len(imglist)):
        imglist[i]=imglist[i].strip('url=').strip(']')

    for i in range(len(drop)-1,-1,-1):
        a.strip(drop[i])

    text=a
    return text,imglist


