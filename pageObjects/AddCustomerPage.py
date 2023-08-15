from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
class AddCustomer:
    lnkCustomer_menu_xpath = "(//a[@href='#'])[7]"
    lnkCustomer_menu_item_xpath = "(//a[@href='/Admin/Customer/List'])"
    btn_AddNew_xpath = "(//a[@href='/Admin/Customer/Create'])"
    btn_PlusIcon_xpath = "(//i[@class='fa toggle-icon fa-plus'])"
    txtEmail_id = "Email"
    txtPassword_id = "Password"
    txtFirstname_id = "FirstName"
    txtLastName_id = "LastName"
    rdButtonMale_id = "Gender_Male"
    rdButtonFemale_xpath = "(//label[@for='Gender_Female'])"
    dateButton_id = "DateOfBirth"
    txtCompany_id = "Company"
    check_exempt_id = "IsTaxExempt"
    newSettler_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[1]"
    newSettler_option1_xpath = "(//option[@value='1'])[1]"
    newSettler_option2_xpath = "(//option[@value='2'])[1]"
    customer_xpath = "(//div[@role='listbox'])[2]"
    customer_Cancel_xpath = "(//span[@title='delete'])"
    customer_Administrators_xpath = "(//option[@value='1'])[2]"
    customer_Forum_xpath = "(//option[@value='2'])[2]"
    customer_Register_xpath = "(//option[@value='3'])"
    customer_guest_xpath = "(//option[@value='4'])"
    customer_vendors_xpath = "(//option[@value='5'])"
    vendor_id = "VendorId"
    vendor1_xpath = "(//option[@value='1'])[3]"
    vendor2_xpath = "(//option[@value='2'])[3]"
    admin_comment_id = "AdminComment"
    save_button_xpath = "(//button[@type='submit'])[2]"


    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menu_item_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btn_AddNew_xpath).click()

    def clickOnAddbtn(self):
        self.driver.find_element(By.XPATH, self.btn_PlusIcon_xpath).click()

    def SetEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def SetPassword(self, Password):
        self.driver.find_element(By.ID, self.txtPassword_id).send_keys(Password)

    def SetFirstName(self, fname):
        self.driver.find_element(By.ID, self.txtFirstname_id).send_keys(fname)

    def SetLastName(self,lname):
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lname)

    def SetGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdButtonMale_id).click()

        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.rdButtonFemale_xpath).click()

        else:
            self.driver.find_element(By.ID, self.rdButtonMale_id).click()

    def SetDOB(self, dob):
        self.driver.find_element(By.ID, self.dateButton_id).send_keys(dob)

    def SetCompanyNAME(self, CompanyName):
        self.driver.find_element(By.ID, self.txtCompany_id).send_keys(CompanyName)

    def clickTax(self):
        self.driver.find_element(By.ID, self.check_exempt_id).click()

    # def SetCustomerRoles(self, role):
    #     self.driver.find_element(By.XPATH, self.customer_xpath).click()
    #     time.sleep(3)
    #
    #     if role == 'Registered':
    #         self.listitem = self.driver.find_element(By.XPATH, self.customer_Register_xpath)
    #
    #     elif role == 'Administrators':
    #         self.listitem = self.driver.find_element(By.XPATH, self.customer_Administrators_xpath)
    #
    #     elif role == 'Guests':
    #         self.driver.find_element(By.XPATH, self.customer_Cancel_xpath).click()
    #         self.listitem = self.driver.find_element(By.XPATH, self.customer_guest_xpath)
    #
    #     elif role == 'Forum Moderators':
    #         self.listitem = self.driver.find_element(By.XPATH, self.customer_Forum_xpath)
    #
    #     elif role == 'Vendors':
    #         self.listitem = self.driver.find_element(By.XPATH, self.customer_vendors_xpath)
    #
    #     else:
    #         self.driver.find_element(By.XPATH, self.customer_Administrators_xpath)
    #
    #     time.sleep(3)
    #     self.driver.execute_script("arguments[0].click;", self.listitem)

    def SetManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.ID, self.vendor_id))


        drp.select_by_visible_text(value)

    def SetAdminContent(self, Admin):
        self.driver.find_element(By.ID, self.admin_comment_id).send_keys(Admin)
        # self.driver.execute_script(("arguments[0].scrollIntoView();", self.admin_comment_id))
        time.sleep(3)


    def ClickSaveBtn(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()












