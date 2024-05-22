import pytest
from selenium import webdriver
from utils.env import Env
# импорт главной фикстуры
from tests.conftest import app
# импорт степов
from steps.common_steps import CommonSteps
from steps.tables_steps import TablesSteps
# всё кроме страниц
from pages.control_panel.ui.topbar_cp_page import TopBarCpPage
from pages.control_panel.ui.sidebar_cp_page import SideBarCpPage
from pages.partner_cabinet.ui.topbar_cabinet_page import TopBarCabinetPage
# импорт для тестов
from pages.keycloak.keycloack_auth_page import KeycloackAuthForm
from pages.partner_cabinet.mim_page import MimAuthPage
from pages.control_panel.internal_user_page import InternalUserPage
from pages.control_panel.notification import NotificationPage
from pages.partner_cabinet.notification import PartnerCabinetNotifications
from pages.partner_cabinet.partner_landing import PartnerLandingPage
# импорт панели навигации внутри опции
from pages.control_panel.option_tab.fts_connection import FtsConnection
from pages.control_panel.option_tab.pwz_admin_tab import AdminTab
from pages.control_panel.option_tab.users import UsersTab


CP_URL = f"{Env().cp_url}/auth/login"
CABINET_URL = f"{Env().partner_url}/"
MIM_URL = f"{Env().mim_url}"

fixture = None


@pytest.fixture
def cp(app):
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
        self.top_bar_cp = TopBarCpPage(driver)
        self.top_bar = TopBarCabinetPage(driver, url=CABINET_URL)
        self.side_bar_cp = SideBarCpPage(driver)
        self.internal_page = InternalUserPage(driver)
        self.notifications = NotificationPage(driver)
        self.pc_notifications = PartnerCabinetNotifications(driver)
        self.cp_auth_form = KeycloackAuthForm(driver, url=CP_URL)
        self.mim_page = MimAuthPage(driver, url=MIM_URL)
        self.cabinet_landing_page = PartnerLandingPage(driver, url=CABINET_URL)
