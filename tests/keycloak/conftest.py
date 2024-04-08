import pytest
from selenium import webdriver
from utils.env import Env
# импорт главной фикстуры
from tests.conftest import app
# импорт степов
from steps.common_steps import CommonSteps
from steps.tables_steps import TablesSteps
# всё кроме страниц
from pages.control_panel.ui.sidebar_cp_page import SideBarCpPage
from pages.control_panel.ui.topbar_cp_page import TopBarCpPage
from pages.partner_cabinet.ui.topbar_cabinet_page import TopBarCabinetPage
from pages.partner_cabinet.ui.sidebar_cabinet_page import SideBarCabinetPage
# импорт для тестов
from pages.keycloak.keycloack_auth_page import KeycloackAuthForm
from pages.control_panel.options.all_options_page import AllOptionsCpPage
from pages.mailpit.mailpit_main import MailPitMain
from pages.pwz.pwz_mainpage import PWZMainPage
from pages.control_panel.pwz_option import PwzOptionPage
from pages.service_booking.service_booking_mainpage import ServiceBookingMainPage
from pages.employee_dashboard.emp_dash_mainpage import EmpDashMainPage


CP_URL = f"{Env().cp_url}/auth/login"
SB_URL = f"{Env().sb_url}/"
PWZ_URL = f"{Env().pwz_url}/auth/login"
EMP_DASH_URL = f"{Env().emp_dash_url}/"
MAIL_PIT_URL = f"{Env().mailpit}/"
MIM_URL = f"{Env().mim_url}"
CABINET_URL = f"{Env().partner_url}/"

fixture = None


@pytest.fixture
def kc(app):
    global fixture

    fixture = Application(app)
    # print(fixture)
    return fixture


@pytest.fixture(scope='function', autouse=True)
def stop(request):
    def fin():
        fixture.driver.quit()

    request.addfinalizer(fin)
    return fixture


class Application:

    def __init__(self, app):
        self.driver = app.driver
        driver = app.driver
        self.common_steps = CommonSteps(driver, url=CP_URL)
        self.tables_steps = TablesSteps(driver, url=CP_URL)
        self.top_bar_cp = TopBarCpPage(driver)
        self.side_bar_cp = SideBarCpPage(driver)
        self.top_bar_pc = TopBarCabinetPage(driver)
        self.side_bar_pc = SideBarCabinetPage(driver)
        self.pwz_main = PWZMainPage(driver, url=CP_URL)
        self.pwz_option = PwzOptionPage(driver, url=CP_URL)

        self.cp_auth_form = KeycloackAuthForm(driver, url=CP_URL)
        self.sb_auth_form = KeycloackAuthForm(driver, url=SB_URL)
        self.auth_pwz_form = KeycloackAuthForm(driver, url=PWZ_URL)
        self.emp_dash_auth_form = KeycloackAuthForm(driver, url=EMP_DASH_URL)
        self.cp_main = AllOptionsCpPage(driver, url=CP_URL)
        self.mailpit_page = MailPitMain(driver, url=MAIL_PIT_URL)
        self.sb_main = ServiceBookingMainPage(driver, url=SB_URL)
        self.emp_dash_main = EmpDashMainPage(driver, url=EMP_DASH_URL)

