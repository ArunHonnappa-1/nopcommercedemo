import pytest
from selenium import webdriver
from pageObjects.Loginpage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


import time

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def testhomepageTitle(self):

        self.logger.info("**** Test_001_Login*****")

        self.driver = webdriver.Chrome()

        self.driver.get(self.baseURL)
        act_title = self.driver.title
        time.sleep(3)
        print("act_title",act_title)
        # self.driver.close()

        if act_title == "Your store. Login":
            assert True
            self.logger.info("*** Title***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"testhomepageTitle.png")
            assert False
            self.logger.info("***Title1*****")

        self.driver.close()

    @pytest.mark.regression
    def test_login(self):
        self.logger.info("****test_login*****")
        self.driver = webdriver.Chrome()

        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()

        actual = self.driver.title
        # self.driver.close()

        if actual == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***login title****")
        else:
            self.logger.info("****login title of the page****")
            assert False
            # self.logger.info("****login title of the page****")

        self.driver.close()






