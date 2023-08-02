import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    chrome_version = "114.0.5735.90"
    service = ChromeService(ChromeDriverManager(version=chrome_version).install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
