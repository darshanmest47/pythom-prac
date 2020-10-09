import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Checkfinal:
    country=(By.CSS_SELECTOR,"#country")
    country_list=(By.XPATH,"//div[@class='suggestions']")
    country_name=(By.XPATH,"//div[@class='suggestions']/ul/li/a[text()='India']")
    check_box=(By.XPATH,"//label[@for='checkbox2']")
    purchase_item=(By.XPATH,"//input[@value='Purchase']")
    success_msg=(By.XPATH,"//div[contains(@class,'alert-success')]/strong")
    dialog_box=(By.XPATH,"//div[contains(@class,'nsm-dialog-animation-fade nsm-dialog nsm-dialog-open')]")

    close_x=(By.XPATH,"//div[contains(@class,'nsm-dialog-animation-fade nsm-dialog nsm-dialog-open')]/button[@aria-label='Close']")

    def __init__(self,driver):
        self.driver=driver

    def enter_country(self):
        self.driver.find_element(*Checkfinal.country).send_keys('Ind')

        waits=WebDriverWait(self.driver,40)
        waits.until(EC.presence_of_element_located(Checkfinal.country_list))
        #waits.until(EC.element_to_be_clickable(Checkfinal.country_name))
        self.driver.find_element(*Checkfinal.country_name).click()


        # self.driver.find_element(*Checkfinal.country_name).click()
    def checkbox(self):
        time.sleep(3)
        self.driver.find_element(*Checkfinal.check_box).click()
        try:
            if Checkfinal.dialog_box:
                waitcondition = WebDriverWait(self.driver, 20)
                waitcondition.until(EC.presence_of_element_located(Checkfinal.dialog_box))
                time.sleep(3)
                self.driver.find_element(*Checkfinal.close_x).click()
        except Exception as e:
            print(e)
        finally:
            pass










    def purchase(self):
        time.sleep(2)
        self.driver.find_element(*Checkfinal.purchase_item).click()














    def checkSuccess(self):
        time.sleep(2)
        # waits=WebDriverWait(self.driver,20)
        # waits.until(EC.presence_of_element_located(Checkfinal.success_msg))
        try:
            print(self.driver.find_element(Checkfinal.success_msg))
        except Exception as e:
            print(e)
        finally:
            text=self.driver.find_element(*Checkfinal.success_msg).text
            assert text=="Success!"



        # assert txt == 'Success!'








