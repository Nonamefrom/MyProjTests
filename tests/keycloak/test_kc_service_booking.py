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
@allure.sub_suite("Набор тестов авторизации Онлайн Записи")
class TestLoginServiceBooking:
    @allure.title("Запрет авторизации существ. b2b пользователя с неправильным паролем ОЗ")
    def test_sb_login_b2b_wrong_pass(self, kc):
        kc.sb_auth_form.open().go_to_login("b2b").login(EMAIL, WRONG_USER_PASS)
        got_error = kc.sb_auth_form.error_message()
        assert ER.ERROR_TEXT == got_error, f"Expected '{ER.ERROR_TEXT}' but got '{got_error}'"

    @allure.title("Запрет авторизации НЕ существ. b2b пользователя с правильным паролем ОЗ")
    def test_sb_login_b2b_wrong_mail(self, kc):
        kc.sb_auth_form.open().go_to_login("b2b").login(WRONG_MAIL, USER_PASS)
        got_error = kc.sb_auth_form.error_message()
        assert ER.ERROR_TEXT == got_error, f"Expected '{ER.ERROR_TEXT}' but got '{got_error}'"

    @allure.title("Запрет авторизации b2b в internal realm ОЗ")
    def test_sb_login_b2b_like_internal(self, kc):
        kc.sb_auth_form.open().go_to_login("internal").login(B2B_MAIL, B2B_PASS)
        got_error = kc.sb_auth_form.error_message()
        assert ER.ERROR_TEXT == got_error, f"Expected '{ER.ERROR_TEXT}' but got '{got_error}'"

    @allure.title("Авторизация корректного b2b пользователя ОЗ")
    def test_sb_login_correct_b2b_user(self, kc):
        kc.sb_auth_form.open().go_to_login("b2b").login(B2B_MAIL, B2B_PASS)
        got_sb_main_h1 = kc.sb_main.sb_h1_text()
        assert ER.SERVICE_BOOKING_H1 == got_sb_main_h1, f"Expected '{ER.SERVICE_BOOKING_H1}' but got '{got_sb_main_h1}'"
        kc.top_bar_cp.click_open_profile_dropdown().click_deauth_button()
        time.sleep(1)
        assert kc.sb_auth_form.check_b2b_internal_buttons() is True, "Кнопки b2b/internal авторизации не найдены"

    @allure.title("Авторизация корректного internal пользователя ОЗ")
    def test_sb_login_correct_internal_user(self, kc):
        kc.sb_auth_form.open().go_to_login("internal").login(INTERNAL_MAIL, INTERNAL_PASS)
        got_sb_main_h1 = kc.sb_main.sb_h1_text()
        assert ER.SERVICE_BOOKING_H1 == got_sb_main_h1, f"Expected '{ER.SERVICE_BOOKING_H1}' but got '{got_sb_main_h1}'"
        kc.top_bar_cp.click_open_profile_dropdown().click_deauth_button()
        time.sleep(1)
        assert kc.sb_auth_form.check_b2b_internal_buttons() is True, "Кнопки b2b/internal авторизации не найдены"

    @allure.title("Восстановление почты пользователя + Кейс несовпадения вводимых новых паролей ОЗ")
    def test_recovery_mail_sb(self, kc):
        kc.sb_auth_form.open().go_to_login("internal").click_forgot_pass()
        kc.sb_auth_form.input_recovery_mail(INTERNAL_MAIL)
        kc.driver.execute_script("window.open('', '_blank');")
        # Переключение контекста на вторую вкладку
        kc.driver.switch_to.window(kc.driver.window_handles[1])
        kc.mailpit_page.open().find_by_client(INTERNAL_MAIL).click_restore_url(kc.driver)
        # Переключение контекста на третью вкладку
        kc.driver.switch_to.window(kc.driver.window_handles[2])
        kc.sb_auth_form.input_different_pass(INTERNAL_PASS, WRONG_USER_PASS)
        # Проверка несовпадения паролей
        assert ER.PASS_ARE_DIFF == kc.sb_auth_form.error_pass_are_diff(), "Wrong error-text or not found"
        kc.sb_auth_form.accept_pass_for_restore(INTERNAL_PASS)
        got_sb_h1 = kc.sb_main.sb_h1_text()
        assert ER.SERVICE_BOOKING_H1 == got_sb_h1, f"Expected '{ER.SERVICE_BOOKING_H1}' but got '{got_sb_h1}'"
