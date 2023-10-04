import configparser
import time
import allure

from utils.env import Env
from pages.base_page import BasePage
from pages.keycloak.keycloack_auth_page import KeycloackAuthForm
from pages.control_panel.ui.topbar_cp_page import TopBarCpPage
from pages.control_panel.options.all_options_page import AllOptionsCpPage
from pages.control_panel.options.add_new_option_page import AddNewOptionCpPage
from pages.mailpit.mailpit_main import MailPitMain
from selenium.webdriver.common.action_chains import ActionChains



config = configparser.ConfigParser()
config.read('ini_config/config.ini')

CP_URL = f"{Env().cp_url}/auth/login"
MAIL_PIT_URL = f"{Env().mailpit}/"
EMAIL = config.get('credentials', 'EMAIL')
INTERNAL_MAIL = config.get('credentials', 'INTERNAL_MAIL')
INTERNAL_PASS = config.get('credentials', 'INTERNAL_PASS')
WRONG_MAIL = config.get('credentials', 'WRONG_MAIL')
WRONG_USER_PASS = config.get('credentials', 'WRONG_USER_PASS')
USER_PASS = config.get('credentials', 'USER_PASS')
ERROR_TEXT = config.get('expected_results', 'ERROR_TEXT')
ERROR_PASS_TEXT = config.get('expected_results', 'PASS_ARE_DIFF')


@allure.suite("Тесты авторизации")
@allure.sub_suite("Набор тестов Панели Управления")
class TestLoginKeyCloack():

    @allure.title("Запрет авторизации сущест. пользователя с неправильным паролем")
    def test_login_wrong_pass(self, driver):
        page = BasePage(driver, CP_URL)
        page.open()
        auth_form = KeycloackAuthForm(driver, url=CP_URL)
        auth_form.login(EMAIL, WRONG_USER_PASS)
        assert ERROR_TEXT == auth_form.error_message(), "Wrong error text"

    @allure.title("Запрет авторизации НЕсущест. пользователя с правильным паролем")
    def test_login_wrong_mail(self, driver):
        page = BasePage(driver, CP_URL)
        page.open()
        auth_form = KeycloackAuthForm(driver, url=CP_URL)
        auth_form.login(WRONG_MAIL, USER_PASS)
        assert ERROR_TEXT == auth_form.error_message(), "Wrong error text"

    @allure.title("Авторизация корректного пользователя")
    def test_login_correct_user(self, driver):
        page = BasePage(driver, CP_URL)
        page.open()
        auth_form = KeycloackAuthForm(driver, url=CP_URL)
        auth_form.login(EMAIL, USER_PASS)
        assert 'Панель управления' == driver.title, "Wrong title of page, or wrong page was loaded"
        top_bar = TopBarCpPage(driver, url=CP_URL)
        top_bar.click_open_profile_dropdown().click_deauth_button()
        time.sleep(1)
        assert auth_form.is_title_correct('Авторизация в internal'), "Wrong title after logout"

    @allure.title("Восстановление почты пользователя + Кейс несовпадения вводимых новых паролей")
    def test_recovery_mail(self, driver):
        page = BasePage(driver, CP_URL)
        page.open()
        auth_form = KeycloackAuthForm(driver, url=CP_URL)
        auth_form.click_forgot_pass()
        auth_form.input_recovery_mail(INTERNAL_MAIL)
        driver.execute_script("window.open('', '_blank');")
        # Переключение контекста на вторую вкладку
        driver.switch_to.window(driver.window_handles[1])
        mailpit_page = MailPitMain(driver, MAIL_PIT_URL)
        mailpit_page.open()
        mailpit_page.find_by_client(INTERNAL_MAIL)
        mailpit_page.click_restore_url(driver)
        # Переключение контекста на третью вкладку
        driver.switch_to.window(driver.window_handles[2])
        auth_form.input_different_pass(INTERNAL_PASS, WRONG_USER_PASS)
        # Проверка несовпадения паролей
        assert ERROR_PASS_TEXT == auth_form.error_pass_are_diff(), "Wrong error-text or not found"
        auth_form.accept_pass_for_restore(INTERNAL_PASS)
        assert 'Панель управления' == driver.title, "Wrong title of page, or wrong page was loaded"
