from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
wordObj=BeautifulSoup(xml_content.decode('utf-8'),"html.parser")
textStrings=wordObj.find("w:t")
#长度应该不是1，这里还有问题
print(len(textStrings))
for textElem in textStrings:
    print(textElem)


