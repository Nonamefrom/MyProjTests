#TO DO: Тесты на права доступа(после добавления соответствующих дашбордов)
#TO DO: Тесты на редактирование пользователя(после добавления метода забора текста из полей)
import time
import allure
from data.test_data import ExpectedResults, RegData, GenerateData


B2B_MAIL = RegData.B2B_MAIL
WRONG_MAIL = RegData.WRONG_MAIL
MAIL_VALIDATION = ExpectedResults.MAIL_VALIDATION_PROFILE_CAB
PHONE = GenerateData.PHONE
NAME = GenerateData.NAME
LAST_NAME = GenerateData.LAST_NAME
MAIL = GenerateData.MAIL


@allure.suite("Тесты страницы B2B сотрудников")
class TestB2BEmployees:

    @allure.title("Тест невозможности регистрации повторно на один email")
    def test_add_and_delete_user(self, pages):
        expected_error = 'Сотрудник с таким Телефоном уже существует'
        name, last_name, mail, mail_1, phone = NAME, LAST_NAME, MAIL, B2B_MAIL, PHONE
        pages.cabinet_landing_page.open().login_all_env(pages)
        pages.cabinet_side_bar.click_b2b_employee()
        pages.b2b_employee_page.call_modal_menu().input_name(name).input_last_name(last_name).input_email(mail)
        pages.b2b_employee_page.input_phone(phone).set_sales_manager_role().set_full_access().click_add_employee()
        got_error = pages.b2b_employee_page.get_bubble_text()
        time.sleep(2)  # Таймер позволяет дождатся отображения страницы и выключения бабла добавленного юзера
        if expected_error == got_error:# Проверка на первом этапе прогона,на случай имеющегося юзера с телефоном
            assert expected_error == got_error, f"Expected '{expected_error}' but got '{got_error}'"
        else:
            pages.b2b_employee_page.call_modal_menu().input_name(name).input_last_name(last_name).input_email(mail_1)
            pages.b2b_employee_page.input_phone(phone).set_sales_manager_role().set_full_access().click_add_employee()
            got_error = pages.b2b_employee_page.get_bubble_text()
            assert expected_error == got_error, f"Expected '{expected_error}' but got '{got_error}'"


    @allure.title("Тест невозможности регистрации повторно на один email")
    def test_add_and_delete_user(self, pages):
        expected_error = 'Пользователь с таким email уже существует'
        name, last_name, mail = NAME, LAST_NAME, MAIL
        pages.cabinet_landing_page.open().login_all_env(pages)
        pages.cabinet_side_bar.click_b2b_employee()
        pages.b2b_employee_page.call_modal_menu().input_name(name).input_last_name(last_name).input_email(mail)
        pages.b2b_employee_page.set_sales_manager_role().set_full_access().click_add_employee()
        got_error = pages.b2b_employee_page.get_bubble_text()
        time.sleep(2)# Таймер позволяет дождатся отображения страницы и выключения бабла добавленного юзера
        if expected_error == got_error:# Проверка на первом этапе прогона,на случай имеющегося юзера с mail
            assert expected_error == got_error, f"Expected '{expected_error}' but got '{got_error}'"
        pages.b2b_employee_page.call_modal_menu().input_name(name).input_last_name(last_name).input_email(mail)
        pages.b2b_employee_page.set_sales_manager_role().set_full_access().click_add_employee()
        got_error = pages.b2b_employee_page.get_bubble_text()
        assert expected_error == got_error, f"Expected '{expected_error}' but got '{got_error}'"

    @allure.title("Тест добавления/удаления юзера + отправка соответствующих писем")
    def test_add_and_delete_user(self, driver, pages, steps):
        mail_theme_added_user = 'Вам открыт доступ к Точке Движения'
        mail_theme_deleted_user = 'Ваша учетная запись удалена'
        name, last_name, mail = NAME, LAST_NAME, MAIL
        pages.cabinet_landing_page.open().login_all_env(pages)
        pages.cabinet_side_bar.click_b2b_employee()
        pages.b2b_employee_page.call_modal_menu().input_name(name).input_last_name(last_name).input_email(mail)
        pages.b2b_employee_page.set_sales_manager_role().set_full_access().click_add_employee()
        driver.execute_script("window.open('', '_blank');")
        # Переключение контекста на вторую вкладку
        driver.switch_to.window(driver.window_handles[1])
        pages.mailpit_page.open().find_by_client(mail)
        except_theme = pages.mailpit_page.mail_theme_text(driver)
        assert mail_theme_added_user == except_theme, f"Expected '{mail_theme_added_user}' but got '{except_theme}'"
        driver.switch_to.window(driver.window_handles[0])
        steps.tables_steps.find_entity(name)
        pages.b2b_employee_page.delete_employee().accept_delete_employee()
        time.sleep(2)
        check_delete = steps.tables_steps.count_find_entity(name)
        assert check_delete == 0, f'Пользователь {name} не удален'
        # Переключение контекста на вторую вкладку
        driver.switch_to.window(driver.window_handles[1])
        pages.mailpit_page.open().find_by_client(mail)
        except_theme = pages.mailpit_page.mail_theme_text(driver)
        assert mail_theme_deleted_user == except_theme, f"Expected '{mail_theme_deleted_user}' but got '{except_theme}'"


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

    @allure.title("Тест проверки валидации поля email")
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
        assert MAIL_VALIDATION == mail_text, f"Ожидалось {MAIL_VALIDATION} , но найдено {mail_text}"
