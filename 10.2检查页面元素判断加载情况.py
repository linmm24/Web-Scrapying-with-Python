from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#DOM 触发的状态是用 expected_conditions 定义的取别名EC
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# WebDriverWait 和 expected_conditions，
# 这两个模块组合起来构成了 Selenium 的隐式等待（implicit wait）。

driver = webdriver.PhantomJS(executable_path='G:/APP/pycharm/phantomjs-2.1.1-windows/bin/phantomjs')
#driver = webdriver.Chrome(executable_path='../chromedriver/chromedriver')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try:
    #判断页面有咩有id为loadedButton的元素
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loadedButton")))
finally:
    print(driver.find_element_by_id("content").text)
    #print(driver.find_element(By.ID, "content").text)与上面的等价
    driver.close()