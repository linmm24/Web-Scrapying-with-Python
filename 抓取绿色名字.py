from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
#创建一个 BeautifulSoup 对象
bsObj=BeautifulSoup(html)
# bsObj.tagName 只能获取页面中的第一个指定的标签
# bsObj.findAll(tagName, tagAttributes) 可以获取页面中所有指定的标签，不再只是 第一个了,前面是标签名后面是条件。
nameList=bsObj.findAll({"span"},{"class":"green"})
#nameList=bsObj.findAll({"h1","h2","h3","h4","h5","h6"})

for name in nameList:
    print(name.get_text())
    #.get_text() 会把你正在处理的 HTML 文档中所有的标签都清除，然后返回 一个只包含文字的字符串