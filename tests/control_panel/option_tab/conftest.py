import pytest
from selenium import webdriver
from utils.env import Env
from tests.conftest import app  # импорт главной фикстуры
from steps.common_steps import CommonSteps
from steps.tables_steps import TablesSteps
# импорт для тестов
from pages.keycloak.keycloack_auth_page import KeycloackAuthForm
from pages.pwz.pwz_mainpage import PWZMainPage
from pages.control_panel.pwz_option import PwzOptionPage
from pages.control_panel.ui.topbar_cp_page import TopBarCpPage
# импорт панели навигации внутри опции
from pages.control_panel.option_tab.additional_info import AdditionalInfoTab
from pages.control_panel.option_tab.edu_results import EducationTab
from pages.control_panel.option_tab.fts_connection import FtsConnection
from pages.control_panel.option_tab.info import InfoTab
from pages.control_panel.option_tab.limits import LimitsTab
from pages.control_panel.option_tab.nomenclature import NomenclatureTab
from pages.control_panel.option_tab.promocodes import PromocodeTab
from pages.control_panel.option_tab.pwz_admin_tab import AdminTab
from pages.control_panel.option_tab.rg_applications import RgApplicationTab
from pages.control_panel.option_tab.rg_authorizations import RgAuthorizationTab
from pages.control_panel.option_tab.rg_conditions import RgConditionsTab
from pages.control_panel.option_tab.rg_sms import RgSmsTab
from pages.control_panel.option_tab.users import UsersTab


CP_URL = f"{Env().cp_url}/auth/login"
SB_URL = f"{Env().sb_url}/"
PWZ_URL = f"{Env().pwz_url}/auth/login"
EMP_DASH_URL = f"{Env().emp_dash_url}/"
MAIL_PIT_URL = f"{Env().mailpit}/"
MIM_URL = f"{Env().mim_url}"
CABINET_URL = f"{Env().partner_url}/"


@pytest.fixture
def cp(app):
    fixture = Application(app)
    return fixture


class Application:

    def __init__(self, app):
        driver = app.driver
        self.common_steps = CommonSteps(driver, url=CP_URL)
        self.tables_steps = TablesSteps(driver, url=CP_URL)
        self.pwz_main = PWZMainPage(driver, url=CP_URL)
        self.pwz_option = PwzOptionPage(driver, url=CP_URL)
        self.cp_auth_form = KeycloackAuthForm(driver, url=CP_URL)
        self.top_bar = TopBarCpPage(driver)

        self.additional = AdditionalInfoTab(driver)
        self.edu = EducationTab(driver)
        self.fts = FtsConnection(driver)
        self.info = InfoTab(driver)
        self.limits = LimitsTab(driver)
        self.nomen = NomenclatureTab(driver)
        self.promo = PromocodeTab(driver)
        self.admin = AdminTab(driver)
        self.rgapp = RgApplicationTab(driver)
        self.rgauth = RgAuthorizationTab(driver)
        self.rgcond = RgConditionsTab(driver)
        self.rgsms = RgSmsTab(driver)
        self.users = UsersTab(driver)



