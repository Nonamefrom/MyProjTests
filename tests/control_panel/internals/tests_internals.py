# Страница в разработке, будет доработана
import time
import allure

import data.test_data
from data.test_data import RegData
from data.test_data import GenerateData, ExpectedResults as ER

gen_data = GenerateData()

@allure.suite("Тесты ПУ")
@allure.sub_suite("Тесты страницы Добавления пользователей ПУ")
class TestAdminRights:
    @allure.title("Проверка отсутствия возможности нажать кнопку Синхронизации с Парусом в ПУ у Админа")
    def test_(self, cp, data_cp_superadmin):
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        name = gen_data.name
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar.click_users()
        time.sleep(1)
        check = cp.internal_page.get_h1_internal_user_page()
        assert check == data.test_data.ExpectedResults.CP_INTERNAL_PAGE_H1, \
            f"Expected {data.test_data.ExpectedResults.CP_INTERNAL_PAGE_H1}, but got {check}"
        cp.internal_page.call_modal_menu().input_name(name)
        cp.internal_page.save_internal()
        time.sleep(5)


    @allure.title("Проверка невозможности авторизоватся незарегистрированным юзером")
    def test_not_auth_unregistered_user(self, cp):
        username, password = RegData.EMAIL, RegData.WRONG_USER_PASS
        cp.cp_auth_form.open().login(username, password)
        got_error = cp.cp_auth_form.error_message()
        assert ER.ERROR_TEXT == got_error, f"Expected '{ER.ERROR_TEXT}' but got '{got_error}'"



    @allure.title("Проверка добавление сотрудника")
    def test_add_internal_and_check_letter(self, cp, data_cp_superadmin):
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        internal_name, internal_lastname, internal_mail = (gen_data.name,
                                                           GenerateData.LAST_NAME,
                                                           GenerateData.TIME_SVR_MAIL)
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar.click_users()
        time.sleep(1)
        check = cp.internal_page.get_h1_internal_user_page()
        assert check == data.test_data.ExpectedResults.CP_INTERNAL_PAGE_H1, \
            f"Expected {data.test_data.ExpectedResults.CP_INTERNAL_PAGE_H1}, but got {check}"
        cp.internal_page.call_modal_menu()
        cp.internal_page.add_internal(internal_name, internal_lastname, internal_mail)
        check_add_internal = cp.internal_page.get_h1_internal_user_page()
        assert check_add_internal == data.test_data.ExpectedResults.CP_INTERNAL_PAGE_H1, \
            f"Expected {data.test_data.ExpectedResults.CP_INTERNAL_PAGE_H1}, but got {check_add_internal}"
        time.sleep(5)



    #     cp.top_bar.click_open_profile_dropdown().click_deauth_button()
    #
    # @allure.title("Проверка не отображения кнопки 'Добавить' у не СуперАдмина")
    # def test_check_add_button_admin(self, cp, data_cp_admin):
    #     username, password = data_cp_admin[1], data_cp_admin[2]
    #     cp.cp_auth_form.open().login(username, password)
    #     cp.side_bar.click_users()
    #     check = cp.internal_page.check_add_button()
    #     assert check is False, "Кнопка 'Добавить' отображается"
    #     cp.top_bar.click_open_profile_dropdown().click_deauth_button()
    #
    #
