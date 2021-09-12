import pytest
from time import sleep

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen

class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = logGen.log_gen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("********** Test_004_SearchCustomerByEmail **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successful **********")

        self.logger.info("**********  Starting Search Customer By Email **********")
        self.addcust = AddCustomer(self.driver)
        sleep(3)
        self.addcust.clickOnCustomerMenu()
        sleep(3)
        self.addcust.clickOnCustomerMenuItem()
        sleep(3)

        self.logger.info("**********  Starting Customer By Email **********")
        searchcust = SearchCustomer(self.driver)
        sleep(5)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        sleep(3)
        searchcust.clickSearch()
        sleep(5)
        status  = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("********** Test_004_SearchCustomerByEmail Finished **********")
        self.driver.close()
