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
from pages.service_booking.service_booking_mainpage import ServiceBookingMainPage
from pages.pwz.pwz_mainpage import PWZMainPage
from pages.employee_dashboard.emp_dash_mainpage import EmpDashMainPage
from selenium.webdriver.common.action_chains import ActionChains



config = configparser.ConfigParser()
config.read('ini_config/config.ini')

CP_URL = f"{Env().cp_url}/auth/login"
SB_URL = f"{Env().sb_url}/"
PWZ_URL = f"{Env().pwz_url}/auth/login"
EMP_DASH_URL = f"{Env().emp_dash_url}/"
MAIL_PIT_URL = f"{Env().mailpit}/"
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
class TestLoginControlPanel():
    @allure.title("Запрет авторизации сущест. пользователя с неправильным паролем ПУ")
    def test_login_wrong_pass(self, driver):
        page = BasePage(driver, CP_URL)
        page.open()
        auth_form = KeycloackAuthForm(driver, url=CP_URL)
        auth_form.login(EMAIL, WRONG_USER_PASS)
        got_error = auth_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Запрет авторизации НЕсущест. пользователя с правильным паролем ПУ")
    def test_login_wrong_mail(self, driver):
        page = BasePage(driver, CP_URL)
        page.open()
        auth_form = KeycloackAuthForm(driver, url=CP_URL)
        auth_form.login(WRONG_MAIL, USER_PASS)
        got_error = auth_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Авторизация корректного пользователя ПУ")
    def test_login_correct_user(self, driver):
        page = BasePage(driver, CP_URL)
        page.open()
        auth_form = KeycloackAuthForm(driver, url=CP_URL)
        auth_form.login(EMAIL, USER_PASS)
        cp_main = AllOptionsCpPage(driver, url=CP_URL)
        got_cp_h1 = cp_main.cp_h1_text()
        assert CP_H1_TEXT == got_cp_h1, f"Expected '{CP_H1_TEXT}' but got '{got_cp_h1}'"
        top_bar = TopBarCpPage(driver, url=CP_URL)
        top_bar.click_open_profile_dropdown().click_deauth_button()
        got_title = auth_form.auth_h1_text()
        assert 'Вход для операторов' == got_title, f"Expected 'Вход для операторов' but got '{got_title}'"

    @allure.title("Восстановление почты пользователя + Кейс несовпадения вводимых новых паролей ПУ")
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
        got_error_text = auth_form.error_pass_are_diff()
        assert ERROR_PASS_TEXT == got_error_text, f"Expected '{ERROR_PASS_TEXT}' but got '{got_error_text}'"
        auth_form.accept_pass_for_restore(INTERNAL_PASS)
        cp_main = AllOptionsCpPage(driver, url=CP_URL)
        got_cp_h1 = cp_main.cp_h1_text()
        assert CP_H1_TEXT == got_cp_h1, f"Expected '{CP_H1_TEXT}' but got '{got_cp_h1}'"
