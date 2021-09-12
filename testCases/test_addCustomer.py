import pytest
from time import sleep

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = logGen.log_gen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("********** Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successful **********")

        self.logger.info("********** Starting Add Customer Test **********")
        self.addcust = AddCustomer(self.driver)
        sleep(3)
        self.addcust.clickOnCustomerMenu()
        sleep(3)
        self.addcust.clickOnCustomerMenuItem()
        sleep(3)
        self.addcust.clickOnAddNew()

        self.logger.info("********** Providing Customer Info **********")
        self.email = random_generator() + "@gmail.com"
        sleep(3)
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Pavan")
        self.addcust.setLastName("Kumar")
        self.addcust.setGender("Male")
        self.addcust.setDOB("1/03/1975")
        self.addcust.setCompanyName("busyQA")
        #self.addcust.setCustomerRoles("Guest")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setAdminContent("This is for Testing ...")
        self.addcust.clickOnsave()

        self.logger.info("********** Saving Customer Info **********")
        self.logger.info("********** Add Customer validation started **********")

        self.msg = self.driver.find_element_by_tag_name("body").text
        #print (self.msg)

        if "customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("********** Add Customer Test Passed **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("********** Add Customer Test Failed **********")
            assert True == False

        self.driver.close()
        self.logger.info("********** End of Test_003_AddCustomer Test **********")


def random_generator(size = 8, chars = string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))
