#通过获取维基百科的一个页面的链接，再从这些链接中随机选一个链接访问，不断向外扩张访问
#自己可不可以找一个网站试一下。不断访问这个网站的不同目录

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
#产生不同的随机数就需要用当前时间作为种子
random.seed(datetime.datetime.now())
#维基百科词条 /wiki/< 词条名称 > 形式的 URL 链接作为参数， 然后以同样的形式返回一个列表，里面包含所有的词条 URL 链接。
def getLinks(articleUrl):
   # html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
#初始化第一个页面
links=getLinks("/wike/Kevin_Bacon")
while len(links)>0:
    #从返回的词条链接中随机选一条作为链接，这样就可以从一个页面到另一个页面的爬取
    newArticle=links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    links=getLinks(newArticle)