@allure.sub_suite("Набор тестов авторизации Онлайн Записи")
class TestLoginServiceBooking():
    @allure.title("Запрет авторизации сущест. b2b пользователя с неправильным паролем ОЗ")
    def test_sb_login_b2b_wrong_pass(self, driver):
        page = BasePage(driver, SB_URL)
        page.open()
        sb_auth_form = KeycloackAuthForm(driver, url=SB_URL)
        sb_auth_form.go_to_login("b2b")
        sb_auth_form.login(EMAIL, WRONG_USER_PASS)
        got_error = sb_auth_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Запрет авторизации НЕсущест. b2b пользователя с правильным паролем ОЗ")
    def test_sb_login_b2b_wrong_mail(self, driver):
        page = BasePage(driver, SB_URL)
        page.open()
        sb_auth_form = KeycloackAuthForm(driver, url=SB_URL)
        sb_auth_form.go_to_login("b2b")
        sb_auth_form.login(WRONG_MAIL, USER_PASS)
        got_error = sb_auth_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Запрет авторизации b2b в internal realm ОЗ")
    def test_sb_login_b2b_like_internal(self, driver):
        page = BasePage(driver, SB_URL)
        page.open()
        sb_auth_form = KeycloackAuthForm(driver, url=SB_URL)
        sb_auth_form.go_to_login("internal")
        sb_auth_form.login(B2B_MAIL, B2B_PASS)
        got_error = sb_auth_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Авторизация корректного b2b пользователя ОЗ")
    def test_sb_login_correct_b2b_user(self, driver):
        page = BasePage(driver, SB_URL)
        page.open()
        sb_auth_form = KeycloackAuthForm(driver, url=SB_URL)
        sb_auth_form.go_to_login("b2b")
        sb_auth_form.login(B2B_MAIL, B2B_PASS)
        sb_main = ServiceBookingMainPage(driver, url=SB_URL)
        assert SB_H1_TEXT == sb_main.sb_h1_text(), f"Expected '{SB_H1_TEXT}' but got '{sb_main.sb_h1_text()}'"
        top_bar = TopBarCpPage(driver, url=SB_URL)
        top_bar.click_open_profile_dropdown().click_deauth_button()
        time.sleep(1)
        assert sb_auth_form.check_b2b_internal_buttons() is True, "Кнопки b2b/internal авторизации не найдены"

    @allure.title("Авторизация корректного internal пользователя ОЗ")
    def test_sb_login_correct_internal_user(self, driver):
        page = BasePage(driver, SB_URL)
        page.open()
        sb_auth_form = KeycloackAuthForm(driver, url=SB_URL)
        sb_auth_form.go_to_login("internal")
        sb_auth_form.login(INTERNAL_MAIL, INTERNAL_PASS)
        sb_main = ServiceBookingMainPage(driver, url=SB_URL)
        assert SB_H1_TEXT == sb_main.sb_h1_text(), f"Expected '{SB_H1_TEXT}' but got '{sb_main.sb_h1_text()}'"
        top_bar = TopBarCpPage(driver, url=SB_URL)
        top_bar.click_open_profile_dropdown().click_deauth_button()
        time.sleep(1)
        assert sb_auth_form.check_b2b_internal_buttons() is True, "Кнопки b2b/internal авторизации не найдены"

    @allure.title("Восстановление почты пользователя + Кейс несовпадения вводимых новых паролей ОЗ")
    def test_recovery_mail_sb(self, driver):
        page = BasePage(driver, SB_URL)
        page.open()
        sb_auth_form = KeycloackAuthForm(driver, url=SB_URL)
        sb_auth_form.go_to_login("internal")
        sb_auth_form.click_forgot_pass()
        sb_auth_form.input_recovery_mail(INTERNAL_MAIL)
        driver.execute_script("window.open('', '_blank');")
        # Переключение контекста на вторую вкладку
        driver.switch_to.window(driver.window_handles[1])
        mailpit_page = MailPitMain(driver, MAIL_PIT_URL)
        mailpit_page.open()
        mailpit_page.find_by_client(INTERNAL_MAIL)
        mailpit_page.click_restore_url(driver)
        # Переключение контекста на третью вкладку
        driver.switch_to.window(driver.window_handles[2])
        sb_auth_form.input_different_pass(INTERNAL_PASS, WRONG_USER_PASS)
        # Проверка несовпадения паролей
        assert ERROR_PASS_TEXT == sb_auth_form.error_pass_are_diff(), "Wrong error-text or not found"
        sb_auth_form.accept_pass_for_restore(INTERNAL_PASS)
        sb_main = ServiceBookingMainPage(driver, url=SB_URL)
        assert SB_H1_TEXT == sb_main.sb_h1_text(), f"Expected '{SB_H1_TEXT}' but got '{sb_main.sb_h1_text()}'"

