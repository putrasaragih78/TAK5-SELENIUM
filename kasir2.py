import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.loginPage import login

class KasirTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
      

    def test_login_success(self):
        browser = self.driver
        browser.get('https://kasirdemo.belajarqa.com/')
        self.assertIn('kasirAja', browser.title)
        browser.find_element(By.ID, 'email').send_keys('saragih78putra@gmail.com')
        browser.find_element(By.ID, 'password').send_keys('1234@')
        browser.find_element(By.CSS_SELECTOR, login.login_btn).click()
        self.assertEqual(browser.current_url, 'https://kasirdemo.belajarqa.com/login')

   

if __name__ == '__main__':
    unittest.main()