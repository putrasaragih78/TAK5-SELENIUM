import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.loginPage import login,loginData

class KasirTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
      

    def test_a_login_success(self):
        browser = self.driver
        browser.get(loginData.url)
        self.assertIn(loginData.title, browser.title)
        browser.find_element(By.ID, login.email).send_keys(loginData.email)
        browser.find_element(By.ID, login.passw).send_keys(loginData.passw)
        browser.find_element(By.CSS_SELECTOR, login.login_btn).click()
        self.assertEqual(browser.current_url, login.login_url)

    def test_b_login_failed(self):
        browser = self.driver
        browser.get(loginData.url)
        self.assertIn(loginData.title, browser.title)
        browser.find_element(By.ID, login.email).send_keys(loginData.email_invalid)
        browser.find_element(By.ID, login.passw).send_keys(loginData.passw)
        error_msg = browser.find_element(By.CSS_SELECTOR, '[role="alert"]').text
        self.assertIn('must be a valid email', error_msg)
      

if __name__ == '__main__':
    unittest.main()