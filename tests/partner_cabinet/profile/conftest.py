import pytest
from selenium import webdriver
from utils.env import Env
# импорт главной фикстуры
from tests.conftest import app
# импорт степов
from steps.common_steps import CommonSteps
from steps.tables_steps import TablesSteps
# всё кроме страниц
from pages.partner_cabinet.ui.sidebar_cabinet_page import SideBarCabinetPage
from pages.partner_cabinet.ui.topbar_cabinet_page import TopBarCabinetPage
# импорт для тестов
from pages.keycloak.keycloack_auth_page import KeycloackAuthForm
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

fixture = None


@pytest.fixture
def pc(app):
    global fixture
    fixture = Application(app)
    return fixture


@pytest.fixture(scope='function', autouse=True)
def stop(request):
    def fin():
        # print(fixture)
        fixture.driver.quit()
    request.addfinalizer(fin)
    return fixture


class Application:

    def __init__(self, app):
        self.driver = app.driver
        driver = app.driver
        self.common_steps = CommonSteps(driver, url=CP_URL)
        self.tables_steps = TablesSteps(driver, url=CP_URL)

        self.cp_auth_form = KeycloackAuthForm(driver, url=CP_URL)
        self.mim_page = MimAuthPage(driver, url=MIM_URL)
        self.cabinet_landing_page = PartnerLandingPage(driver, url=CABINET_URL)
        self.cabinet_page = PartnerOptionsPage(driver, url=CABINET_URL)
        self.cabinet_side_bar = SideBarCabinetPage(driver, url=CABINET_URL)
        self.cabinet_top_bar = TopBarCabinetPage(driver, url=CABINET_URL)
        self.profile_page = ProfilePageCabinet(driver, url=CABINET_URL)
        self.b2b_employee_page = B2bEmployeePageCab(driver)
