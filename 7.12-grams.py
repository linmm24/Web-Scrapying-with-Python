from urllib.request import urlopen
from bs4 import BeautifulSoup

#ngrams 函数把一个待处理的字符串分成单词序列（假设所有单词按照空格分开），
# 然后增 加到 n-gram 模型（本例中是 2-gram）里形成以每个单词开始的二元数组
#input 待处理的字符串，n数组的长度
def getNgrams(input, n):
  input = input.split(' ')
  output = []
  for i in range(len(input)-n+1):
    output.append(input[i:i+n])
  return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
ngrams = getNgrams(content, 2)
print(ngrams)
print("2-grams count is: "+str(len(ngrams)))