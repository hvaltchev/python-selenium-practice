#!/usr/bin/env python3

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("http://www.apple.com/shop/studio/apple-watch")

driver.implicitly_wait(5) # seconds
#Enter Get started button
startbtn = driver.find_element_by_xpath("//html/body/div[2]/div[4]/div/div/div[3]/div[1]/div/div[1]/div/div/button/span")
startbtn.click()
#initialize three variables size, case, and band

#click on size
#traverse and count options EXIT CONDITION BUTTON IS NOT ON THE PAGE
sizebtn = driver.find_element_by_xpath("//html/body/div[2]/div[4]/div/div/div[4]/div[1]/div/div[1]")
sizebtn.click()

nextbtn = driver.find_element_by_xpath("//html/body/div[2]/div[4]/div/div/div[3]/div[2]/div/div[2]/button[2]")
nextbtn.click()
driver.implicitly_wait(5)

#click on case 
#click on Aluminum
#traverse and count options EXIT CONDITION BUTTON IS NOT ON THE PAGE

sizebtn = driver.find_element_by_xpath("//html/body/div[2]/div[4]/div/div/div[4]/div[1]/div/div[2]")
sizebtn.click()

driver.implicitly_wait(5)
nextbtn = driver.find_element_by_xpath("//html/body/div[2]/div[4]/div/div/div[3]/div[3]/div/div[2]/button[2]")

while(1):
    if nextbtn.is_displayed():
        nextbtn = driver.find_element_by_xpath("//html/body/div[2]/div[4]/div/div/div[3]/div[2]/div/div[2]/button[2]")
        nextbtn.click()
    elif nextbtn.is_displayed() == 0:
        break

#click on band
#click on sport band
#traverse and count options EXIT CONDITION BUTTON IS NOT ON THE PAGE

sizebtn = driver.find_element_by_xpath("//html/body/div[2]/div[4]/div/div/div[4]/div[1]/div/div[1]")
sizebtn.click()

nextbtn = driver.find_element_by_xpath("//html/body/div[2]/div[4]/div/div/div[3]/div[2]/div/div[2]/button[2]")
nextbtn.click()

driver.wait(10)
driver.close()
