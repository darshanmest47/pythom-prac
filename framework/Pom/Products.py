from selenium.webdriver.common.by import By
import time

from framework.MainClass import MainClass
from framework.Pom.Checkout import Checkout


class Products:
    main=MainClass()
    logs=main.loggerFunc()
    products=(By.XPATH,"//h4[@class='card-title']/a")
    checkout=(By.XPATH,"//a[contains(text(),'Check')]")
    def __init__(self,driver):
        self.driver=driver

    def productsfind(self):
        productlist=self.driver.find_elements(*Products.products)
        # return (productlist,Products.products)
        for ele in productlist:
            print(ele.text)
            Products.logs.info(ele.text)
            if ele.text=="Nokia Edge":

                ele.find_element(By.XPATH,"parent::h4/parent::div/following-sibling::div/button").click()
                break
        time.sleep(4)
        self.driver.find_element(*Products.checkout).click()

        checkouts=Checkout(self.driver)
        return checkouts

