#!/usr/bin/env python3

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.google.com')
print(driver.title)
#driver.quit()
