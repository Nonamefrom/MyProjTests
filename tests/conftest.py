import pytest
from selenium import webdriver

from utils.env import Env
@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    web_driver = webdriver.Remote(
        command_executor=f"{Env().remote_webdriver_url}",
        options=options
    )
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()
