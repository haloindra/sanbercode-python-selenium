import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_login_sucsess(self):
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol Masuk
        time.sleep(5)

        # validasi
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/dashboard"
        self.assertEqual(expected_current_url, browser.current_url)


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()