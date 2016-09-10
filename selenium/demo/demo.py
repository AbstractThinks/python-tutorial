# -*- coding: utf-8 -*-

from selenium import webdriver
import time

browser = webdriver.Firefox()
# browser.get("http://www.baidu.com")
time.sleep(5)
print("Browser will be closed")
browser.quit()
print("Browser is close")