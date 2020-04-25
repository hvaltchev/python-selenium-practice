#!/usr/bin/env python3

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://www.indeed.com/")

driver.implicitly_wait(5) # seconds
#Enter Get started button
job = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div/div/form/div[1]/div[1]/div/div[2]/input")
loc = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div/div/form/div[2]/div[1]/div/div[2]/input")
job.clear()
job.send_keys("Quality Assurance Engieer")
job.send_keys(u'\ue004')
loc.send_keys("Santa Clara")
loc.send_keys(u'\ue007')
