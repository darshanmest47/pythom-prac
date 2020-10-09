from selenium.webdriver.common.by import By

from framework.Pom.Products import Products


class Shop:
    shop=(By.LINK_TEXT,"Shop")
    def __init__(self,driver):
        self.driver=driver

    def click_Shop(self):
        print('Hello')
        self.driver.find_element(*Shop.shop).click()
        products= Products(self.driver)
        return products
