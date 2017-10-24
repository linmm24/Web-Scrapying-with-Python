from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)
dictReader = csv.DictReader(dataFile)
#csv.DictReader 会返回把 CSV 文件每一行转换成 Python 的字典对象返回，
# 而不是列表对 象，并把字段列表保存在变量 dictReader.fieldnames 里，字段列表同时作为字典对象的键
print(dictReader.fieldnames)

for row in dictReader:
    print(row)