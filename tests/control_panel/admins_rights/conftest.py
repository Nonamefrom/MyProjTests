import pytest
from selenium import webdriver
from utils.env import Env
from tests.conftest import app  # импорт главной фикстуры
# импорт для тестов
from steps.common_steps import CommonSteps
from steps.tables_steps import TablesSteps
from pages.control_panel.ui.topbar_cp_page import TopBarCpPage
from pages.control_panel.ui.sidebar_cp_page import SideBarCpPage
from pages.keycloak.keycloack_auth_page import KeycloackAuthForm
# импорт панели навигации внутри опции
from pages.control_panel.option_tab.fts_connection import FtsConnection
from pages.control_panel.option_tab.pwz_admin_tab import AdminTab
from pages.control_panel.option_tab.users import UsersTab

CP_URL = f"{Env().cp_url}/auth/login"


@pytest.fixture
def cp(app):
    fixture = Application(app)
    return fixture


class Application:

    def __init__(self, app):
        driver = app.driver
        self.common_steps = CommonSteps(driver, url=CP_URL)
        self.tables_steps = TablesSteps(driver, url=CP_URL)
        self.top_bar = TopBarCpPage(driver)
        self.side_bar = SideBarCpPage(driver)

        self.cp_auth_form = KeycloackAuthForm(driver, url=CP_URL)

        self.fts = FtsConnection(driver)
        self.admin = AdminTab(driver)
        self.users = UsersTab(driver)



