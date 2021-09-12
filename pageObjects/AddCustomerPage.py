
from time import sleep
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # Locators
    lnkCustomers_menu_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]/p[1]"
    lnkCustomers_menuitem_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/p[1]"
    btnAddnew_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_xpath = "//input[@id='Gender_Male']"
    rdFemaleGender_xpath = "//input[@id='Gender_Female']"
    txtDOB_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    cbIsTaxExempt_xpath = "//input[@id='IsTaxExempt']"
    drpNewsletter_xpath = "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div[1]"
    txtCustomerRoles_xpath = "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]" # "//option[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]" # "//option[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]" # "//option[contains(text(),'Guests')]"
    lstitemVendor_xpath = "//li[contains(text(),'Vendors')]" # "//option[contains(text(),'Vendors')]"
    lstitemForumModerators_xpath = "//li[contains(text(),'Forum Moderators')]" # "//option[contains(text(),'Forum Moderators')]"
    drpManagerOfVendor_xpath = "//select[@id='VendorId']"
    cbActive_xpath = "//input[@id='Active']"
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        sleep(3)
        if role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role == "Guests":
            # Here user can be Registered or Guest, only one
            sleep(3)
            #self.driver.find_element_by_xpath("//ul[@id='SelectedCustomerRoleIds_taglist']").click()
            #self.driver.find_element_by_xpath("//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]").clear()
            self.driver.find_element_by_xpath("//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
            sleep(3)
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        elif role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendor_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpManagerOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element_by_xpath(self.rdMaleGender_xpath).click()
        elif gender == "Female":
            self.driver.find_element_by_xpath(self.rdFemaleGender_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.rdMaleGender_xpath).click()

    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def setDOB(self, dob):
        self.driver.find_element_by_xpath(self.txtDOB_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txtAdminComment_xpath).send_keys(content)

    def clickOnsave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()