from selenium import webdriver
import time

#REPLACE WITH YOUR DRIVER PATH. EXAMPLES FOR CHROME AND PHANTOMJS
#phantomjs可执行文件的目录
driver = webdriver.PhantomJS(executable_path='G:/APP/pycharm/phantomjs-2.1.1-windows/bin/phantomjs')
#driver = webdriver.Chrome(executable_path='../chromedriver/chromedriver')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
#等待五秒。那时页面已经刷新了
time.sleep(5)
#输出页面刷新后的内容，选择器用的是选择器是 find_element_by_id
print(driver.find_element_by_id("content").text)
driver.close()