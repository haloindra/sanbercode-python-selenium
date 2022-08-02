import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class AdminTest(unittest.TestCase):
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_redirect_page_to_employment_stat(self):
    
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
        employ_stat = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[3]/a")

        actions = ActionChains(browser)
        
        #Click Pay Grade
        actions.move_to_element(job).move_to_element(employ_stat).click().perform()
        time.sleep(3)

        #Validate
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/employmentStatus" 
        self.assertEqual(expected_current_url, browser.current_url)

    def test_b_add_employment_status(self):
        
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
        employ_stat = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[3]/a")

        actions = ActionChains(browser)
        
        #Click Pay Grade
        actions.move_to_element(job).move_to_element(employ_stat).click().perform()
        time.sleep(3)

        #Validate URL
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/employmentStatus" 
        self.assertEqual(expected_current_url, browser.current_url)

        #Add Employment Status
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME, "empStatus[name]").send_keys("Sedang Bekerja")
        time.sleep(1)
        browser.find_element(By.NAME,"btnSave").click()
        time.sleep(3)

        #Validation
        add_status_success = browser.find_element(By.LINK_TEXT, "Sedang Bekerja").text
        self.assertEqual(add_status_success, "Sedang Bekerja")
        
    def test_c_add_employment_status_fail(self):
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
        employ_stat = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[3]/a")

        actions = ActionChains(browser)
        
        #Click Pay Grade
        actions.move_to_element(job).move_to_element(employ_stat).click().perform()
        time.sleep(3)

        #Validate URL
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/employmentStatus" 
        self.assertEqual(expected_current_url, browser.current_url)

        #Add Employment Status
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME, "empStatus[name]").send_keys("   ")
        time.sleep(1)

        #Validation 
        required = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/span").text
        self.assertEqual(required, "Required")

        browser.find_element(By.NAME,"btnSave").click()
        time.sleep(3)
    
    def test_d_delete_employment_status(self):
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
        employ_stat = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[3]/a")

        actions = ActionChains(browser)
        
        #Click Pay Grade
        actions.move_to_element(job).move_to_element(employ_stat).click().perform()
        time.sleep(3)

        #Validate URL
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/employmentStatus" 
        self.assertEqual(expected_current_url, browser.current_url)

        #Delete Employment Status
        browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[2]/form/div[4]/table/tbody/tr[1]/td[1]/input").click()
        time.sleep(1)
        browser.find_element(By.NAME, "btnDelete").click()
        time.sleep(1)
        browser.find_element(By.ID, "dialogDeleteBtn").click()
        time.sleep(1)


    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()