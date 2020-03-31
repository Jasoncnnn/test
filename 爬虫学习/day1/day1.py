#判断是否可以爬取某网页
import urllib.request
import urllib.parse
import urllib.error
import socket
from urllib.robotparser import RobotFileParser
'''
data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
response=urllib.request.urlopen('http://httpbin.org/post',data=data)
'''
rp=RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
print(rp.read())
'''
print(rp.can_fetch('*','http://www.biquge.info/34_34538/'))
print(rp.can_fetch('*','http://www.biquge.info/'))
'''

#print(response.read(),'seq=',sep='\n')

