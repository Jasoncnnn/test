import urllib
import urllib.request
import multiprocessing
from bs4 import BeautifulSoup
import re
import os
import time
import gzip

#请求头字典
'''
req_header={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie':'_abcde_qweasd=0; __guid=270189431.88115020722726830.1582038501555.4824; _abcde_qweasd=0; bdshare_firstime=1582038502825; Hm_lvt_169609146ffe5972484b0957bd1b46d6=1582038503; monitor_count=3; Hm_lpvt_169609146ffe5972484b0957bd1b46d6=1582038564',
    'Host':'www.xbiquge.la',
    'Referer':'http://www.xbiquge.la/15/15409/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
'''
req_header={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate,br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie':'__guid=164384313.2702753913022171000.1582350790041.1296; monitor_count=7; Hm_lvt_40639e2e855ad00c65304ee021f07859=1582350791,1582350927,1582351069,1582351277; Hm_lpvt_40639e2e855ad00c65304ee021f07859=1582351277',
    'Host':'www.booktxt.net',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
url='https://www.booktxt.net/0_436/92583.html'
# 请求当前章节页面  params为请求参数
request = urllib.request.Request(url,headers=req_header)
response = urllib.request.urlopen(request)
content = gzip.decompress(response.read())
data = content.decode('gb2312','ignore')
# soup转换
soup = BeautifulSoup(data, "lxml")
#print(soup)
a=soup.find('div',id='content')

text=''
'''
if a.select('h1')==[]:
    for i in a:
        if i.name!='p' and i.name!='br' and i.name!='h1' and i.name!='script' and i.name!='div':
            text+=(i.string+'\n')
else:
    for i in a.table.table.table.table:
        #print(i.name,'\n')
        if i.name!='p' and i.name!='br' and i.name!='h1' and i.name!='script' and i.name!='div' and i.name!='table' and i.name!='td' and i.name!='tr':
            text+=(i.string+'\n')
'''
print(a)


'''
for i in range(len(text)):
    print(text[i])
        #print(i.name)

print(a.replace_with())
 '''   

#print(a.select('h1')==[])
print(text)