@allure.sub_suite("Набор тестов авторизации Пункта выдачи заказов")
class TestLoginPWZ():
    @allure.title("Запрет авторизации сущест. пользователя с неправильным паролем ПВЗ")
    def test_pwz_login_wrong_pass(self, driver):
        page = BasePage(driver, PWZ_URL)
        page.open()
        auth_pwz_form = KeycloackAuthForm(driver, url=PWZ_URL)
        auth_pwz_form.go_to_login("internal")
        auth_pwz_form.login(EMAIL, WRONG_USER_PASS)
        got_error = auth_pwz_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Запрет авторизации НЕсущест. b2b пользователя с правильным паролем ПВЗ")
    def test_pwz_login_b2b_wrong_mail(self, driver):
        page = BasePage(driver, PWZ_URL)
        page.open()
        auth_pwz_form = KeycloackAuthForm(driver, url=PWZ_URL)
        auth_pwz_form.go_to_login("b2b")
        auth_pwz_form.login(WRONG_MAIL, USER_PASS)
        got_error = auth_pwz_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Запрет авторизации b2b в internal realm ПВЗ")
    def test_pwz_login_b2b_like_internal(self, driver):
        page = BasePage(driver, PWZ_URL)
        page.open()
        auth_pwz_form = KeycloackAuthForm(driver, url=PWZ_URL)
        auth_pwz_form.go_to_login("internal")
        auth_pwz_form.login(B2B_MAIL, B2B_PASS)
        got_error = auth_pwz_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Авторизация корректного b2b пользователя ПВЗ")
    def test_pwz_login_correct_b2b_user(self, driver):
        page = BasePage(driver, PWZ_URL)
        page.open()
        auth_pwz_form = KeycloackAuthForm(driver, url=PWZ_URL)
        auth_pwz_form.go_to_login("b2b")
        auth_pwz_form.login(B2B_MAIL, B2B_PASS)
        pwz_main = PWZMainPage(driver, url=PWZ_URL)
        assert PWZ_H1_TEXT == pwz_main.pwz_h1_text(), f"Expected '{PWZ_H1_TEXT}' but got '{pwz_main.pwz_h1_text()}'"
        top_bar = TopBarCpPage(driver, url=PWZ_URL)
        top_bar.click_open_profile_dropdown().click_deauth_button()
        time.sleep(1)
        assert auth_pwz_form.check_b2b_internal_buttons() is True, "Кнопки b2b/internal авторизации не найдены"

    @allure.title("Авторизация корректного internal пользователя ПВЗ")
    def test_pwz_login_correct_internal_user(self, driver):
        page = BasePage(driver, PWZ_URL)
        page.open()
        auth_pwz_form = KeycloackAuthForm(driver, url=PWZ_URL)
        auth_pwz_form.go_to_login("internal")
        auth_pwz_form.login(INTERNAL_MAIL, INTERNAL_PASS)
        pwz_main = PWZMainPage(driver, url=PWZ_URL)
        assert PWZ_H1_TEXT == pwz_main.pwz_h1_text(), f"Expected '{PWZ_H1_TEXT}' but got '{pwz_main.pwz_h1_text()}'"
        top_bar = TopBarCpPage(driver, url=PWZ_URL)
        top_bar.click_open_profile_dropdown().click_deauth_button()
        time.sleep(1)
        assert auth_pwz_form.check_b2b_internal_buttons() is True, "Кнопки b2b/internal авторизации не найдены"

    @allure.title("Восстановление почты пользователя + Кейс несовпадения вводимых новых паролей ПВЗ")
    def test_recovery_mail_pwz(self, driver):
        page = BasePage(driver, PWZ_URL)
        page.open()
        auth_pwz_form = KeycloackAuthForm(driver, url=PWZ_URL)
        auth_pwz_form.go_to_login("internal")
        auth_pwz_form.click_forgot_pass()
        auth_pwz_form.input_recovery_mail(INTERNAL_MAIL)
        driver.execute_script("window.open('', '_blank');")
        # Переключение контекста на вторую вкладку
        driver.switch_to.window(driver.window_handles[1])
        mailpit_page = MailPitMain(driver, MAIL_PIT_URL)
        mailpit_page.open()
        mailpit_page.find_by_client(INTERNAL_MAIL)
        mailpit_page.click_restore_url(driver)
        # Переключение контекста на третью вкладку
        driver.switch_to.window(driver.window_handles[2])
        auth_pwz_form.input_different_pass(INTERNAL_PASS, WRONG_USER_PASS)
        # Проверка несовпадения паролей
        assert ERROR_PASS_TEXT == auth_pwz_form.error_pass_are_diff(), "Wrong error-text or not found"
        auth_pwz_form.accept_pass_for_restore(INTERNAL_PASS)
        pwz_main = PWZMainPage(driver, url=PWZ_URL)
        assert PWZ_H1_TEXT == pwz_main.pwz_h1_text(), f"Expected '{PWZ_H1_TEXT}' but got '{pwz_main.pwz_h1_text()}'"

