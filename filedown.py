import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

browsername="firefox"

if browsername=="chrome":
    options=webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--ignore-certificate-errors')
    options.headless=True


    options.add_experimental_option("prefs",{"download.default_directory","E:\\filedowns"})

    driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)


elif browsername=='firefox':
    options=webdriver.FirefoxOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--ignore-certificate-errors')
    options.headless=True
    fp=webdriver.FirefoxProfile()
    fp.set_preference("browser.download.manager.showWhenStarting",False)
    fp.set_preference("browser.download.manager.showAlertOnComplete",False)
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf")
    fp.set_preference("browser.download.dir","E:\filedowns")
    fp.set_preference("browser.download.folderList",2)
    driver=webdriver.Firefox(executable_path=GeckoDriverManager().install(),firefox_profile=fp,options=options)
else:
    print('Error')

driver.get('http://demo.automationtesting.in/FileDownload.html')
driver.find_element(By.XPATH,"//textarea[@id='textbox']").send_keys("Darshan")
waits=WebDriverWait(driver,10)
waits.until(expected_conditions.element_to_be_clickable((By.XPATH,"//button[@id='createTxt']")))

driver.find_element(By.XPATH,"//button[@id='createTxt']").click()
time.sleep(4)
driver.find_element(By.XPATH,"//a[@download='info.txt']").click()

driver.find_element(By.XPATH,"//textarea[@id='pdfbox']").send_keys('Darshan Mesta')
waits.until(expected_conditions.element_to_be_clickable((By.XPATH,"//button[@id='createPdf']")))

driver.find_element(By.XPATH,"//button[@id='createPdf']").click()
time.sleep(4)
driver.find_element(By.XPATH,"//a[@download='info.pdf']").click()

S=lambda X:driver.execute_script("return document.body.parentNode.scroll"+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element(By.TAG_NAME,'body').screenshot('filedownfull.png')

time.sleep(15)
driver.quit()