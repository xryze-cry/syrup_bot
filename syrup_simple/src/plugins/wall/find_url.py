import os
def fr():
    with open('C:\\Users\\Administrator\\Desktop\\syrup\\func\\wall\\No.txt','r+') as r:
        num=int(r.readline())+1
        r.seek(0)
        r.write(str(num))
    No=str(num)
    if len(No) != 6:
        for i in range(0,6-len(No)):
            No='0'+No
        url=f'C:\\Users\\Administrator\\Desktop\\syrup\\func\\wall\\{No}'
        os.mkdir(url)
    return No

def dd(url):
    os.rmdir(url)

def li(url):
    list=os.listdir(url)
    if 'img.txt' in list:
        return 1
    else:
        return 0