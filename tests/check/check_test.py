#TO DO: Тесты на права доступа, после добавления соответствующих дашбордов
import configparser
import time
import allure
import datetime


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
now = datetime.datetime.now()
time_1 = str(now).split(' ')
time_1 = '-'.join(time_1)
test_time = time_1[:-7:].replace(':','.')
NAME = f"ИмяТест{test_time}"
LAST_NAME = f"ФамилияТест{test_time}"
MAIL = f'test{test_time}@mail.ru'


class TestCheck:
    @allure.title("Тест добавления юзера")
    def test_check_cab(self, pages, steps):
        pages.cabinet_landing_page.open().login_all_env(pages)  # Авторизация пользователя в КУ
        # steps.tables_steps.find_option('Обучение')# раскоментировать для работы с опцией
        # time.sleep(5)
        pages.cabinet_side_bar.click_b2b_employee()#переход на страницу сотрудников
        # steps.tables_steps.find_option('ИмяТест2024-02-04-20.27.04')# юзер сверху страницы
        # steps.tables_steps.find_option('ИмяТест2024-01-30-17.33.53')# юзер снизу страницы
        steps.tables_steps.find_entity('ИмяТест2024-02-04-20.16.37')# юзер на 3ьей странице


    @allure.title("Тест добавления юзера")
    def test_check_control_panel(self, driver, pages, steps):
        pages.cp_auth_form.open().login(EMAIL, USER_PASS) # авторизация в ПУ DEV окружение
        steps.common_steps.find_elem('test2')# Поиск опции на 2ой странице, клик и перебор работает
        # pages.side_bar_cp.click_users()


    """

    @allure.title("Тест добавления юзера")
    def test_add_and_delete_user(self, driver, pages, steps):
        # mail_error = "Поле Почта должно быть действительным электронным адресом."
        mail_theme_added_user = 'Вам открыт доступ к Точке Движения'
        name, last_name, mail = NAME, LAST_NAME, MAIL
        # pages.cp_auth_form.open().login(EMAIL, USER_PASS) # авторизация в ПУ DEV окружение
        pages.cabinet_landing_page.open().login_all_env(pages) # Авторизация пользователя в КУ
        # pages.side_bar_cp.click_users()
        time.sleep(1)
        pages.cabinet_side_bar.click_b2b_employee()
        steps.common_steps.find_elem('ИмяТест2024-01-30-17.23.30') # поиск опции в ПУ на 2ой странице, работает
        # steps.tables_steps.find_option('ИмяТест2024-01-30-17.23.30')
        # steps.tables_steps.find_option('WARRANTYWITH') не работает с опциями в ПУ
        # pages.cabinet_side_bar.click_b2b_employee()
        # time.sleep(1)
        # steps.tables_steps.find_option('ФамилияТест2024-01-30-17.33.53')
        time.sleep(10)
        # pages.b2b_employee_page.call_modal_menu()
        # pages.b2b_employee_page.input_name(name)
        # pages.b2b_employee_page.input_last_name(last_name)
        # pages.b2b_employee_page.input_email(mail)
        # pages.b2b_employee_page.set_sales_manager_role()
        # pages.b2b_employee_page.set_full_access()
        # pages.b2b_employee_page.click_add_employee()
        # driver.execute_script("window.open('', '_blank');")
        # # Переключение контекста на вторую вкладку
        # driver.switch_to.window(driver.window_handles[1])
        # pages.mailpit_page.open().find_by_client(mail)
        # time.sleep(5)
        # except_theme = pages.mailpit_page.mail_theme_text(driver)
        # assert mail_theme_added_user == except_theme, f"Expected '{mail_theme_added_user}' but got '{except_theme}'"
        # driver.switch_to.window(driver.window_handles[0])
        # time.sleep(5)
        # steps.tables_steps.find_elem(name)
        # pages.b2b_employee_page.delete_employee()
        # time.sleep(2)
        # pages.b2b_employee_page.accept_delete_employee()
        # time.sleep(6)
        # assert steps.tables_steps.find_elem(name) == False, f'Пользователь {name} не удален'
        # time.sleep(10)

    @allure.title("Тест на валидацию пустых полей модалки")
    def test_check_empty_inputs(self, pages):
        exception = 5  # 5 - количество полей на валидацию пустого поля
        pages.cabinet_landing_page.open().login_all_env(pages)
        pages.cabinet_side_bar.click_b2b_employee()
        pages.b2b_employee_page.call_modal_menu()
        pages.b2b_employee_page.click_add_employee()
        error_count = pages.b2b_employee_page.count_error_empty_massage_clients()
        assert error_count == exception, f"Ожидалось {exception} сообщений, но найдено {error_count}"


    @allure.title("Тест валидации пустого чекбокса")
    def test_check_empty_checkbox(self, pages):
        exception_error = "Необходимо выбрать хотя бы одну опцию"
        pages.cabinet_landing_page.open().login_all_env(pages)
        pages.cabinet_side_bar.click_b2b_employee()
        pages.b2b_employee_page.call_modal_menu()
        pages.b2b_employee_page.set_chose_access()
        pages.b2b_employee_page.click_add_employee()
        checkbox_error = pages.b2b_employee_page.error_checkbox_massage()
        assert exception_error == checkbox_error, f"Ожидалось {exception_error} сообщений, но найдено {checkbox_error}"

    @allure.title("Блок тестов проверки")
    def test_check_wrong_mail_validation(self, pages):
        mail_error = "Поле Почта должно быть действительным электронным адресом."
        pages.cabinet_landing_page.open().login_all_env(pages)
        pages.cabinet_side_bar.click_b2b_employee()
        pages.b2b_employee_page.call_modal_menu()
        pages.b2b_employee_page.set_chose_access()
        pages.b2b_employee_page.click_add_employee()
        pages.b2b_employee_page.input_email(WRONG_MAIL)
        pages.b2b_employee_page.click_add_employee()
        time.sleep(1)
        mail_text = pages.b2b_employee_page.error_mail_massage()
        assert mail_error == mail_text, f"Ожидалось {mail_error} , но найдено {mail_text}"
    """


