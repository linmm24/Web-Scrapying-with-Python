from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
#建立一个几何
pages=set()
def getLinks(pageUrl):
    #global告诉python这个变量是全局的，就可以给函数外的变量赋值
    global pages
    html=urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj=BeautifulSoup(html)
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("页面缺少一些属性！不过不用担心!")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href'in link.attrs:
            if link.attrs['href'] not in pages:
                #我们遇到了新页面
                newPage=link.attrs['href']
                print("----------------\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)

#初始化，空的url就是http://en.wikipedia.org
getLinks("")