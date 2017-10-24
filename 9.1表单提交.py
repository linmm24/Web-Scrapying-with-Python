# -*- coding: utf-8 -*-
#!usr/bin/python
from urllib import request,parse
import http.cookiejar
import urllib
import re
#模拟登录测试模块
print('loging info my ssfw')
cookie=http.cookiejar.CookieJar()#储存获取到的cookie
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
loging_data=parse.urlencode([
    ('zj4',"140604132"),
    ('mm',"076134"),
    ('v_yzm','yryy')])#POST用到的数据

#请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '+
    '(KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'
}
#构造request
req=request.Request(url='http://zj2.njust.edu.cn/loginAction.do',
                    data=loging_data.encode(encoding='gbk'),
                    headers=headers)
try:
    result=opener.open(req)#访问请求的链接
    print(result.read().decode('gbk'))
except urllib.error.HTTPError:
    print("connect failed")
