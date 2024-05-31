import importlib
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.env import Env


fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser)

    return fixture


def pytest_addoption(parser):
    # НЕ ПУШИТЬ С ЗАКОММЕНТИРОВАННОЙ СТРОКОЙ ГДЕ DEFAULT=CHROME_REMOTE И РАСКОММЕНТИРОВАННОЙ ГДЕ CHROME
    parser.addoption("--browser", action="store", default="chrome_remote",
                     help='example: chrome_remote for docker, chrome for pc browser with venv usage')
    # parser.addoption("--browser", action="store", default="chrome",
    #                  help='example: chrome_remote for docker, chrome for pc browser with venv usage')
    # parser.addoption("--stage", action="store", default='dev', help="dev for dev, stage for stage")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("suit_"):  # "suit_filename" for test data on models (suit_notification_valid as example)
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x.number) for x in testdata])
        if fixture.startswith("data_"):  # "data_filename" for test data on tuples (data_cp_user as example)
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x[1]) for x in testdata])


# работа с файлами .py в папке data
# аналог 'from data.{имя файла}.py import testdata' для каждого файла с тестами
def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


class Application:

    def __init__(self, browser):
        if browser == "chrome_remote":
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Remote(command_executor=f"{Env().remote_webdriver_url}",
                                           options=options)
            self.driver.maximize_window()
        elif browser == "chrome" or browser == "cd":
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            # self.driver.set_window_rect(width=1280, height=720)
            # try:
            #     self.driver = webdriver.Chrome()
            # except:
            #     service = Service(executable_path=f"{Env().local_chrome_driver}")
            #     # service = Service(executable_path='C:\PycharmProjects\webdrivers\chromedriver.exe')
            #     self.driver = webdriver.Chrome(service=service)

        elif browser == "firefox" or browser == "ff":
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
        elif browser == "ie":
            self.driver = webdriver.Ie()
            self.driver.maximize_window()

        else:
            raise ValueError("Unrecognized browser %s" % browser)

    def is_valid(self):
        try:
            # noinspection PyStatementEffect
            self.driver.current_url
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()
