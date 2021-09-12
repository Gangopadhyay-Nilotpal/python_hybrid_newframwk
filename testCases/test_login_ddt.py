
import pytest
from selenium import webdriver
import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from utilities import ExcelUtils

class Test_002_DDT_Login:

    # class variables
    path = ReadConfig.getExcelFilePath()
    baseURL = ReadConfig.getApplicationURL()
    pagetitle_afterlogin = ReadConfig.getpageTitleAftLogin()
    # Data Driven Testing - Data will come from Excel file

    log_er = logGen.log_gen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.log_er.info("********** Test_002_DDT_Login **********")
        self.log_er.info("********** Verifying Login DDT Test - Started **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("No. of Rows in Excel : ", self.rows)
        list_status = []

        for r in range(2, self.rows + 1):
            self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.passwd = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exptval = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.passwd)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title

            if act_title == self.pagetitle_afterlogin:
                if self.exptval == "Pass":
                    self.log_er.info("********** Verifying Login DDT Test - Passed **********")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exptval == "Fail":
                    self.log_er.info("********** Verifying Login DDT Test - Failed **********")
                    self.lp.clickLogout()
                    list_status.append("Fail")
            elif act_title != self.pagetitle_afterlogin:
                if self.exptval == "Pass":
                    self.log_er.info("********** Verifying Login DDT Test - Failed **********")
                    list_status.append("Fail")
                elif self.exptval == "Fail":
                    self.log_er.info("********** Verifying Login DDT Test - Passed **********")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.log_er.info("********** Final - Login DDT Test - Passed **********")
            self.driver.close()
            assert True
        else:
            self.log_er.info("********** Final - Login DDT Test - Failed **********")
            self.driver.close()
            assert False

        self.log_er.info("********** End of Login DDT Test **********")
        self.log_er.info("********** Completed Test_002_DDT_Login **********")
