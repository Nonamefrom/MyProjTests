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
# импорт для тестов
from pages.keycloak.keycloack_auth_page import KeycloackAuthForm
from pages.control_panel.internal_user_page import InternalUserPage
# импорт панели навигации внутри опции
from pages.control_panel.option_tab.fts_connection import FtsConnection
from pages.control_panel.option_tab.pwz_admin_tab import AdminTab
from pages.control_panel.option_tab.users import UsersTab

CP_URL = f"{Env().cp_url}/auth/login"

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
        self.side_bar_cp = SideBarCpPage(driver)
        self.internal_page = InternalUserPage(driver)

        self.cp_auth_form = KeycloackAuthForm(driver, url=CP_URL)

        self.fts = FtsConnection(driver)
        self.admin = AdminTab(driver)
        self.users = UsersTab(driver)



