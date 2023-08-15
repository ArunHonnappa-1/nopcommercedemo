import pytest
import time
from selenium import webdriver
from pageObjects.Loginpage import Loginpage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_addcustomer(self):
        self.logger.info("****test_login*****")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()



        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)

        self.addCustomer = AddCustomer(self.driver)
        self.addCustomer.clickOnCustomerMenu()
        self.addCustomer.clickOnCustomerMenuItem()
        self.addCustomer.clickOnAddnew()
        time.sleep(3)

        self.email = self.random_generator() + "@gmail.com"
        self.addCustomer.SetEmail(self.email)
        time.sleep(3)

        # self.addCustomer.SetEmail("xyz@gmail.com")
        time.sleep(3)
        self.addCustomer.SetPassword("Test123")
        self.addCustomer.SetFirstName("Arun")
        self.addCustomer.SetLastName("Honnappa1")
        self.addCustomer.SetGender("Male")
        self.addCustomer.SetDOB("10/08/2023")
        self.addCustomer.SetCompanyNAME("QA")
        self.addCustomer.clickTax()
        # self.addcust.SetCustomerRoles("Guests")
        self.addCustomer.SetManagerOfVendor("Vendor 2")
        time.sleep(6)
        self.addCustomer.SetAdminContent("Test the following feature")
        time.sleep(10)
        self.addCustomer.ClickSaveBtn()
        time.sleep(3)

        self.message = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.message)




        # if 'Customer has been added succesfully' in self.message:
        #     assert True == True
        #     # assert True
        #
        # else:
        #     assert True == False
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer.png")
            # assert False

        # self.driver.close()
    #For random emai genarate with combination of caharacter and number
    # def random_generator(size=4, chars=string.ascii_lowercase + string.digits):
    #     return ''.join(random.choice(chars) for _ in range(8))
    #For random email geneartw with character
    def random_generator(size=4, chars=string.ascii_lowercase ):
        return ''.join(random.choice(chars) for x in range(8))









