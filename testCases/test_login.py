
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    pagetitle_beforelogin = ReadConfig.getpageTitleBefLogin()
    pagetitle_afterlogin = ReadConfig.getpageTitleAftLogin()

    log_er = logGen.log_gen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.log_er.info("********** Test_001_Login **********")
        self.log_er.info("********** Verifying test_homePageTitle TC **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == self.pagetitle_beforelogin :
            self.driver.close()
            self.log_er.info("********** test_homePageTitle TC - Passed **********")
            self.log_er.info("********** execution test_homePageTitle completed **********")
            assert True
        else :
            self.driver.save_screenshot(".\\_Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.log_er.info("********** test_homePageTitle TC - Failed **********")
            self.log_er.info("********** execution test_homePageTitle completed **********")
            assert False

    @pytest.mark.sanity
    def test_Login(self, setup):
        self.log_er.info("********** test_Login TC **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == self.pagetitle_afterlogin :
            self.lp.clickLogout()
            self.driver.close()
            self.log_er.info("********** test_Login TC - Passed **********")
            self.log_er.info("********** execution test_Login completed **********")
            assert True
        else :
            self.driver.save_screenshot(".\\_Screenshots\\" + "test_Login.png")
            #self.lp.clickLogout()
            self.driver.close()
            self.log_er.info("********** test_Login TC - Failed **********")
            self.log_er.info("********** execution test_Login completed **********")
            assert False
