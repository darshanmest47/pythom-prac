import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
         "--browser_name", default='chrome', action="store"
     )

@pytest.fixture(scope="class")
def setup(request):
    browsername=request.config.getoption("--browser_name")
    if browsername=='chrome':
        options=webdriver.ChromeOptions()
        options.add_argument('--start_maximized')

        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        request.cls.driver=driver
        yield
        driver.close()


    elif browsername=="firefox":
        print('firefox')
        options=webdriver.FirefoxOptions()
        options.add_argument('--start_maximized')

        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()

        request.cls.driver = driver
        yield
        driver.close()
    elif browsername=="IE":
        print('Hello')
        options=webdriver.IeOptions()
        options.add_argument('--start_maximized')
        driver=webdriver.Ie(executable_path=IEDriverManager().install(),options=options)
        request.cls.driver=driver
        yield
        driver.close()

    else:
        print('Error')
