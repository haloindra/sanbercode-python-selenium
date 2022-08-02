import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class AdminTest(unittest.TestCase):
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # def test_a_redirect_page_to_job_cat(self):
    
    #     #Login
    #     browser = self.browser 
    #     browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login") 
    #     time.sleep(3)
    #     browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
    #     time.sleep(1)
    #     browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
    #     time.sleep(1)
    #     browser.find_element(By.NAME,"Submit").click() 
    #     time.sleep(1)

    #     browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/a").click()
    #     time.sleep(2)

    #     #Hover to Job Title
    #     job = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/a")
    #     job_title = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[1]/a")
    #     pay_grade = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[2]/a")
    #     employ_stat = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[3]/a")
    #     job_cat = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[4]/a")
    #     work_shift = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[5]/a")

    #     actions = ActionChains(browser)
        
    #     #Click Pay Grade
    #     actions.move_to_element(job).move_to_element(work_shift).click().perform()
    #     time.sleep(3)

    #     #Validate
    #     expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/workShift" 
    #     self.assertEqual(expected_current_url, browser.current_url)

    # def test_b_add_work_shifts_success(self):
    #     #Login
    #     browser = self.browser 
    #     browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login") 
    #     time.sleep(3)
    #     browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
    #     time.sleep(1)
    #     browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
    #     time.sleep(1)
    #     browser.find_element(By.NAME,"Submit").click() 
    #     time.sleep(1)

    #     browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/a").click()
    #     time.sleep(2)

    #     #Hover to Job Title
    #     job = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/a")
    #     job_title = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[1]/a")
    #     pay_grade = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[2]/a")
    #     employ_stat = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[3]/a")
    #     job_cat = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[4]/a")
    #     work_shift = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[5]/a")

    #     actions = ActionChains(browser)
        
    #     #Click Pay Grade
    #     actions.move_to_element(job).move_to_element(work_shift).click().perform()
    #     time.sleep(3)

    #     #Validate
    #     expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/workShift" 
    #     self.assertEqual(expected_current_url, browser.current_url)

    #     #Add Work Shifts
    #     browser.find_element(By.NAME, "btnAdd").click()
    #     time.sleep(1)
    #     browser.find_element(By.NAME, "workShift[name]").send_keys("Lembur2")
    #     time.sleep(1)
    #     sel = Select(browser.find_element(By.NAME, "workShift[workHours][from]"))
    #     sel.select_by_value("09:00")
    #     time.sleep(1)
    #     sel = Select(browser.find_element(By.NAME, "workShift[workHours][to]"))
    #     sel.select_by_value("20:00")
    #     time.sleep(1)
    #     sel = Select(browser.find_element(By.NAME, "workShift[availableEmp][]"))
    #     sel.select_by_value("77")
    #     time.sleep(1)
    #     browser.find_element(By.ID, "btnAssignEmployee").click()
    #     time.sleep(1)
    #     browser.find_element(By.NAME, "btnSave").click()
    #     time.sleep(3)

    # def test_c_add_work_shift_failed(self):
    #     #Login
    #     browser = self.browser 
    #     browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login") 
    #     time.sleep(3)
    #     browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
    #     time.sleep(1)
    #     browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
    #     time.sleep(1)
    #     browser.find_element(By.NAME,"Submit").click() 
    #     time.sleep(1)

    #     browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/a").click()
    #     time.sleep(2)

    #     #Hover to Job Title
    #     job = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/a")
    #     job_title = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[1]/a")
    #     pay_grade = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[2]/a")
    #     employ_stat = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[3]/a")
    #     job_cat = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[4]/a")
    #     work_shift = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[5]/a")

    #     actions = ActionChains(browser)
        
    #     #Click Pay Grade
    #     actions.move_to_element(job).move_to_element(work_shift).click().perform()
    #     time.sleep(3)

    #     #Validate
    #     expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/workShift" 
    #     self.assertEqual(expected_current_url, browser.current_url)

    #     #Add Work Shifts
    #     browser.find_element(By.NAME, "btnAdd").click()
    #     time.sleep(1)
    #     browser.find_element(By.NAME, "workShift[name]").send_keys("Lembur3")
    #     time.sleep(1)
    #     sel = Select(browser.find_element(By.NAME, "workShift[workHours][from]"))
    #     sel.select_by_value("23:00")
    #     time.sleep(1)

    #     #Validation Time From
    #     validation_time = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[2]/span").text
    #     self.assertEqual(validation_time, "From time should be less than To time")

    #     sel = Select(browser.find_element(By.NAME, "workShift[workHours][to]"))
    #     sel.select_by_value("12:00")
    #     time.sleep(1)

    #     sel = Select(browser.find_element(By.NAME, "workShift[availableEmp][]"))
    #     sel.select_by_value("77")
    #     time.sleep(1)
    #     browser.find_element(By.ID, "btnAssignEmployee").click()
    #     time.sleep(1)
    #     browser.find_element(By.NAME, "btnSave").click()
    #     time.sleep(3)

    def test_d_delete_work_shift_success(self):
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
        actions.move_to_element(job).move_to_element(work_shift).click().perform()
        time.sleep(3)

        #Validate
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/workShift" 
        self.assertEqual(expected_current_url, browser.current_url)

        #Delete Work Shift
        browser.find_element(By.NAME, "/html/body/div[1]/div[3]/div[2]/div/div[2]/form/div[4]/table/tbody/tr[1]/td[1]/input").click()
        time.sleep(1)
        browser.find_element(By.NAME, "btnDelete").click


    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()