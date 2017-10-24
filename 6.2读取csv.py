from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)
# csv.reader 返回的 csvReader 对象是可迭代
for row in csvReader:
	print("The album \""+row[0]+"\" was released in "+str(row[1]))