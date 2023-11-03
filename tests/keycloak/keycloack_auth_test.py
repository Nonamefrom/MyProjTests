import configparser
import time
import allure


config = configparser.ConfigParser()
config.read('ini_config/config.ini')


EMAIL = config.get('credentials', 'EMAIL')
INTERNAL_MAIL = config.get('credentials', 'INTERNAL_MAIL')
INTERNAL_PASS = config.get('credentials', 'INTERNAL_PASS')
B2B_MAIL = config.get('credentials', 'B2B_MAIL')
B2B_PASS = config.get('credentials', 'B2B_PASS')
WRONG_MAIL = config.get('credentials', 'WRONG_MAIL')
WRONG_USER_PASS = config.get('credentials', 'WRONG_USER_PASS')
USER_PASS = config.get('credentials', 'USER_PASS')
ERROR_LOGIN_TEXT = config.get('expected_results', 'ERROR_TEXT')
ERROR_PASS_TEXT = config.get('expected_results', 'PASS_ARE_DIFF')
SB_H1_TEXT = config.get('expected_results', 'SERVICE_BOOKING_H1')
CP_H1_TEXT = config.get('expected_results', 'CONTROL_PANEL_H1')
B2B_H1_TEXT = config.get('expected_results', 'SERVICE_BOOKING_H1')
INTERNAL_H1_TEXT = config.get('expected_results', 'SERVICE_BOOKING_H1')
PWZ_H1_TEXT = config.get('expected_results', 'PWZ_H1')
EMP_DASH_H1_TEXT = config.get('expected_results', 'EMP_DASH_H1')


@allure.suite("Тесты авторизации")
@allure.sub_suite("Набор тестов авторизации Панели Управления")
class TestLoginControlPanel:
    @allure.title("Запрет авторизации сущест. пользователя с неправильным паролем ПУ")
    def test_login_wrong_pass(self, pages):
        pages.cp_auth_form.open().login(EMAIL, WRONG_USER_PASS)
        got_error = pages.cp_auth_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Запрет авторизации НЕсущест. пользователя с правильным паролем ПУ")
    def test_login_wrong_mail(self, pages):
        pages.cp_auth_form.open().login(WRONG_MAIL, USER_PASS)
        got_error = pages.cp_auth_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Авторизация корректного пользователя ПУ")
    def test_login_correct_user(self, pages):
        pages.cp_auth_form.open().login(EMAIL, USER_PASS)
        got_cp_h1 = pages.cp_main.cp_h1_text()
        assert CP_H1_TEXT == got_cp_h1, f"Expected '{CP_H1_TEXT}' but got '{got_cp_h1}'"
        pages.top_bar.click_open_profile_dropdown().click_deauth_button()
        got_title = pages.cp_auth_form.auth_h1_text()
        assert 'Вход для операторов' == got_title, f"Expected 'Вход для операторов' but got '{got_title}'"

    @allure.title("Восстановление почты пользователя + Кейс несовпадения вводимых новых паролей ПУ")
    def test_recovery_mail(self, driver, pages):
        pages.cp_auth_form.open().click_forgot_pass()
        pages.cp_auth_form.input_recovery_mail(INTERNAL_MAIL)
        driver.execute_script("window.open('', '_blank');")
        # Переключение контекста на вторую вкладку
        driver.switch_to.window(driver.window_handles[1])
        pages.mailpit_page.open().find_by_client(INTERNAL_MAIL).click_restore_url(driver)
        # Переключение контекста на третью вкладку
        driver.switch_to.window(driver.window_handles[2])
        pages.cp_auth_form.input_different_pass(INTERNAL_PASS, WRONG_USER_PASS)
        # Проверка несовпадения паролей
        got_error_text = pages.cp_auth_form.error_pass_are_diff()
        assert ERROR_PASS_TEXT == got_error_text, f"Expected '{ERROR_PASS_TEXT}' but got '{got_error_text}'"
        pages.cp_auth_form.accept_pass_for_restore(INTERNAL_PASS)
        got_cp_h1 = pages.cp_main.cp_h1_text()
        assert CP_H1_TEXT == got_cp_h1, f"Expected '{CP_H1_TEXT}' but got '{got_cp_h1}'"


