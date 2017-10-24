import  csv
#绝对路径为G:\APP\pycharm\PycharmProjects\python网络数据采集\test.csv
csvFile=open("../python网络数据采集/test.csv",'w+')
try:
    writer=csv.writer(csvFile)
    #写入标题栏
    writer.writerow(('number','number plus 2','number times 2'))
    for i in range(10):
        writer.writerow((i,i+2,i*2))
finally:
    csvFile.close()