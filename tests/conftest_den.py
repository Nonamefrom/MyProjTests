import pytest
from selenium import webdriver
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
from steps.common_steps import CommonSteps
from steps.tables_steps import TablesSteps
from utils.env import Env

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
    web_driver = webdriver.Remote(
        command_executor=f"{Env().remote_webdriver_url}",
        options=options
    )
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()


class PageManager:  # pylint: disable=too-few-public-methods
    def __init__(self, driver):
        self.driver = driver
        self.top_bar = TopBarCpPage(driver, url=CP_URL)
        self.side_bar_cp = SideBarCpPage(driver, url=CP_URL)
        self.cp_auth_form = KeycloackAuthForm(driver, CP_URL)
        self.cp_main = AllOptionsCpPage(driver, url=CP_URL)
        self.sb_auth_form = KeycloackAuthForm(driver, url=SB_URL)
        self.sb_main = ServiceBookingMainPage(driver, url=SB_URL)
        self.auth_pwz_form = KeycloackAuthForm(driver, url=PWZ_URL)
        self.pwz_main = PWZMainPage(driver, url=PWZ_URL)
        self.emp_dash_auth_form = KeycloackAuthForm(driver, EMP_DASH_URL)
        self.emp_dash_main = EmpDashMainPage(driver, url=EMP_DASH_URL)
        self.mailpit_page = MailPitMain(driver, MAIL_PIT_URL)
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