@allure.sub_suite("Набор тестов авторизации Дашборда сотрудника")
class TestLoginEmployeeDashboard():
    @allure.title("Запрет авторизации сущест. пользователя EMPDASH с неправильным паролем Employee Dashboard")
    def test_employee_dash_login_wrong_pass(self, driver):
        page = BasePage(driver, EMP_DASH_URL)
        page.open()
        auth_emp_dash_form = KeycloackAuthForm(driver, url=EMP_DASH_URL)
        auth_emp_dash_form.login(B2B_MAIL, WRONG_USER_PASS)
        got_error = auth_emp_dash_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Запрет авторизации НЕсущест. b2b пользователя EMPDASH с правильным паролем Employee Dashboard")
    def test_employee_dash_login_b2b_wrong_mail(self, driver):
        page = BasePage(driver, EMP_DASH_URL)
        page.open()
        auth_emp_dash_form = KeycloackAuthForm(driver, url=EMP_DASH_URL)
        auth_emp_dash_form.login(WRONG_MAIL, B2B_PASS)
        got_error = auth_emp_dash_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Запрет авторизации internal в b2b realm Employee Dashboard")
    def test_employee_dash_login_b2b_like_internal(self, driver):
        page = BasePage(driver, EMP_DASH_URL)
        page.open()
        auth_emp_dash_form = KeycloackAuthForm(driver, url=EMP_DASH_URL)
        auth_emp_dash_form.login(INTERNAL_MAIL, INTERNAL_PASS)
        got_error = auth_emp_dash_form.error_message()
        assert ERROR_LOGIN_TEXT == got_error, f"Expected '{ERROR_LOGIN_TEXT}' but got '{got_error}'"

    @allure.title("Авторизация корректного b2b пользователя Employee Dashboard")
    def test_employee_dash_login_correct_b2b_user(self, driver):
        page = BasePage(driver, EMP_DASH_URL)
        page.open()
        auth_emp_dash_form = KeycloackAuthForm(driver, url=EMP_DASH_URL)
        auth_emp_dash_form.login(B2B_MAIL, B2B_PASS)
        emp_dash_main = EmpDashMainPage(driver, url=EMP_DASH_URL)
        assert EMP_DASH_H1_TEXT == emp_dash_main.employee_dashboard_h1_text(), f"Expected '{EMP_DASH_H1_TEXT}' but got '{emp_dash_main.employee_dashboard_h1_text()}'"
        top_bar = TopBarCpPage(driver, url=EMP_DASH_URL)
        top_bar.click_open_profile_dropdown().click_deauth_button()
        time.sleep(1)
        got_title = auth_emp_dash_form.auth_h1_text()
        assert 'Вход' == got_title, f"Expected 'Вход' but got '{got_title}'"

    @allure.title("Восстановление почты пользователя + Кейс несовпадения вводимых новых паролей Employee Dashboard")
    def test_recovery_mail_employee_dash(self, driver):
        page = BasePage(driver, EMP_DASH_URL)
        page.open()
        auth_emp_dash_form = KeycloackAuthForm(driver, url=EMP_DASH_URL)
        auth_emp_dash_form.click_forgot_pass()
        auth_emp_dash_form.input_recovery_mail(B2B_MAIL)
        driver.execute_script("window.open('', '_blank');")
        # Переключение контекста на вторую вкладку
        driver.switch_to.window(driver.window_handles[1])
        mailpit_page = MailPitMain(driver, MAIL_PIT_URL)
        mailpit_page.open()
        mailpit_page.find_by_client(B2B_MAIL)
        mailpit_page.click_restore_url(driver)
        # Переключение контекста на третью вкладку
        driver.switch_to.window(driver.window_handles[2])
        auth_emp_dash_form.input_different_pass(B2B_PASS, WRONG_USER_PASS)
        # Проверка несовпадения паролей
        assert ERROR_PASS_TEXT == auth_emp_dash_form.error_pass_are_diff(), "Wrong error-text or not found"
        auth_emp_dash_form.accept_pass_for_restore(B2B_PASS)
        emp_dash_main = EmpDashMainPage(driver, url=EMP_DASH_URL)
        assert EMP_DASH_H1_TEXT == emp_dash_main.employee_dashboard_h1_text(), f"Expected '{EMP_DASH_H1_TEXT}' but got '{emp_dash_main.employee_dashboard_h1_text()}'"
