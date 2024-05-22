# TO DO: Тесты на права доступа(после добавления соответствующих дашбордов)
# TO DO: Тесты на редактирование пользователя(после добавления метода забора текста из полей)
import time
import allure
from data.test_data import ExpectedResults as ER, RegData, GenerateData

B2B_MAIL = RegData.B2B_MAIL
WRONG_MAIL = RegData.WRONG_MAIL
PHONE = GenerateData.PHONE
NAME = GenerateData.NAME
LAST_NAME = GenerateData.LAST_NAME
TIME_MAIL = GenerateData.TIME_MAIL
RANDOM_MAIL = GenerateData.RANDOM_MAIL


@allure.suite("Тесты страницы B2B сотрудников")
class TestB2BEmployees:

    @allure.title("Тест невозможности регистрации повторно на один телефон")
    def test_unique_phone(self, emp):
        expected_error = 'Сотрудник с таким Телефоном уже существует'
        name, last_name, mail, mail_1, phone = NAME, LAST_NAME, TIME_MAIL, RANDOM_MAIL, PHONE
        emp.cabinet_landing_page.open().login_all_env(emp)
        emp.cabinet_side_bar.click_b2b_employee()
        emp.b2b_employee_page.call_modal_menu().input_name(name).input_last_name(last_name).input_email(mail)
        emp.b2b_employee_page.input_phone(phone).set_sales_manager_role().set_full_access().click_add_employee()
        got_error = emp.b2b_employee_page.get_bubble_text()
        if expected_error == got_error:  # Проверка на первом этапе прогона, на случай имеющегося юзера с телефоном
            assert expected_error == got_error, f"Expected '{expected_error}' but got '{got_error}'"
        else:
            time.sleep(5)  # ждём исчезание нотификейшена добавленного юзера
            emp.b2b_employee_page.call_modal_menu().input_name(name).input_last_name(last_name).input_email(mail_1)
            emp.b2b_employee_page.input_phone(phone).set_sales_manager_role().set_full_access().click_add_employee()
            got_error = emp.b2b_employee_page.get_bubble_text()
            # time.sleep(7)
            assert expected_error == got_error, f"Expected '{expected_error}' but got '{got_error}'"

    @allure.title("Тест невозможности регистрации повторно на один email")
    def test_unique_mail(self, emp):
        expected_error = 'Пользователь с таким email уже существует'
        name, last_name, mail = NAME, LAST_NAME, TIME_MAIL
        emp.cabinet_landing_page.open().login_all_env(emp)
        emp.cabinet_side_bar.click_b2b_employee()
        emp.b2b_employee_page.call_modal_menu().input_name(name).input_last_name(last_name).input_email(mail)
        emp.b2b_employee_page.set_sales_manager_role().set_full_access().click_add_employee()
        got_error = emp.b2b_employee_page.get_bubble_text()
        time.sleep(5)  # Таймер позволяет дождаться отображения страницы и выключения нотификейшена добавления юзера
        if expected_error == got_error:  # Проверка на первом этапе прогона, на случай имеющегося юзера с mail
            assert expected_error == got_error, f"Expected '{expected_error}' but got '{got_error}'"
        else:
            emp.b2b_employee_page.call_modal_menu().input_name(name).input_last_name(last_name).input_email(mail)
            emp.b2b_employee_page.set_sales_manager_role().set_full_access().click_add_employee()
            got_error = emp.b2b_employee_page.get_bubble_text()
            assert expected_error == got_error, f"Expected '{expected_error}' but got '{got_error}'"

    @allure.title("Тест добавления/удаления юзера + отправка соответствующих писем")
    def test_add_and_delete_user(self, emp):
        mail_theme_added_user = 'Вам открыт доступ к Точке Движения'
        mail_theme_deleted_user = 'Ваша учетная запись удалена'
        name, last_name, mail = NAME, LAST_NAME, RANDOM_MAIL
        emp.cabinet_landing_page.open().login_all_env(emp)
        emp.cabinet_side_bar.click_b2b_employee()
        emp.b2b_employee_page.call_modal_menu().input_name(name).input_last_name(last_name).input_email(mail)
        emp.b2b_employee_page.set_sales_manager_role().set_full_access().click_add_employee()
        emp.driver.execute_script("window.open('', '_blank');")
        # Переключение контекста на вторую вкладку
        emp.driver.switch_to.window(emp.driver.window_handles[1])
        emp.mailpit_page.open().find_by_client(mail)
        except_theme = emp.mailpit_page.mail_theme_text(emp.driver)
        assert mail_theme_added_user == except_theme, f"Expected '{mail_theme_added_user}' but got '{except_theme}'"
        emp.driver.switch_to.window(emp.driver.window_handles[0])
        emp.tables_steps.find_entity(mail)
        emp.b2b_employee_page.delete_employee().accept_delete_employee()
        time.sleep(1)
        emp.driver.refresh()
        check_delete = emp.tables_steps.count_find_entity(mail)
        assert check_delete == 0, f'Пользователь {mail} не удален'
        # Переключение контекста на вторую вкладку
        emp.driver.switch_to.window(emp.driver.window_handles[1])
        emp.mailpit_page.open().find_by_client(mail)
        except_theme = emp.mailpit_page.mail_theme_text(emp.driver)
        assert mail_theme_deleted_user == except_theme, f"Expected '{mail_theme_deleted_user}' but got '{except_theme}'"

    @allure.title("Тест на валидацию пустых полей модалки")
    def test_check_empty_inputs(self, emp):
        exception = 5  # 5 - количество полей на валидацию пустого поля
        emp.cabinet_landing_page.open().login_all_env(emp)
        emp.cabinet_side_bar.click_b2b_employee()
        emp.b2b_employee_page.call_modal_menu()
        emp.b2b_employee_page.click_add_employee()
        error_count = emp.b2b_employee_page.count_error_empty_massage_clients()
        assert error_count == exception, f"Ожидалось {exception} сообщений, но найдено {error_count}"

    @allure.title("Тест валидации пустого чекбокса")
    def test_check_empty_checkbox(self, emp):
        exception_error = "Необходимо выбрать хотя бы одну опцию"
        emp.cabinet_landing_page.open().login_all_env(emp)
        emp.cabinet_side_bar.click_b2b_employee()
        emp.b2b_employee_page.call_modal_menu()
        emp.b2b_employee_page.set_chose_access()
        emp.b2b_employee_page.click_add_employee()
        checkbox_error = emp.b2b_employee_page.error_checkbox_massage()
        assert exception_error == checkbox_error, f"Ожидалось {exception_error} сообщений, но найдено {checkbox_error}"

    @allure.title("Тест проверки валидации поля email")
    def test_check_wrong_mail_validation(self, emp):
        # mail_error = "Поле Почта должно быть действительным электронным адресом."
        emp.cabinet_landing_page.open().login_all_env(emp)
        emp.cabinet_side_bar.click_b2b_employee()
        emp.b2b_employee_page.call_modal_menu()
        emp.b2b_employee_page.set_chose_access()
        emp.b2b_employee_page.click_add_employee()
        emp.b2b_employee_page.input_email(WRONG_MAIL)
        emp.b2b_employee_page.click_add_employee()
        time.sleep(1)
        mail_text = emp.b2b_employee_page.error_mail_massage()
        assert ER.MAIL_VALIDATION_PROFILE_CAB == mail_text, (f"Ожидалось {ER.MAIL_VALIDATION_PROFILE_CAB},"
                                                             f" но найдено {mail_text}")

    @allure.title("Уборка тестовых юзеров после тестов")
    def test_delete_all_test_users(self, emp):
        emp.cabinet_landing_page.open().login_all_env(emp)
        emp.cabinet_side_bar.click_b2b_employee()
        while True:
            emp.tables_steps.find_test_employee("ИмяТест")
            try:
                emp.b2b_employee_page.delete_employee().accept_delete_employee()
                time.sleep(2)
                emp.driver.refresh()
            except:
                return False