@allure.sub_suite("Набор тестов авторизации Онлайн Записи")
class TestLoginServiceBooking:
    @allure.title("Запрет авторизации сущест. b2b пользователя с неправильным паролем ОЗ")
    def test_sb_login_b2b_wrong_pass(self, pages):
        pages.sb_auth_form.open().go_to_login("b2b").login(EMAIL, WRONG_USER_PASS)
        got_error = pages.sb_auth_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Запрет авторизации НЕсущест. b2b пользователя с правильным паролем ОЗ")
    def test_sb_login_b2b_wrong_mail(self, pages):
        pages.sb_auth_form.open().go_to_login("b2b").login(WRONG_MAIL, USER_PASS)
        got_error = pages.sb_auth_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Запрет авторизации b2b в internal realm ОЗ")
    def test_sb_login_b2b_like_internal(self, pages):
        pages.sb_auth_form.open().go_to_login("internal").login(B2B_MAIL, B2B_PASS)
        got_error = pages.sb_auth_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Авторизация корректного b2b пользователя ОЗ")
    def test_sb_login_correct_b2b_user(self, pages):
        pages.sb_auth_form.open().go_to_login("b2b").login(B2B_MAIL, B2B_PASS)
        got_sb_main_h1 = pages.sb_main.sb_h1_text()
        assert SB_H1_TEXT == got_sb_main_h1, f"Expected '{SB_H1_TEXT}' but got '{got_sb_main_h1}'"
        pages.top_bar.click_open_profile_dropdown().click_deauth_button()
        time.sleep(1)
        assert pages.sb_auth_form.check_b2b_internal_buttons() is True, "Кнопки b2b/internal авторизации не найдены"

    @allure.title("Авторизация корректного internal пользователя ОЗ")
    def test_sb_login_correct_internal_user(self, pages):
        pages.sb_auth_form.open().go_to_login("internal").login(INTERNAL_MAIL, INTERNAL_PASS)
        got_sb_main_h1 = pages.sb_main.sb_h1_text()
        assert SB_H1_TEXT == got_sb_main_h1, f"Expected '{SB_H1_TEXT}' but got '{got_sb_main_h1}'"
        pages.top_bar.click_open_profile_dropdown().click_deauth_button()
        time.sleep(1)
        assert pages.sb_auth_form.check_b2b_internal_buttons() is True, "Кнопки b2b/internal авторизации не найдены"

    @allure.title("Восстановление почты пользователя + Кейс несовпадения вводимых новых паролей ОЗ")
    def test_recovery_mail_sb(self, driver, pages):
        pages.sb_auth_form.open().go_to_login("internal").click_forgot_pass()
        pages.sb_auth_form.input_recovery_mail(INTERNAL_MAIL)
        driver.execute_script("window.open('', '_blank');")
        # Переключение контекста на вторую вкладку
        driver.switch_to.window(driver.window_handles[1])
        pages.mailpit_page.open().find_by_client(INTERNAL_MAIL).click_restore_url(driver)
        # Переключение контекста на третью вкладку
        driver.switch_to.window(driver.window_handles[2])
        pages.sb_auth_form.input_different_pass(INTERNAL_PASS, WRONG_USER_PASS)
        # Проверка несовпадения паролей
        assert ERROR_PASS_TEXT == pages.sb_auth_form.error_pass_are_diff(), "Wrong error-text or not found"
        pages.sb_auth_form.accept_pass_for_restore(INTERNAL_PASS)
        got_sb_h1 = pages.sb_main.sb_h1_text()
        assert SB_H1_TEXT == got_sb_h1, f"Expected '{SB_H1_TEXT}' but got '{got_sb_h1}'"


@allure.sub_suite("Набор тестов авторизации Пункта выдачи заказов")
class TestLoginPWZ:
    @allure.title("Запрет авторизации сущест. пользователя с неправильным паролем ПВЗ")
    def test_pwz_login_wrong_pass(self, pages):
        pages.auth_pwz_form.open().go_to_login("internal").login(EMAIL, WRONG_USER_PASS)
        got_error = pages.auth_pwz_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Запрет авторизации НЕсущест. b2b пользователя с правильным паролем ПВЗ")
    def test_pwz_login_b2b_wrong_mail(self, pages):
        pages.auth_pwz_form.open().go_to_login("b2b").login(WRONG_MAIL, USER_PASS)
        got_error = pages.auth_pwz_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Запрет авторизации b2b в internal realm ПВЗ")
    def test_pwz_login_b2b_like_internal(self, pages):
        pages.auth_pwz_form.open().go_to_login("internal").login(B2B_MAIL, B2B_PASS)
        got_error = pages.auth_pwz_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Авторизация корректного b2b пользователя ПВЗ")
    def test_pwz_login_correct_b2b_user(self, pages):
        pages.auth_pwz_form.open().go_to_login("b2b").login(B2B_MAIL, B2B_PASS)
        got_pwz_h1 = pages.pwz_main.pwz_h1_text()
        assert PWZ_H1_TEXT == got_pwz_h1, f"Expected '{PWZ_H1_TEXT}' but got '{got_pwz_h1}'"
        pages.top_bar.click_open_profile_dropdown().click_deauth_button()
        time.sleep(1)
        assert pages.auth_pwz_form.check_b2b_internal_buttons() is True, "Кнопки b2b/internal авторизации не найдены"

    @allure.title("Авторизация корректного internal пользователя ПВЗ")
    def test_pwz_login_correct_internal_user(self, pages):
        pages.auth_pwz_form.open().go_to_login("internal").login(INTERNAL_MAIL, INTERNAL_PASS)
        got_pwz_h1 = pages.pwz_main.pwz_h1_text()
        assert PWZ_H1_TEXT == got_pwz_h1, f"Expected '{PWZ_H1_TEXT}' but got '{got_pwz_h1}'"
        pages.top_bar.click_open_profile_dropdown().click_deauth_button()
        time.sleep(1)
        assert pages.auth_pwz_form.check_b2b_internal_buttons() is True, "Кнопки b2b/internal авторизации не найдены"

    @allure.title("Восстановление почты пользователя + Кейс несовпадения вводимых новых паролей ПВЗ")
    def test_recovery_mail_pwz(self, driver, pages):
        pages.auth_pwz_form.open().go_to_login("internal").click_forgot_pass()
        pages.auth_pwz_form.input_recovery_mail(INTERNAL_MAIL)
        driver.execute_script("window.open('', '_blank');")
        # Переключение контекста на вторую вкладку
        driver.switch_to.window(driver.window_handles[1])
        pages.mailpit_page.open().find_by_client(INTERNAL_MAIL).click_restore_url(driver)
        # Переключение контекста на третью вкладку
        driver.switch_to.window(driver.window_handles[2])
        pages.auth_pwz_form.input_different_pass(INTERNAL_PASS, WRONG_USER_PASS)
        # Проверка несовпадения паролей
        assert ERROR_PASS_TEXT == pages.auth_pwz_form.error_pass_are_diff(), "Wrong error-text or not found"
        pages.auth_pwz_form.accept_pass_for_restore(INTERNAL_PASS)
        got_pwz_h1 = pages.pwz_main.pwz_h1_text()
        assert PWZ_H1_TEXT == got_pwz_h1, f"Expected '{PWZ_H1_TEXT}' but got '{got_pwz_h1}'"


