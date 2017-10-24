from selenium import webdriver


driver = webdriver.PhantomJS(executable_path='G:/APP/pycharm/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get("http://en.wikipedia.org/wiki/Monty_Python")
assert "Monty Python" in driver.title
print("Monty Python was not in the title")
driver.close()