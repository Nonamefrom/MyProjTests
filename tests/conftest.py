import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--headless")
    driver = webdriver.Remote(
        command_executor="http://chrome:4444/wd/hub",
        options=options
    )
    driver.maximize_window()
    yield driver
    driver.quit()
