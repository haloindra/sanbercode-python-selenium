import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class AdminTest(unittest.TestCase):
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_redirect_page_to_job_pay_grade(self):
        
        #Login
        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login") 
        time.sleep(3)
        browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() 
        time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(2)
        #Hover to Job Title
        job = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/a")
        job_title = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[1]/a")
        pay_grade = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[2]/a")

        actions = ActionChains(browser)
        
        #Click Pay Grade
        actions.move_to_element(job).move_to_element(pay_grade).click().perform()
        time.sleep(3)

        #Validate
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewPayGrades" 
        self.assertEqual(expected_current_url, browser.current_url)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()