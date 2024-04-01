import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.env import Env
import importlib

from steps.common_steps import CommonSteps
from steps.tables_steps import TablesSteps

from pages.keycloak.keycloack_auth_page import KeycloackAuthForm
from pages.control_panel.ui.topbar_cp_page import TopBarCpPage
from pages.control_panel.ui.sidebar_cp_page import SideBarCpPage
from pages.control_panel.options.all_options_page import AllOptionsCpPage
from pages.mailpit.mailpit_main import MailPitMain
from pages.service_booking.service_booking_mainpage import ServiceBookingMainPage
from pages.pwz.pwz_mainpage import PWZMainPage
from pages.employee_dashboard.emp_dash_mainpage import EmpDashMainPage
from pages.partner_cabinet.mim_page import MimAuthPage
from pages.partner_cabinet.partner_landing import PartnerLandingPage
from pages.partner_cabinet.partner_options_page import PartnerOptionsPage
from pages.partner_cabinet.ui.sidebar_cabinet_page import SideBarCabinetPage
from pages.partner_cabinet.ui.topbar_cabinet_page import TopBarCabinetPage
from pages.partner_cabinet.profile_page import ProfilePageCabinet
from pages.partner_cabinet.b2b_empoyee_page import B2bEmployeePageCab

CP_URL = f"{Env().cp_url}/auth/login"
SB_URL = f"{Env().sb_url}/"
PWZ_URL = f"{Env().pwz_url}/auth/login"
EMP_DASH_URL = f"{Env().emp_dash_url}/"
MAIL_PIT_URL = f"{Env().mailpit}/"
MIM_URL = f"{Env().mim_url}"
CABINET_URL = f"{Env().partner_url}/"


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    web_driver = webdriver.Remote(command_executor=f"{Env().remote_webdriver_url}",
                                  options=options)
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()


class PageManager:  # pylint: disable=too-few-public-methods
    def __init__(self, driver):
        self.driver = driver
        self.top_bar = TopBarCpPage(driver, url=CP_URL)
        self.side_bar_cp = SideBarCpPage(driver, url=CP_URL)
        self.cp_auth_form = KeycloackAuthForm(driver, url=CP_URL)
        self.cp_main = AllOptionsCpPage(driver, url=CP_URL)
        self.sb_auth_form = KeycloackAuthForm(driver, url=SB_URL)
        self.sb_main = ServiceBookingMainPage(driver, url=SB_URL)
        self.auth_pwz_form = KeycloackAuthForm(driver, url=PWZ_URL)
        self.pwz_main = PWZMainPage(driver, url=PWZ_URL)
        self.emp_dash_auth_form = KeycloackAuthForm(driver, url=EMP_DASH_URL)
        self.emp_dash_main = EmpDashMainPage(driver, url=EMP_DASH_URL)
        self.mailpit_page = MailPitMain(driver, url=MAIL_PIT_URL)
        self.mim_page = MimAuthPage(driver, url=MIM_URL)
        self.cabinet_landing_page = PartnerLandingPage(driver, url=CABINET_URL)
        self.cabinet_page = PartnerOptionsPage(driver, url=CABINET_URL)
        self.cabinet_side_bar = SideBarCabinetPage(driver, url=CABINET_URL)
        self.cabinet_top_bar = TopBarCabinetPage(driver, url=CABINET_URL)
        self.profile_page = ProfilePageCabinet(driver, url=CABINET_URL)
        self.b2b_employee_page = B2bEmployeePageCab(driver, url=CABINET_URL)


@pytest.fixture
def pages(driver):
    return PageManager(driver)


class StepsManager:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.common_steps = CommonSteps(driver, url=self.url)
        self.tables_steps = TablesSteps(driver, url=self.url)


@pytest.fixture
def steps(driver):
    return StepsManager(driver, url=CP_URL)


############################################################################################################
############################### ПЕРЕПИСЫВАЮ НА НОВЫЕ ФИКСТУРЫ ##############################################
# В этом конфтесте ничего не иимпортируем и в ините ничего кроме драйвера который дальше передаём. #########
# Так как тут хранится только фикстура запуска браузера и отключение его после выполнения тестов в модуле ##
# Для каждой папки будет своя фикстура которая будет "на модуль" инициировать свои классы ##################
# По крайней мере я думаю что так будет работать нормально #################################################
# Если тесты мешают друг другу запуском "на модуль" то либо разнести тесты по файлам либо прописать шаги ###
# необходимые для работы каждого тестов внутри одного модуля без того что они мешают друг другу ############
############################################################################################################

fixture = None


@pytest.fixture
def app(request):
    global fixture
    stage = request.config.getoption("--stage")
    browser = request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser)
    return fixture


@pytest.fixture(scope='module', autouse=True)
def stop(request):
    def fin():
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome_remote",
                     help='example: chrome_remote for docker, chrome for pc browser with venv usage')
    parser.addoption("--stage", action="store", default='dev', help="dev for dev, stage for stage")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x[1]) for x in testdata])
        # elif fixture.startswith("json_"):
        #     testdata = load_from_json(fixture[5:])
        #     metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


# работа с файлами .py в папке data
# аналог 'from data.{имя файла}.py import testdata' для каждого файла с тестами
def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

# # работа с json
# def load_from_json(file):
#     with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
#         return jsonpickle.decode(f.read())


class Application:

    def __init__(self, browser):
        if browser == "chrome_remote":
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Remote(command_executor=f"{Env().remote_webdriver_url}",
                                           options=options)
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
            # try:
            #     self.driver = webdriver.Chrome()
            # except:
            #     service = Service(executable_path=f"{Env().local_chrome_driver}")
            #     # service = Service(executable_path='C:\PycharmProjects\webdrivers\chromedriver.exe')
            #     self.driver = webdriver.Chrome(service=service)
            # # self.driver.maximize_window()

        elif browser == "firefox" or browser == "ff":
            self.driver = webdriver.Firefox()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

    def is_valid(self):
        try:
            # noinspection PyStatementEffect
            self.driver.current_url
            # print(1)
            return True
        except:
            # print(0)
            return False

    def destroy(self):
        self.driver.quit()
