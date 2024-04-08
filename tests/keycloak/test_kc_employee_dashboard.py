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
@allure.sub_suite("Набор тестов авторизации Дашборда сотрудника")
class TestLoginEmployeeDashboard:
    @allure.title("Запрет авторизации существ. пользователя EMPDASH с неправильным паролем Employee Dashboard")
    def test_employee_dash_login_wrong_pass(self, kc):
        kc.emp_dash_auth_form.open().login(B2B_MAIL, WRONG_USER_PASS)
        got_error = kc.emp_dash_auth_form.error_message()
        assert ER.ERROR_TEXT == got_error, f"Expected '{ER.ERROR_TEXT}' but got '{got_error}'"

    @allure.title("Запрет авторизации НЕ существ. b2b пользователя EMPDASH с правильным паролем Employee Dashboard")
    def test_employee_dash_login_b2b_wrong_mail(self, kc):
        kc.emp_dash_auth_form.open().login(WRONG_MAIL, B2B_PASS)
        got_error = kc.emp_dash_auth_form.error_message()
        assert ER.ERROR_TEXT == got_error, f"Expected '{ER.ERROR_TEXT}' but got '{got_error}'"

    @allure.title("Запрет авторизации internal в b2b realm Employee Dashboard")
    def test_employee_dash_login_b2b_like_internal(self, kc):
        kc.emp_dash_auth_form.open().login(INTERNAL_MAIL, INTERNAL_PASS)
        got_error = kc.emp_dash_auth_form.error_message()
        assert ER.ERROR_TEXT == got_error, f"Expected '{ER.ERROR_TEXT}' but got '{got_error}'"

    @allure.title("Авторизация корректного b2b пользователя Employee Dashboard")
    def test_employee_dash_login_correct_b2b_user(self, kc):
        kc.emp_dash_auth_form.open().login(B2B_MAIL, B2B_PASS)
        got_emp_dash_h1 = kc.emp_dash_main.employee_dashboard_h1_text()
        assert ER.EMP_DASH_H1 == got_emp_dash_h1, f"Expected '{ER.EMP_DASH_H1}' but got '{got_emp_dash_h1}'"
        kc.top_bar_pc.open_profile_dropdown_emp().click_deauth_button_emp()
        time.sleep(1)
        got_title = kc.emp_dash_auth_form.auth_h1_text()
        assert 'Вход для партнеров' == got_title, f"Expected 'Вход для партнеров' but got '{got_title}'"

    @allure.title("Восстановление почты пользователя + Кейс несовпадения вводимых новых паролей Employee Dashboard")
    def test_recovery_mail_employee_dash(self, kc):
        kc.emp_dash_auth_form.open().click_forgot_pass()
        kc.emp_dash_auth_form.input_recovery_mail(B2B_MAIL)
        kc.driver.execute_script("window.open('', '_blank');")
        # Переключение контекста на вторую вкладку
        kc.driver.switch_to.window(kc.driver.window_handles[1])
        kc.mailpit_page.open().find_by_client(B2B_MAIL).click_restore_url(kc.driver)
        # Переключение контекста на третью вкладку
        kc.driver.switch_to.window(kc.driver.window_handles[2])
        kc.emp_dash_auth_form.input_different_pass(B2B_PASS, WRONG_USER_PASS)
        # Проверка несовпадения паролей
        assert ER.PASS_ARE_DIFF == kc.emp_dash_auth_form.error_pass_are_diff(), "Wrong error-text or not found"
        kc.emp_dash_auth_form.accept_pass_for_restore(B2B_PASS)
        got_emp_main_h1 = kc.emp_dash_main.employee_dashboard_h1_text()
        assert ER.EMP_DASH_H1 == got_emp_main_h1, f"Expected '{ER.EMP_DASH_H1}' but got '{got_emp_main_h1}'"
