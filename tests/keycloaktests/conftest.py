import pytest
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    web_driver = webdriver.Remote(
        command_executor="http://chrome:4444/wd/hub",
        options=options
    )
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()
