'''
Created on May 2, 2018

@author: HP ProBook
'''
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
browser = webdriver.Chrome("D:\\EclipseWorkspace\\Selenium\\src\\chromedriver.exe")
browser.get("http://www.facebook.com")
username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")
submit = browser.find_element_by_id("submit")

username.send_keys( "letam0023@gmail.com" )
password.send_keys( "yhbb227525" )


submit.click()
wait = WebDriverWait( browser, 5 )

try:
page_loaded = wait.until_not(
lambda browser: browser.current_url == login_page
)
except TimeoutException:
self.fail( "Loading timeout expired" )

self.assertEqual(
browser.current_url,
correct_page,
msg = "Successful Login"
)