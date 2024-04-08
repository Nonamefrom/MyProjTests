import time
import allure
from data.test_data import ExpectedResults as ER


@allure.suite("Тесты ПУ")
@allure.sub_suite("Проверка разделения прав Админа и СуперАдмина")
class TestAdminRights:
    @allure.title("Проверка отсутствия возможности нажать кнопку Синхронизации с Парусом в ПУ у Админа")
    def test_admin_sync_button_is_disabled(self, cp, data_cp_admin):
        username, password = data_cp_admin[1], data_cp_admin[2]
        cp.cp_auth_form.open().login(username, password)
        cp.common_steps.find_elem('ПВЗ')
        cp.admin.admin_tab()
        check = cp.admin.sync_button_status()
        assert check is not True
        assert cp.admin.sync_button_class() is not True
        cp.top_bar_cp.click_open_profile_dropdown().click_deauth_button()

    @allure.title("Проверка возможности нажать кнопку Синхронизации с Парусом в ПУ у СуперАдмина")
    def test_super_admin_sync_button_is_active(self, cp, data_cp_superadmin):
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        cp.cp_auth_form.open().login(username, password)
        cp.common_steps.find_elem('ПВЗ')
        cp.admin.admin_tab()
        # assert cp.admin.sync_button_status() is True
        assert cp.admin.sync_button_class() is True
        cp.top_bar_cp.click_open_profile_dropdown().click_deauth_button()

    @allure.title("Проверка отображение кнопки 'Добавить' у СуперАдмина")
    def test_check_add_button_super_admin(self, cp, data_cp_superadmin):
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_users()
        check = cp.internal_page.check_add_button()
        assert check is True, "Кнопка 'Добавить' не отображается"
        cp.top_bar_cp.click_open_profile_dropdown().click_deauth_button()

    @allure.title("Проверка не отображения кнопки 'Добавить' у не СуперАдмина")
    def test_check_add_button_admin(self, cp, data_cp_admin):
        username, password = data_cp_admin[1], data_cp_admin[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_users()
        check = cp.internal_page.check_add_button()
        assert check is False, "Кнопка 'Добавить' отображается"
        cp.top_bar_cp.click_open_profile_dropdown().click_deauth_button()

    # TODO ждет дальнейшей разработки
    # @allure.title("Проверка наличия вкладки связывания БШМ с РГ в ПУ у СуперАдмина")
    # def test_super_admin_sync_button_is_active(self, cp, data_cp_superadmin):
    #     username, password = data_cp_superadmin[1], data_cp_superadmin[2]
    #     cp.cp_auth_form.open().login(username, password)

    # TODO ждет дальнейшей разработки
    # @allure.title("Проверка отсутствия вкладки связывания БШМ с РГ в ПУ у Админа")
    # def test_admin_sync_button_is_disabled(self, cp, data_cp_admin):
    #     username, password = data_cp_admin[1], data_cp_admin[2]
    #     cp.cp_auth_form.open().login(username, password)
