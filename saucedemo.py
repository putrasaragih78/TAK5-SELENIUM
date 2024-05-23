import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.saucePage import loginPage, loginData

class SaucedemoTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
      

    def test_a_login_success(self):
        browser = self.browser 
        browser.get(loginData.url)
        self.assertIn(loginData.tittle, self.browser.title)
        browser.find_element(By.NAME, loginPage.user).send_keys(loginData.user_valid)
        browser.find_element(By.NAME, loginPage.psw).send_keys(loginData.pass_valid)
        browser.find_element(By.ID, loginPage.login_btn).click()
        url = browser.current_url
        self.assertEqual(url, loginData.url_login)
        browser.quit()

    def test_b_login_failed(self):
        browser = self.browser 
        browser.get('https://www.saucedemo.com/')
        self.assertIn('Swag Labs', self.browser.title)
        browser.find_element(By.NAME, 'user-name').send_keys('salah_user')
        browser.find_element(By.NAME, 'password').send_keys('secret_sauce')
        browser.find_element(By.ID, 'login-button').click()
        browser.find_element(By.CSS_SELECTOR, '[data-test="error"]')
        error_msg = browser.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
        self.assertIn('Username and password do not match', error_msg)
        browser.quit()
       
    def test_c_login_locked(self):
        browser = self.browser 
        browser.get('https://www.saucedemo.com/')
        self.assertIn('Swag Labs', self.browser.title)
        browser.find_element(By.NAME, 'user-name').send_keys('locked_out_user')
        browser.find_element(By.NAME, 'password').send_keys('secret_sauce')
        browser.find_element(By.ID, 'login-button').click()
        browser.find_element(By.CSS_SELECTOR, '[data-test="error"]')
        error_msg = browser.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
        self.assertIn('his user has been locked out', error_msg)  
        browser.quit()

if __name__ == '__main__':
    unittest.main()