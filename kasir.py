import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class KasirTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
      

    def test_login(self):
        browser = self.driver 
        browser.get('https://kasirdemo.belajarqa.com/')
        self.assertIn('kasirAja', browser.title)
        browser.find_element(By.ID, 'email').send_keys('saragih78putra@gmail.co')
        browser.find_element(By.ID, 'password').send_keys('1234@')
        browser.find_element(By.CSS_SELECTOR, '.chakra-button.css-1n8i4of').click()
        self.assertEqual(browser.current_url, 'https://kasirdemo.belajarqa.com/login')

   

if __name__ == '__main__':
    unittest.main()