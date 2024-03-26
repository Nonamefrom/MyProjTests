import pytest
from selenium import webdriver
from utils.env import Env
import importlib
from tests.conftest import app

from steps.common_steps import CommonSteps
from steps.tables_steps import TablesSteps

from pages.keycloak.keycloack_auth_page import KeycloackAuthForm
# from pages.control_panel.ui.topbar_cp_page import TopBarCpPage
# from pages.control_panel.ui.sidebar_cp_page import SideBarCpPage
# from pages.control_panel.options.all_options_page import AllOptionsCpPage
# from pages.mailpit.mailpit_main import MailPitMain
# from pages.service_booking.service_booking_mainpage import ServiceBookingMainPage
# from pages.pwz.pwz_mainpage import PWZMainPage
# from pages.employee_dashboard.emp_dash_mainpage import EmpDashMainPage
# from pages.partner_cabinet.mim_page import MimAuthPage
# from pages.partner_cabinet.partner_landing import PartnerLandingPage
# from pages.partner_cabinet.partner_options_page import PartnerOptionsPage
# from pages.partner_cabinet.ui.sidebar_cabinet_page import SideBarCabinetPage
# from pages.partner_cabinet.ui.topbar_cabinet_page import TopBarCabinetPage
# from pages.partner_cabinet.profile_page import ProfilePageCabinet
# from pages.partner_cabinet.b2b_empoyee_page import B2bEmployeePageCab

CP_URL = f"{Env().cp_url}/auth/login"
SB_URL = f"{Env().sb_url}/"
PWZ_URL = f"{Env().pwz_url}/auth/login"
EMP_DASH_URL = f"{Env().emp_dash_url}/"
MAIL_PIT_URL = f"{Env().mailpit}/"
MIM_URL = f"{Env().mim_url}"
CABINET_URL = f"{Env().partner_url}/"


@pytest.fixture
def ref(app):
    fixture = Application(app)
    return fixture


class Application:

    def __init__(self, app):
        driver = app.driver
        self.common_steps = CommonSteps(driver, url=CP_URL)
        self.tables_steps = TablesSteps(driver, url=CP_URL)
        # self.pwz_main = PWZMainPage(driver, url=PWZ_URL)
        # self.mim_page = MimAuthPage(driver, url=MIM_URL)
        self.cp_auth_form = KeycloackAuthForm(driver, url=CP_URL)


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


# работа с файлами .py в папке data
# аналог 'from data.{имя файла}.py import testdata' для каждого файла с тестами
def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata
# аналог from data.cp_user_wrong_pass.py import testdata


# работа с json
def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())
