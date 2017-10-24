import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='G:/APP/pycharm/phantomjs-2.1.1-windows/bin/phantomjs')
#driver = webdriver.Firefox()
driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
time.sleep(2)
#单击图片预览按钮
driver.find_element_by_id("img-canvas").click()
#The easiest way to get exactly one of every page
imageList = set()

#等待页面加载完成
time.sleep(5)
#当向右箭头可以点击时，开始翻页
print(driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"))
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
    #While we can click on the right arrow, move through the pages
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(2)
    # 获取已加载的新页面（一次可以加载多个页面，但是重复的页面不能加载到集合中）
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute("src")
        imageList.add(image)

driver.quit()

# 用Tesseract处理我们收集的图片URL链接
for image in sorted(imageList):
    urlretrieve(image, "page.jpg")
    p = subprocess.Popen(["tesseract", "page.jpg", "page"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p.wait()
    f = open("page.txt", "r")
    print(f.read())
