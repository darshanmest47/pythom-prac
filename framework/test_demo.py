from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from framework.MainClass import MainClass
from framework.Pom.Shop import Shop


class TestDemo(MainClass):
    shop=""
    checkouts=""
    checkfinal=""
    main=MainClass()
    logs=main.loggerFunc()
    def test_final(self):
        self.driver.get('https://rahulshettyacademy.com/angularpractice/')

        TestDemo.shop = Shop(self.driver)
        time.sleep(3)

    def test_products(self):
        products=TestDemo.shop.click_Shop()

        TestDemo.checkouts=products.productsfind()
        print(TestDemo.checkouts)
        TestDemo.logs.info(TestDemo.checkouts)






    def test_checkout(self):
        print('Hello')
        TestDemo.checkouts.inccount()
        time.sleep(3)
        TestDemo.checkouts.checktotals()

        TestDemo.checkfinal=TestDemo.checkouts.clickCheckout()

    def test_checkoutfinal(self):
        print(TestDemo.checkfinal)
        TestDemo.logs.info(TestDemo.checkfinal)
        TestDemo.checkfinal.enter_country()
        TestDemo.checkfinal.checkbox()
        TestDemo.checkfinal.purchase()
        TestDemo.checkfinal.checkSuccess()










