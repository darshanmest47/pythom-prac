
from selenium.webdriver.common.by import By
import time

from framework.Pom.Checkfinal import Checkfinal


class Checkout:
    qty=(By.XPATH,"//input[contains(@id,'InputEmail')]")
    total1=(By.XPATH,"//span[contains(@class,'glyphicon-remove')]/parent::button/parent::td/parent::tr/td[4]/strong")
    total2=(By.XPATH,"//td[@class='text-right']/h3")
    success=(By.XPATH,"//button[contains(@class,'btn-success')]")
    def __init__(self,driver):
        self.driver=driver

    def inccount(self):
        ele1=self.driver.find_element(*Checkout.qty)


        self.driver.find_element(*Checkout.qty).clear()


        self.driver.find_element(*Checkout.qty).send_keys(0)

        self.driver.find_element(*Checkout.qty).send_keys(2)

    def checktotals(self):
        sum1=self.driver.find_element(*Checkout.total1)
        sum2=self.driver.find_element(*Checkout.total2)
        assert sum1.text==sum2.text

    def clickCheckout(self):

        self.driver.find_element(*Checkout.success).click()

        checkfinal=Checkfinal(self.driver)
        return checkfinal


