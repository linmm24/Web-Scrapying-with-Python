import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj=BeautifulSoup(html)
#下载的是页面上的表格，1表示第二个
table=bsObj.findAll("table",{"class":"wikitable"})[0]
rows=table.findAll("tr")

csvFile=open("../python网络数据采集/editors.csv",'wt',newline='',encoding='utf-8')
writer=csv.writer(csvFile)
try:
    for row in rows:
        csvRow=[]
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()