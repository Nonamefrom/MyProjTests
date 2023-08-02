import allure
import pytest
from pages.base_page import BasePage
from pages.keycloack_auth_page import KeycloackAuthForm
from pages.topbar_cp_page import TopBarCpPage

CPurl = 'https://develop-cp.dev.svrauto.ru/auth/login'
email = 'admin@svrauto.ru'
wrongemail = 'admin@admin@ru23'
wronguserpass = '123456789'
userpass = 'adminPass'
errortext = 'Неправильное имя пользователя или пароль.'


@allure.suite("Тесты авторизации")
@allure.sub_suite("Набор тестов Панели Управления")
# Авторизация существующего пользователя ПУ с неправильным паролем
@allure.title("Авторизация сущест. пользователя с неправильным паролем")
def test_login_wrong_pass(driver):
    page = BasePage(driver, CPurl)
    page.open()
    auth_form = KeycloackAuthForm(driver, url=CPurl)
    auth_form.login(email, wronguserpass)
    assert errortext == auth_form.error_message(), "Wrong error text"


# Авторизация НЕсуществующего пользователя ПУ с правильным паролем
@allure.title("Авторизация НЕсущест. пользователя с правильным паролем")
def test_login_wrong_mail(driver):
    page = BasePage(driver, CPurl)
    page.open()
    auth_form = KeycloackAuthForm(driver, url=CPurl)
    auth_form.login(wrongemail, userpass)
    assert errortext == auth_form.error_message(), "Wrong error text"


# Авторизация существующего пользователя ПУ с правильным паролем
@allure.title("Авторизация корректного пользователя")
def test_login_correct_user(driver):
    page = BasePage(driver, CPurl)
    page.open()
    auth_form = KeycloackAuthForm(driver, url=CPurl)
    auth_form.login(email, userpass)
    assert 'Панель управления' == driver.title, "Wrong title of page, or wrong page was loaded"
    top_bar = TopBarCpPage(driver, CPurl)
    top_bar.click_open_profile_dropdown().click_deauth_button()
    assert auth_form.is_title_correct('Авторизация в internal'), "Wrong title after logout"


if __name__ == "__main__":
    pytest.main()
