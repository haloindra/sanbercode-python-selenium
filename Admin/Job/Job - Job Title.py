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

    def test_b_add_job_success(self):
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

        #Add Job Titles
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME, "jobTitle[jobTitle]").send_keys("Kang Rumput3")
        time.sleep(1)
        browser.find_element(By.NAME, "jobTitle[jobDescription]").send_keys("Sukanya bebersih rumput, bebersih taman, siramin tanaman, pokoknya bersih pangkal kaya1")
        time.sleep(1)
        browser.find_element(By.NAME, "jobTitle[note]").send_keys("ini perlu buat memperindah taman dan kebun1")
        time.sleep(1)
        browser.find_element(By.NAME, "btnSave").click()
        time.sleep(1)

    def test_c_delete_job_title_success(self):
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

        actions = ActionChains(browser)

        #Click Job Title
        actions.move_to_element(job).move_to_element(job_title).click().perform()
        time.sleep(3)
        
        #Validate
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewJobTitleList"
        self.assertEqual(expected_current_url, browser.current_url)

        #Delete Job Title
        browser.find_element(By.NAME, "chkSelectRow[]").click()
        time.sleep(1)
        browser.find_element(By.NAME, "btnDelete").click()
        time.sleep(1)
        browser.find_element(By.ID, "dialogDeleteBtn").click()
        time.sleep(1)
       
    def test_d_add_job_title_failed_many_char(self):
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

        actions = ActionChains(browser)

        #Click Job Title
        actions.move_to_element(job).move_to_element(job_title).click().perform()
        time.sleep(3)
        
        #Validate
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewJobTitleList"
        self.assertEqual(expected_current_url, browser.current_url)

        #Add Job Title Fail
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)

        browser.find_element(By.NAME, "jobTitle[jobTitle]").send_keys(" ")
        time.sleep(1)

        browser.find_element(By.NAME, "jobTitle[jobDescription]").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis viverra turpis sit amet dui iaculis, nec imperdiet metus gravida. Suspendisse eget felis ante. Phasellus commodo mauris ipsum. Fusce malesuada rutrum ipsum consectetur rhoncus. Phasellus lacinia felis ac eros consectetur consequat. Morbi egestas pellentesque mi, sed semper massa venenatis et. Ut accumsan elit et tincidunt eleifend. Pellentesque eu aliquet ex, at suscipit dolor. Nam odio velit, iaculis id mauris eget, elementum pellentesque erat.")
        time.sleep(1)

        browser.find_element(By.NAME, "jobTitle[note]").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis viverra turpis sit amet dui iaculis, nec imperdiet metus gravida. Suspendisse eget felis ante. Phasellus commodo mauris ipsum. Fusce malesuada rutrum ipsum consectetur rhoncus. Phasellus lacinia felis ac eros consectetur consequat. Morbi egestas pellentesque mi, sed semper massa venenatis et. Ut accumsan elit et tincidunt eleifend. Pellentesque eu aliquet ex, at suscipit dolor. Nam odio velit, iaculis id mauris eget, elementum pellentesque erat.")
        time.sleep(1)

        #Validation Input Job Title
        validation_job_title = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/span").text
        self.assertEqual(validation_job_title, 'Required')

        #Validation Input Job Description
        validation_job_desc = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[2]/span").text
        self.assertEqual(validation_job_desc, 'Should be less than 400 characters')

        #Validation Input Job Desc
        validation_job_note = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[3]/span").text
        self.assertEqual(validation_job_note, 'Should be less than 400 characters')

        browser.find_element(By.NAME, "btnSave").click()
        time.sleep(1)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()