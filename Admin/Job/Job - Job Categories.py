import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class AdminTest(unittest.TestCase):
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_redirect_page_to_job_cat(self):
    
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
        job_cat = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[4]/a")
        work_shift = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[5]/a")

        actions = ActionChains(browser)
        
        #Click Pay Grade
        actions.move_to_element(job).move_to_element(job_cat).click().perform()
        time.sleep(3)

        #Validate
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/jobCategory" 
        self.assertEqual(expected_current_url, browser.current_url)

    def test_b_add_job_categories(self):

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
        job_cat = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[4]/a")
        work_shift = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[5]/a")

        actions = ActionChains(browser)
        
        #Click Pay Grade
        actions.move_to_element(job).move_to_element(job_cat).click().perform()
        time.sleep(3)

        #Validate
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/jobCategory" 
        self.assertEqual(expected_current_url, browser.current_url)

        #Add Job Categories
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME, "jobCategory[name]").send_keys("Nyapu Lantai1")
        time.sleep(1)
        browser.find_element(By.NAME, "btnSave").click()
        time.sleep(3)

        #Validation
        success_job_cat = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[2]/form/div[4]/table/tbody/tr/td[2]/a").text
        self.assertEqual(success_job_cat, "Nyapu Lantai1")

    def test_c_add_job_categories_failed(self):

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
        job_cat = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[4]/a")
        work_shift = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[5]/a")

        actions = ActionChains(browser)
        
        #Click Pay Grade
        actions.move_to_element(job).move_to_element(job_cat).click().perform()
        time.sleep(3)

        #Validate
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/jobCategory" 
        self.assertEqual(expected_current_url, browser.current_url)

        #Add Job Categories
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME, "jobCategory[name]").send_keys("asadadsdasdassdasasdasdadadsadflkslkelkejglkejlkelke")
        time.sleep(1)
        browser.find_element(By.NAME, "btnSave").click()
        time.sleep(3)

        #Validation
        error_job_cat = browser.find_element(By.XPATH, "//span[contains(text(),'Should be less than 50 characters')]").text
        self.assertEqual(error_job_cat, "Should be less than 50 characters")

    def test_d_delete_job_categories_success(self):
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
        job_cat = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[4]/a")
        work_shift = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[5]/a")

        actions = ActionChains(browser)
        
        #Click Pay Grade
        actions.move_to_element(job).move_to_element(job_cat).click().perform()
        time.sleep(3)

        #Validate
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/jobCategory" 
        self.assertEqual(expected_current_url, browser.current_url)

        #Delete Job Categories
        browser.find_element(By.NAME, "")


    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()