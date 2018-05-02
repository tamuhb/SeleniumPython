'''
Created on May 2, 2018

@author: HP ProBook
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user = "letam0023@gmail.com"
pwd = "yhbb227525"
driver = webdriver.Chrome("D:\\EclipseWorkspace\\Selenium\\src\\chromedriver.exe")

driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()