import time
import allure

import data.test_data
from data.test_data import RegData
from data.test_data import ExpectedResults as ER


@allure.suite("Тесты ПУ")
@allure.sub_suite("Тесты страницы Добавления пользователей ПУ")
class TestAdminRights:
    @allure.title("Проверка отсутствия возможности нажать кнопку Синхронизации с Парусом в ПУ у Админа")
    def test_(self, cp, data_cp_superadmin):
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        name = data.test_data.GenerateData.NAME
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar.click_users()
        time.sleep(1)
        check = cp.internal_page.get_h1_internal_user_page()
        assert check == data.test_data.ExpectedResults.CP_INTERNAL_PAGE_H1, \
            f"Expected {data.test_data.ExpectedResults.CP_INTERNAL_PAGE_H1}, but got {check}"
        cp.internal_page.call_modal_menu().input_name(name)
        cp.internal_page.save_internal()

    #
    # @allure.title("Проверка возможности нажать кнопку Синхронизации с Парусом в ПУ у СуперАдмина")
    # def test_super_admin_sync_button_is_active(self, cp, data_cp_superadmin):
    #     username, password = data_cp_superadmin[1], data_cp_superadmin[2]
    #     cp.cp_auth_form.open().login(username, password)
    #     cp.common_steps.find_elem('ПВЗ')
    #     cp.admin.admin_tab()
    #     # assert cp.admin.sync_button_status() is True
    #     assert cp.admin.sync_button_class() is True
    #     cp.top_bar.click_open_profile_dropdown().click_deauth_button()
    #
    # @allure.title("Проверка отображение кнопки 'Добавить' у СуперАдмина")
    # def test_check_add_button_super_admin(self, cp, data_cp_superadmin):
    #     username, password = data_cp_superadmin[1], data_cp_superadmin[2]
    #     cp.cp_auth_form.open().login(username, password)
    #     cp.side_bar.click_users()
    #     check = cp.internal_page.check_add_button()
    #     assert check is True, "Кнопка 'Добавить' не отображается"
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
