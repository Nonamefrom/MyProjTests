import time
import allure
from data.test_data import ExpectedResults as ER
from data.test_data import RegData


EMAIL = RegData.EMAIL
INTERNAL_MAIL = RegData.INTERNAL_MAIL
INTERNAL_PASS = RegData.INTERNAL_PASS
B2B_MAIL = RegData.B2B_MAIL
B2B_PASS = RegData.B2B_PASS
WRONG_MAIL = RegData.WRONG_MAIL
WRONG_USER_PASS = RegData.WRONG_USER_PASS
USER_PASS = RegData.USER_PASS


@allure.suite("Тесты авторизации")
@allure.sub_suite("Набор тестов авторизации Панели Управления")
class TestLoginControlPanel:
    @allure.title("Запрет авторизации существ. пользователя с неправильным паролем ПУ")
    @allure.id('KeyCloack/CP/№ 1')
    def test_login_wrong_pass(self, kc):
        kc.cp_auth_form.open().login(EMAIL, WRONG_USER_PASS)
        got_error = kc.cp_auth_form.error_message()
        assert ER.ERROR_TEXT == got_error, f"Expected '{ER.ERROR_TEXT}' but got '{got_error}'"

    @allure.title("Запрет авторизации НЕ существ. пользователя с правильным паролем ПУ")
    @allure.id('KeyCloack/CP/№ 2')
    def test_login_wrong_mail(self, kc):
        kc.cp_auth_form.open().login(WRONG_MAIL, USER_PASS)
        got_error = kc.cp_auth_form.error_message()
        assert ER.ERROR_TEXT == got_error, f"Expected '{ER.ERROR_TEXT}' but got '{got_error}'"

    @allure.title("Авторизация корректного пользователя ПУ")
    @allure.id('KeyCloack/CP/№ 3')
    def test_login_correct_user(self, kc):
        kc.cp_auth_form.open().login(EMAIL, USER_PASS)
        got_cp_h1 = kc.cp_main.cp_h1_text()
        assert ER.CONTROL_PANEL_H1 == got_cp_h1, f"Expected '{ER.CONTROL_PANEL_H1}' but got '{got_cp_h1}'"
        kc.top_bar_cp.click_open_profile_dropdown().click_deauth_button()
        got_title = kc.cp_auth_form.auth_h1_text()
        assert 'Вход для операторов' == got_title, f"Expected 'Вход для операторов' but got '{got_title}'"

    @allure.title("Восстановление почты пользователя + Кейс несовпадения вводимых новых паролей ПУ")
    @allure.id('KeyCloack/CP/№ 4')
    def test_recovery_mail(self, kc):
        kc.cp_auth_form.open().click_forgot_pass()
        kc.cp_auth_form.input_recovery_mail(INTERNAL_MAIL)
        kc.driver.execute_script("window.open('', '_blank');")
        # Переключение контекста на вторую вкладку
        kc.driver.switch_to.window(kc.driver.window_handles[1])
        kc.mailpit_page.open().find_by_client(INTERNAL_MAIL).click_restore_url(kc.driver)
        # Переключение контекста на третью вкладку
        kc.driver.switch_to.window(kc.driver.window_handles[2])
        kc.cp_auth_form.input_different_pass(INTERNAL_PASS, WRONG_USER_PASS)
        # Проверка несовпадения паролей
        got_error_text = kc.cp_auth_form.error_pass_are_diff()
        assert ER.PASS_ARE_DIFF == got_error_text, f"Expected '{ER.PASS_ARE_DIFF}' but got '{got_error_text}'"
        kc.cp_auth_form.accept_pass_for_restore(INTERNAL_PASS)
        got_cp_h1 = kc.cp_main.cp_h1_text()
        assert ER.CONTROL_PANEL_H1 == got_cp_h1, f"Expected '{ER.CONTROL_PANEL_H1}' but got '{got_cp_h1}'"
