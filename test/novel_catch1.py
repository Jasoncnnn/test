#下载一本小说并存放在指定目录
import urllib.request
from bs4 import BeautifulSoup
import time
import gzip
from urllib.error import HTTPError,URLError
import random

#req_header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
'''
req_header={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie':'_abcde_qweasd=0; __guid=270189431.88115020722726830.1582038501555.4824; _abcde_qweasd=0; bdshare_firstime=1582038502825; Hm_lvt_169609146ffe5972484b0957bd1b46d6=1582038503; monitor_count=3; Hm_lpvt_169609146ffe5972484b0957bd1b46d6=1582038564',
    'Host':'www.xbiquge.la',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}#新笔趣阁
'''
req_header={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie':'__guid=130189705.926614980802380000.1582362419987.4084; clickbids=34538; Hm_lvt_6dfe3c8f195b43b8e667a2a2e5936122=1582362452; Hm_lvt_c979821d0eeb958aa7201d31a6991f34=1582362421,1582362456; monitor_count=4; Hm_lpvt_6dfe3c8f195b43b8e667a2a2e5936122=1582362481; Hm_lpvt_c979821d0eeb958aa7201d31a6991f34=1582362482',
    'Host':'www.biquge.info',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}#笔趣阁

#iplist=['123.163.96.80:9999','58.247.127.145:53281','183.196.168.194:9000','123.139.56.238:9999','119.57.108.109:53281']

#打开并返回整个网页
def url_open(url):
    '''
    proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})
    opener=urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    '''
    request = urllib.request.Request(url,headers=req_header)
    response = urllib.request.urlopen(request)
    content = gzip.decompress(response.read())
    data = content.decode('utf-8','ignore')

    return data

class novel_catch(object):

    def __init__(self,url):#init两边各有两个_
        self.url = url
        self.chapter_names = []#存放章节名称
        self.chapter_hrefs = []#存放章节链接

    #获取章节名称和章节URL
    def get_catalogue(self):
        response=url_open(self.url)
        soup = BeautifulSoup(response, "html.parser")
        #chapter_hrefs=re.findall('/\d\d/\d\d\d\d\d/\d\d\d\d\d\d\d\.html',soup)
        a=soup.find('div',id='list')
        #print(a)
        for i in a.dl:
            if i.name=='dd':
                self.chapter_names.append(i.string)
                self.chapter_hrefs.append('http://www.biquge.info/34_34538/'+i.a['href'])
        self.novel_name=soup.find('div',id='info').h1.string
    
    #获取对应章节的内容
    def get_chapter_text(self,url):
        try:
            response=url_open(url)       
            soup = BeautifulSoup(response, "lxml")
            a=soup.find('div',id='content')
            text=''
            for i in a:
                if i.name!='img' and i.name!='a' and i.name!='p' and i.name!='br' and i.name!='strong' and i.name!='h1' and i.name!='script' and i.name!='div' and i.name!='table' and i.name!='td' and i.name!='tr':
                    text+=(i.string+'\n\n')
        
            return text
        except HTTPError as e:
            print(e.code)
            print("获取章节内容失败,1秒后重试！")
            time.sleep(1)
            self.get_chapter_text(url)
        except URLError as e:
            print(e.reason)
            print("获取章节内容失败,1秒后重试！")
            time.sleep(1)
            self.get_chapter_text(url)
        except Exception as e:
            print(e)
            print("获取章节内容失败,1秒后重试！")
            time.sleep(1)
            self.get_chapter_text(url)
    
    #写入txt文档
    def writer(self,name,path,text1):
        with open(path,'a',encoding='utf-8') as f:
            f.write(name+'\n')           
            f.write(text1)
            f.write('\n\n')







    
if __name__ == "__main__":
    novel_1=novel_catch('http://www.biquge.info/34_34538/')

    novel_1.get_catalogue()

    for i in range(len(novel_1.chapter_names)):
        name=novel_1.chapter_names[i]
        text=str(novel_1.get_chapter_text(novel_1.chapter_hrefs[i]))
        novel_1.writer(name,'F:\学习资料\程序设计\python练习代码\\'+novel_1.novel_name+'.txt',text)
        print(name+'\t下载完成',i)
        time.sleep(random.choice([0.3,1,1.5,2]))

    print('successful')
    #打开书的目录获取章节名字和链接地址
    #catalogue_catch()








