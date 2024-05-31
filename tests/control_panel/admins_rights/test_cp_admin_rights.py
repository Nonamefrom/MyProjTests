import time
import allure
from data.test_data import ExpectedResults as ER


@allure.suite('Тесты ПУ')
@allure.sub_suite('Проверка разделения прав Админа и СуперАдмина')
class TestAdminRights:

    @allure.title('Проверка отсутствия возможности нажать кнопку Синхронизации с Парусом у Пользователя ПУ в ПВЗ опции')
    @allure.id('CP/PWZ/№ 1')
    def test_admin_sync_button_is_disabled(self, cp, data_cp_user):
        username, password = data_cp_user[1], data_cp_user[2]
        cp.cp_auth_form.open().login(username, password)
        cp.common_steps.find_elem('ПВЗ')
        cp.admin.admin_tab()
        assert cp.admin.sync_button_status() is False
        assert cp.admin.sync_button_class() is False
        cp.top_bar_cp.click_open_profile_dropdown().click_deauth_button()

    @allure.title('Проверка возможности нажать кнопку Синхронизации с Парусом у Администратора ПУ в ПВЗ опции')
    @allure.id('CP/PWZ/№ 2')
    def test_super_admin_sync_button_is_active(self, cp, data_cp_superadmin):
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        cp.cp_auth_form.open().login(username, password)
        cp.common_steps.find_elem('ПВЗ')
        cp.admin.admin_tab()
        assert cp.admin.sync_button_status() is True
        assert cp.admin.sync_button_class() is True
        cp.top_bar_cp.click_open_profile_dropdown().click_deauth_button()

    @allure.title('Проверка отображение кнопки "Добавить" Пользователя у Администратора на странице Пользователей ПУ')
    @allure.id('CP/USERS/№ 1')
    def test_check_add_button_super_admin(self, cp, data_cp_superadmin):
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_users()
        assert cp.internal_page.check_add_button() is True, 'Кнопка "Добавить" не отображается'
        cp.top_bar_cp.click_open_profile_dropdown().click_deauth_button()

    @allure.title('Проверка не отображения кнопки "Добавить" Пользователя у Пользователя на странице Пользователей ПУ')
    @allure.id('CP/USERS/№ 2')
    def test_check_add_button_admin(self, cp, data_cp_user):
        username, password = data_cp_user[1], data_cp_user[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_users()
        assert cp.internal_page.check_add_button() is False, 'Кнопка "Добавить" отображается'
        cp.top_bar_cp.click_open_profile_dropdown().click_deauth_button()

    @allure.title('Проверка наличия вкладки связывания БШМ с РГ в ПУ у Администратора и кнопки Связать')
    @allure.id('CP/FTS/№ 1')
    def test_super_admin_link_warranty_to_fts_tab_and_button(self, cp, data_cp_superadmin, data_fts_names):
        fts = data_fts_names
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        cp.cp_auth_form.open().login(username, password)
        cp.common_steps.find_elem(fts)
        assert cp.fts.link_to_warranty_tab_exist() is True, f'У Администратора нет вкладки Привязки РГ в опции {fts}'
        assert cp.fts.link_button_is_present() is True, f'На вкладке Привязки РГ в опции {fts} нет кнопки "Связать"'

    @allure.title('Проверка отсутствия вкладки связывания БШМ с РГ в ПУ у Пользователя, и нет кнопки "Связать"')
    @allure.id('CP/FTS/№ 2')
    def test_user_link_warranty_to_fts_tab_and_button(self, cp, data_cp_user, data_fts_names):
        fts = data_fts_names
        username, password = data_cp_user[1], data_cp_user[2]
        cp.cp_auth_form.open().login(username, password)
        cp.common_steps.find_elem(fts)
        assert cp.fts.link_to_warranty_tab_exist() is False, f'У Пользователя видна вкладка Привязки РГ в опции {fts}'

    @allure.title('Проверка наличия кнопки "Отправить уведомление" в ПУ у Администратора')
    @allure.id('CP/Notification/№ 12')
    def test_able_to_press_send_notification_button_as_superadmin(self, cp, data_cp_superadmin,
                                                                  suit_notification_for_test):
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        notification = suit_notification_for_test
        header = notification.header
        cp.notifications.fill_notification(notification)
        cp.notifications.save()
        assert cp.notifications.get_snack_result() == 'created', 'Нет нотификейшена об успешном создании'
        time.sleep(7)  # Костыль для того что бы исчез предыдущий нотификейшн в снекбаре. 5 секунд + анимация + запас
        cp.notifications.find_send_button_by_header_and_status('created', header)
        assert cp.notifications.get_snack_result() == 'sent', 'Созданное уведомление не найдено'

    @allure.title('Проверка наличия кнопки "Отправить уведомление" в ПУ у Пользователя')
    @allure.id('CP/Notification/№ 13')
    def test_able_to_press_send_notification_button_as_user(self, cp, data_cp_user,
                                                            suit_notification_for_test):
        username, password = data_cp_user[1], data_cp_user[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        notification = suit_notification_for_test
        header = notification.header
        cp.notifications.fill_notification(notification)
        cp.notifications.save()
        assert cp.notifications.get_snack_result() == 'created', 'Нет нотификейшена об успешном создании'
        time.sleep(7)  # Костыль для того что бы исчез предыдущий нотификейшн в снекбаре. 5 секунд + анимация + запас
        cp.notifications.find_send_button_by_header_and_status('created', header)
        assert cp.notifications.get_snack_result() == 'sent', 'Созданное уведомление не найдено'
