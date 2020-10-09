import time

import pytest
from selenium.webdriver.support import expected_conditions as EC


from framework.MainClass import MainClass
from framework.Pom.Signpage import Signpage
from framework.Testdata import TestData


class Testsign(MainClass):
    sign=""
    main=MainClass()
    logs=main.loggerFunc()

    def test_main(self,getData):
            Testsign.sign = Signpage(self.driver)
            print('Hello')
            self.driver.get('https://rahulshettyacademy.com/angularpractice/')
            time.sleep(2)
            Testsign.sign.name_fill().send_keys(getData["name"])
            Testsign.logs.info(getData["name"])

            time.sleep(2)
            Testsign.sign.email_fill().send_keys(getData["email"])
            Testsign.logs.info(getData["email"])

            time.sleep(2)
            Testsign.sign.pass_fill().send_keys(getData["password"])
            Testsign.logs.info(getData["password"])

            Testsign.sign.check_fill().click()

            time.sleep(2)
            selele = Testsign.sign.select_fill()
            main = MainClass()
            main.signSelect(selele, getData["gender"])
            Testsign.logs.info(getData["gender"])

            Testsign.sign.student_fill().click()

            time.sleep(2)
            # Testsign.sign.bdy_fill().send_keys(getData["DOB"])
            # Testsign.logs.info(getData["DOB"])

            Testsign.sign.submit_click().click()
            main = MainClass()
            ele = Testsign.sign.verify_success()
            waits = main.waituntillpresent(self.driver)
            waits.until(EC.presence_of_element_located(ele))
            assert self.driver.find_element(*ele).text == 'Success!'
















    @pytest.fixture(params=TestData.testdata)
    def getData(self,request):
        return request.param


