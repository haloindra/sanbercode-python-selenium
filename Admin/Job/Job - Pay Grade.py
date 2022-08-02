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

    def test_b_add_pay_grade_success(self):
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

        #Add Pay Grade
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME, "payGrade[name]").send_keys("Grade 96")
        time.sleep(1)
        browser.find_element(By.NAME, "btnSave").click()
        time.sleep(3)

    def test_c_assign_currency_success(self):
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

        #Add Pay Grade
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME, "payGrade[name]").send_keys("Grade 95")
        time.sleep(1)
        browser.find_element(By.NAME, "btnSave").click()
        time.sleep(3)

        #Add Assign Currency
        browser.find_element(By.ID, "btnAddCurrency").click()
        time.sleep(1)
        browser.find_element(By.NAME, "payGradeCurrency[currencyName]").send_keys("IDR - Indonesian Rupiah")
        time.sleep(1)
        browser.find_element(By.NAME, "payGradeCurrency[minSalary]").send_keys("2000000")
        time.sleep(1)
        browser.find_element(By.NAME, "payGradeCurrency[maxSalary]").send_keys("2500000")
        time.sleep(1)
        browser.find_element(By.NAME, "btnSaveCurrency").click()
        time.sleep(3)

    def test_d_delete_pay_grade_success(self):
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

        #Delete Paygrade
        browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/div[2]/form/div[4]/table/tbody/tr[7]/td[1]/input").click()
        time.sleep(1)
        browser.find_element(By.NAME, "btnDelete").click()
        time.sleep(1)
        browser.find_element(By.ID, "dialogDeleteBtn").click()
        time.sleep(1)

    def test_e_add_paygrade_failed(self):
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

        #Add Pay Grade
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME, "payGrade[name]").send_keys("   ")
        time.sleep(1)
        browser.find_element(By.NAME, "btnSave").click()
        time.sleep(3)

        #Validate
        validation_pay_grade = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/span").text
        self.assertEqual(validation_pay_grade, 'Required')

    def test_f_add_salary_failed(self):
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

        #Add Pay Grade
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME, "payGrade[name]").send_keys("grade 87")
        time.sleep(1)
        browser.find_element(By.NAME, "btnSave").click()
        time.sleep(3)

        #Add Assign Currency
        browser.find_element(By.ID, "btnAddCurrency").click()
        time.sleep(1)
        browser.find_element(By.NAME, "payGradeCurrency[currencyName]").send_keys("abc")
        time.sleep(1)


        browser.find_element(By.NAME, "payGradeCurrency[minSalary]").send_keys("0")
        time.sleep(1)
        browser.find_element(By.NAME, "payGradeCurrency[maxSalary]").send_keys("1")
        time.sleep(1)
        browser.find_element(By.NAME, "btnSaveCurrency").click()
        time.sleep(3)

        #Validate Invalid
        invalid = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[1]/span[1]").text
        self.assertEqual(invalid, "Invalid")

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()