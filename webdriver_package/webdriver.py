from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

browser="chrome"
if browser=='chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browser=='firefox':
    driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browser=='opera':
    driver=webdriver.Opera(executable_path=OperaDriverManager().install())



time.sleep(5)
driver.maximize_window()
driver.get('https://reactquiztype.herokuapp.com/')
print(driver.title)

#css-selector for multiple classes

# driver.find_element(By.CSS_SELECTOR,"button[class*='waves-light']").click()





# xpath with text
# time.sleep(5)
# driver.find_element(By.XPATH,"//button[text()='Submit']").click()



#name
driver.find_element(By.NAME,'firstname').send_keys('Darshan')

time.sleep(2)
driver.find_element(By.XPATH,"//input[@placeholder='Lastname']").send_keys('Mesta')
time.sleep(2)
driver.find_element(By.NAME,'email').send_keys('darshanmesta33@gmail.com')
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='row'][4]/div/input").send_keys('DarshanKA47@')
time.sleep(2)
# print(driver.find_element_by_partial_link_text('Already').text)
# time.sleep(2)
# driver.find_element_by_link_text('Already Have an Account').click()
# xpath for multiple classes
time.sleep(3)
driver.find_element(By.XPATH,"//button[contains(@class,'waves-light')]").click()
time.sleep(5)
print(driver.find_element(By.CLASS_NAME,'toast').text)

# print(driver.find_elements(By.TAG_NAME,'a'))

time.sleep(5)
print(driver.current_url)
#class selector
# time.sleep(2)
# print(driver.find_element(By.CLASS_NAME,'toast').text)




# ##id locator
# driver.find_element(By.NAME,'firstname').send_keys('Darshan')
# time.sleep(2)
# driver.find_element(By.ID,'pass-show').send_keys('DarshanKA47@')


time.sleep(10)

