from urllib.request import urlopen
from bs4 import BeautifulSoup
#正则表达式re模块
import re
html=urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj=BeautifulSoup(html)
#.不能直接表示，要转义\.    img.*表示匹配img后面加任意单个字符
images=bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])