@allure.sub_suite("Набор тестов авторизации Дашборда сотрудника")
class TestLoginEmployeeDashboard:
    @allure.title("Запрет авторизации сущест. пользователя EMPDASH с неправильным паролем Employee Dashboard")
    def test_employee_dash_login_wrong_pass(self, pages):
        pages.emp_dash_auth_form.open().login(B2B_MAIL, WRONG_USER_PASS)
        got_error = pages.emp_dash_auth_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Запрет авторизации НЕсущест. b2b пользователя EMPDASH с правильным паролем Employee Dashboard")
    def test_employee_dash_login_b2b_wrong_mail(self, pages):
        pages.emp_dash_auth_form.open().login(WRONG_MAIL, B2B_PASS)
        got_error = pages.emp_dash_auth_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Запрет авторизации internal в b2b realm Employee Dashboard")
    def test_employee_dash_login_b2b_like_internal(self, pages):
        pages.emp_dash_auth_form.open().login(INTERNAL_MAIL, INTERNAL_PASS)
        got_error = pages.emp_dash_auth_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Авторизация корректного b2b пользователя Employee Dashboard")
    def test_employee_dash_login_correct_b2b_user(self, pages):
        pages.emp_dash_auth_form.open().login(B2B_MAIL, B2B_PASS)
        got_emp_dash_h1 = pages.emp_dash_main.employee_dashboard_h1_text()
        assert EMP_DASH_H1_TEXT == got_emp_dash_h1, f"Expected '{EMP_DASH_H1_TEXT}' but got '{got_emp_dash_h1}'"
        pages.top_bar.click_open_profile_dropdown().click_deauth_button()
        time.sleep(1)
        got_title = pages.emp_dash_auth_form.auth_h1_text()
        assert 'Вход' == got_title, f"Expected 'Вход' but got '{got_title}'"

    @allure.title("Восстановление почты пользователя + Кейс несовпадения вводимых новых паролей Employee Dashboard")
    def test_recovery_mail_employee_dash(self, driver, pages):
        pages.emp_dash_auth_form.open().click_forgot_pass()
        pages.emp_dash_auth_form.input_recovery_mail(B2B_MAIL)
        driver.execute_script("window.open('', '_blank');")
        # Переключение контекста на вторую вкладку
        driver.switch_to.window(driver.window_handles[1])
        pages.mailpit_page.open().find_by_client(B2B_MAIL).click_restore_url(driver)
        # Переключение контекста на третью вкладку
        driver.switch_to.window(driver.window_handles[2])
        pages.emp_dash_auth_form.input_different_pass(B2B_PASS, WRONG_USER_PASS)
        # Проверка несовпадения паролей
        assert ERROR_PASS_TEXT == pages.emp_dash_auth_form.error_pass_are_diff(), "Wrong error-text or not found"
        pages.emp_dash_auth_form.accept_pass_for_restore(B2B_PASS)
        got_emp_main_h1 = pages.emp_dash_main.employee_dashboard_h1_text()
        assert EMP_DASH_H1_TEXT == got_emp_main_h1, f"Expected '{EMP_DASH_H1_TEXT}' but got '{got_emp_main_h1}'"
