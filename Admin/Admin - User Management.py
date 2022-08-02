import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class AdminTest(unittest.TestCase):
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_redirect_page_to_user_management_sucsess(self):
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

        #Redirect_user_management
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

        #Validate
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers"
        self.assertEqual(expected_current_url, browser.current_url)

    def test_b_system_search_user_success(self):
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

        #NEGATIVE CASE
    def test_c_system_search_user_failed(self):
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

        #Redirect User Management
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

        #Search User
        browser.find_element(By.NAME, "searchSystemUser[userName]").send_keys("@Dmin")
        time.sleep(1)
        browser.find_element(By.NAME, "_search").click()
        time.sleep(3)

        #Validate Element
        search_result = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td").text
        self.assertEqual(search_result, 'No Records Found')

        #POSITIVE CASE
    def test_d_reset_search_success(self):
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

        #Redirect User Management
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

        #Search User
        browser.find_element(By.NAME, "searchSystemUser[userName]").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.NAME, "_search").click()
        time.sleep(3)
      
        #Reset Search User
        browser.find_element(By.NAME, "_reset").click()
        time.sleep(3)

        # Validate Reset Search
        all_user = browser.find_element(By.NAME,"frmList_ohrmListComponent").text
        
        #List All User
        self.assertEqual(all_user, 'resultTable')

        #Positive CASE
    def test_e_add_user_success(self):
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

        #Redirect User Management
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

        #Add User
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[employeeName][empName]").send_keys("Admin A")
        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[userName]").send_keys("tester3")
        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[password]").send_keys("tester123")
        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[confirmPassword]").send_keys("tester123")
        time.sleep(1)
        browser.find_element(By.NAME, "btnSave").click()
        time.sleep(3)

    #NEGATIVE CASE
    def test_f_add_user_failed_employee_does_not_exist(self):
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

        #Redirect User Management
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

        #Add User
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[employeeName][empName]").send_keys("Admin @")
        time.sleep(1)
        
        #Validation Error
        validation_error = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[2]/span").text
        self.assertEqual(validation_error, "Employee does not exist")
        time.sleep(2)

    #NEGATIVE CASE
    def test_g_add_user_failed_less_than_5_char_username(self):
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

        #Redirect User Management
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

        #Add User
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[userName]").send_keys("A")
        time.sleep(1)
        
        #Validation Error
        validation_error = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[3]/span").text
        self.assertEqual(validation_error, "Should have at least 5 characters")
        time.sleep(2)

    #NEGATIVE CASE
    def test_h_add_user_failed_less_than_8_char_pswd(self):
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

        #Redirect User Management
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

        #Add User
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[password]").send_keys("A")
        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[confirmPassword]").send_keys("A")
        time.sleep(1)
        
        #Validation Error
        validation_error = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[6]/span").text
        self.assertEqual(validation_error, "Should have at least 8 characters")
        time.sleep(2)

    def test_i_add_user_failed_null_input(self):
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

        #Redirect User Management
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

        #Add User
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)
        
        ddelement = Select(browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/select"))
        ddelement.select_by_value('1')

        browser.find_element(By.NAME, "systemUser[employeeName][empName]").send_keys("@")
        time.sleep(1)

        #Validation Employee Name
        validation_employee = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[2]/span").text
        self.assertEqual(validation_employee, 'Employee does not exist')
        

        browser.find_element(By.NAME, "systemUser[userName]").send_keys("^sai")
        time.sleep(1)

        #Validation Username
        validation_username = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[3]/span").text
        self.assertEqual(validation_username, 'Should have at least 5 characters')
        
        ddelement = Select(browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[4]/select"))
        ddelement.select_by_value('1')
        
        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[password]").send_keys("asdasdniijijijijij")

        #Validation Password
        validation_password = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[6]/span").text
        self.assertEqual(validation_password, 'Should have at least 8 characters')

        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[confirmPassword]").send_keys("asdasdniijijijijij")
        time.sleep(1)

        browser.find_element(By.NAME, "btnSave").click()
        time.sleep(3)

    def test_j_delete_user_success(self):
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

        #Redirect User Management
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

        #Search User
        browser.find_element(By.NAME, "searchSystemUser[userName]").send_keys("unchunch2")
        time.sleep(1)
        browser.find_element(By.NAME, "_search").click()
        time.sleep(3)

        #Delete User
        browser.find_element(By.NAME, "chkSelectRow[]").click()
        time.sleep(1)
        browser.find_element(By.NAME, "btnDelete").click()
        time.sleep(1)
        browser.find_element(By.ID, "dialogDeleteBtn").click()
        time.sleep(3)

        #Validate User Deleted
        browser.refresh()
        time.sleep(5)
        browser.find_element(By.NAME, "searchSystemUser[userName]").send_keys("unchunch2")
        time.sleep(1)
        browser.find_element(By.NAME, "_search").click()
        time.sleep(3)
        check_user = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td").text
        self.assertEqual(check_user, 'No Records Found')

    def test_k_pagination_success(self):
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

        #Redirect User Management
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

        #Pagination
        browser.find_element(By.LINK_TEXT, "Next").click()
        time.sleep(1)
        browser.find_element(By.LINK_TEXT, "First").click()
        time.sleep(2)
        browser.find_element(By.LINK_TEXT, "Previous").click()
        time.sleep(1)
        browser.find_element(By.LINK_TEXT, "Last").click()
        time.sleep(1)


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()