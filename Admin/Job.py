import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class AdminTest(unittest.TestCase):
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_redirect_page_to_job_all_submenu(self):
        
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

        #Click Job Title
        actions.move_to_element(job).move_to_element(job_title).click().perform()
        time.sleep(3)

        #Validate
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewJobTitleList"
        self.assertEqual(expected_current_url, browser.current_url)

        browser.execute_script("window.history.go(-1)")
        
        #Click Pay Grade
        actions.move_to_element(job).move_to_element(pay_grade).click().perform()
        time.sleep(3)

        #Validate
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewPayGrades" 
        self.assertEqual(expected_current_url, browser.current_url)

        browser.execute_script("window.history.go(-1)")

        #Click Employment Stats
        actions.move_to_element(job).move_to_element(employ_stat).click().perform()
        time.sleep(3)

        #Validate
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/employmentStatus"
        self.assertEqual(expected_current_url, browser.current_url)

        browser.execute_script("window.history.go(-1)")
        
        #Click Job Categori
        actions.move_to_element(job).move_to_element(job_cat).click().perform()
        time.sleep(3)

        #Validate
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/jobCategory"
        self.assertEqual(expected_current_url, browser.current_url)

        browser.execute_script("window.history.go(-1)")

        #Click Work Shift
        actions.move_to_element(job).move_to_element(work_shift).click().perform()
        time.sleep(3)

        #Validate
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/workShift"
        self.assertEqual(expected_current_url, browser.current_url)

    def test_b_(self):
        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() 
        time.sleep(1)

        #Redirect User Management
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

        #Search User
        browser.find_element(By.NAME, "searchSystemUser[userName]").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.NAME, "_search").click()
        time.sleep(3)

        #Validate Element
        search_result = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td[2]/a").text
        self.assertEqual(search_result, 'Admin')

    # def test_c_reset_search_success(self):
    #     browser = self.browser 
    #     browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    #     time.sleep(3)
    #     browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
    #     time.sleep(1)
    #     browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
    #     time.sleep(1)
    #     browser.find_element(By.NAME,"Submit").click() 
    #     time.sleep(1)

    #     #Redirect User Management
    #     browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
    #     time.sleep(3)

    #     #Search User
    #     browser.find_element(By.NAME, "searchSystemUser[userName]").send_keys("Admin")
    #     time.sleep(1)
    #     browser.find_element(By.NAME, "_search").click()
    #     time.sleep(3)
      
    #     #Reset Search User
    #     browser.find_element(By.NAME, "_reset").click()
    #     time.sleep(3)

    #     # Validate Reset Search
    #     all_user = browser.find_element(By.NAME,"frmList_ohrmListComponent").text
        
    #     List All User
    #     self.assertEqual(all_user, 'resultTable')
        
    # def test_d_add_user_success(self):
    #     browser = self.browser 
    #     browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    #     time.sleep(3)
    #     browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
    #     time.sleep(1)
    #     browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
    #     time.sleep(1)
    #     browser.find_element(By.NAME,"Submit").click() 
    #     time.sleep(1)

    #     #Redirect User Management
    #     browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
    #     time.sleep(3)

    #     #Add User
    #     browser.find_element(By.NAME, "btnAdd").click()
    #     time.sleep(1)
    #     browser.find_element(By.NAME, "systemUser[employeeName][empName]").send_keys("Admin A")
    #     time.sleep(1)
    #     browser.find_element(By.NAME, "systemUser[userName]").send_keys("tester3")
    #     time.sleep(1)
    #     browser.find_element(By.NAME, "systemUser[password]").send_keys("tester123")
    #     time.sleep(1)
    #     browser.find_element(By.NAME, "systemUser[confirmPassword]").send_keys("tester123")
    #     time.sleep(1)
    #     browser.find_element(By.NAME, "btnSave").click()
    #     time.sleep(3)

    # def test_e_delete_user_success(self):
    #     browser = self.browser 
    #     browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    #     time.sleep(3)
    #     browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
    #     time.sleep(1)
    #     browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
    #     time.sleep(1)
    #     browser.find_element(By.NAME,"Submit").click() 
    #     time.sleep(1)

    #     #Redirect User Management
    #     browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
    #     time.sleep(3)

    #     #Search User
    #     browser.find_element(By.NAME, "searchSystemUser[userName]").send_keys("indraaa")
    #     time.sleep(1)
    #     browser.find_element(By.NAME, "_search").click()
    #     time.sleep(3)

    #     #Delete User
    #     browser.find_element(By.NAME, "chkSelectRow[]").click()
    #     time.sleep(1)
    #     browser.find_element(By.NAME, "btnDelete").click()
    #     time.sleep(1)
    #     browser.find_element(By.ID, "dialogDeleteBtn").click()
    #     time.sleep(3)

    #     #Validate User Deleted
    #     browser.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers")

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()