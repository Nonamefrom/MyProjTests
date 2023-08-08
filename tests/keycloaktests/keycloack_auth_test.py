import allure
import pytest
import configparser
from pages.base_page import BasePage
from pages.keycloack_auth_page import KeycloackAuthForm
from pages.controlpanelpages.topbar_cp_page import TopBarCpPage

config = configparser.ConfigParser()
config.read('ini_config/config.ini')

CP_URL = config.get('credentials', 'CP_URL')
EMAIL = config.get('credentials', 'EMAIL')
WRONG_MAIL = config.get('credentials', 'WRONG_MAIL')
WRONG_USER_PASS = config.get('credentials', 'WRONG_USER_PASS')
USER_PASS = config.get('credentials', 'USER_PASS')
ERROR_TEXT = config.get('expected_results', 'ERROR_TEXT')


@allure.suite("Тесты авторизации")
@allure.sub_suite("Набор тестов Панели Управления")
class TestLoginKeyCloack():
# Авторизация существующего пользователя ПУ с неправильным паролем
    @allure.title("Авторизация сущест. пользователя с неправильным паролем")
    def test_login_wrong_pass(self, driver):
        page = BasePage(driver, CP_URL)
        page.open()
        auth_form = KeycloackAuthForm(driver, url=CP_URL)
        auth_form.login(EMAIL, WRONG_USER_PASS)
        assert ERROR_TEXT == auth_form.error_message(), "Wrong error text"


# Авторизация НЕсуществующего пользователя ПУ с правильным паролем
    @allure.title("Авторизация НЕсущест. пользователя с правильным паролем")
    def test_login_wrong_mail(self, driver):
        page = BasePage(driver, CP_URL)
        page.open()
        auth_form = KeycloackAuthForm(driver, url=CP_URL)
        auth_form.login(WRONG_MAIL, USER_PASS)
        assert ERROR_TEXT == auth_form.error_message(), "Wrong error text"


# Авторизация/деавторизация существующего пользователя ПУ с правильным паролем
    @allure.title("Авторизация корректного пользователя")
    def test_login_correct_user(self, driver):
        page = BasePage(driver, CP_URL)
        page.open()
        auth_form = KeycloackAuthForm(driver, url=CP_URL)
        auth_form.login(EMAIL, USER_PASS)
        assert 'Панель управления' == driver.title, "Wrong title of page, or wrong page was loaded"
        top_bar = TopBarCpPage(driver, CP_URL)
        top_bar.click_open_profile_dropdown().click_deauth_button()
        assert auth_form.is_title_correct('Авторизация в internal'), "Wrong title after logout"
