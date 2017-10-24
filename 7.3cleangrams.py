from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict


#可以用来统计一篇文章单词出现的频率，来判断文章的主旨，或者通过单词所在的句子来总结
def cleanInput(input):
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def getNgrams(input, n):
    input = cleanInput(input)
    #dict() 函数用于创建一个字典。返回一个字典
    output = dict()
    for i in range(len(input)-n+1):
        newNGram = " ".join(input[i:i+n])
        if newNGram in output:
            output[newNGram] += 1
        else:
            output[newNGram] = 1
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
#ngrams = getNgrams(content, 2)
#print(ngrams)
#print("2-grams count is: "+str(len(ngrams)))

ngrams = getNgrams(content, 2)
# OrderedDict类（有序字典） 按照单词出现的次数排序，统计词频
ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
print(ngrams)