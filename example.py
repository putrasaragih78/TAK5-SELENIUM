from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://www.saucedemo.com/')
browser.find_element(By.NAME, 'user-name').send_keys('standard_user')
browser.find_element(By.NAME, 'password').send_keys('secret_sauce')