import time

from selenium.webdriver.common.by import By


class Signpage:
    def __init__(self,driver):
        self.driver=driver

    name_field=(By.XPATH,"//input[@minlength='2']")
    email_field=(By.XPATH,"//input[@name='email']")
    password_field=(By.XPATH,"//input[@type='password']")
    checkbox_field=(By.XPATH,"//input[@type='checkbox']")
    select_field=(By.XPATH,"//select[@class='form-control']")
    student_field=(By.XPATH,"//input[@value='option1']")
    bdy_field=(By.XPATH,"//input[@name='bday']")
    submit_field=(By.XPATH,"//input[@value='Submit']")
    success_txt=(By.XPATH,"//strong[contains(text(),'Succ')]")


    def name_fill(self):

        return self.driver.find_element(*Signpage.name_field)
    def email_fill(self):
        return self.driver.find_element(*Signpage.email_field)

    def pass_fill(self):
        return self.driver.find_element(*Signpage.password_field)

    def check_fill(self):
        return self.driver.find_element(*Signpage.checkbox_field)


    def select_fill(self):
        return self.driver.find_element(*Signpage.select_field)

    def student_fill(self):
        return self.driver.find_element(*Signpage.student_field)

    # def bdy_fill(self):
    #     return self.driver.find_element(*Signpage.bdy_field)

    def submit_click(self):
        return self.driver.find_element(*Signpage.submit_field)

    def verify_success(self):
        return Signpage.success_txt
