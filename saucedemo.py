import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SaucedemoTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
      

    def test_login(self):
        browser = self.browser 
        browser.get('https://www.saucedemo.com/')
        self.assertIn('Swag Labs', self.browser.title)
        browser.find_element(By.NAME, 'user-name').send_keys('standard_user')
        browser.find_element(By.NAME, 'password').send_keys('secret_sauce')
        browser.find_element(By.ID, 'login-button').click()
        url = browser.current_url
        self.assertEqual(url, 'https://www.saucedemo.com/inventory.html')

    def test_login_failed(self):
        browser = self.browser 
        browser.get('https://www.saucedemo.com/')
        self.assertIn('Swag Labs', self.browser.title)
        browser.find_element(By.NAME, 'user-name').send_keys('salah_user')
        browser.find_element(By.NAME, 'password').send_keys('secret_sauce')
        browser.find_element(By.ID, 'login-button').click()
        browser.find_element(By.CSS_SELECTOR, '[data-test="error"]')
       
        

if __name__ == '__main__':
    unittest.main()