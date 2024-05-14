import time
import allure
from data.test_data import ExpectedResults as ER


@allure.suite('Тесты ПУ')
@allure.sub_suite('Проверка разделения прав Админа и СуперАдмина')
class TestAdminRights:
    @allure.title('Проверка отсутствия возможности нажать кнопку Синхронизации с Парусом в ПУ у Админа')
    def test_admin_sync_button_is_disabled(self, cp, data_cp_user):
        username, password = data_cp_user[1], data_cp_user[2]
        cp.cp_auth_form.open().login(username, password)
        cp.common_steps.find_elem('ПВЗ')
        cp.admin.admin_tab()
        # assert cp.admin.sync_button_status() is not True
        assert cp.admin.sync_button_class() is not True
        cp.top_bar_cp.click_open_profile_dropdown().click_deauth_button()

    @allure.title('Проверка возможности нажать кнопку Синхронизации с Парусом в ПУ у СуперАдмина')
    def test_super_admin_sync_button_is_active(self, cp, data_cp_superadmin):
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        cp.cp_auth_form.open().login(username, password)
        cp.common_steps.find_elem('ПВЗ')
        cp.admin.admin_tab()
        # assert cp.admin.sync_button_status() is True
        assert cp.admin.sync_button_class() is True
        cp.top_bar_cp.click_open_profile_dropdown().click_deauth_button()

    @allure.title('Проверка отображение кнопки "Добавить" у СуперАдмина')
    def test_check_add_button_super_admin(self, cp, data_cp_superadmin):
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_users()
        assert cp.internal_page.check_add_button() is True, 'Кнопка "Добавить" не отображается'
        cp.top_bar_cp.click_open_profile_dropdown().click_deauth_button()

    @allure.title('Проверка не отображения кнопки "Добавить" у не СуперАдмина')
    def test_check_add_button_admin(self, cp, data_cp_user):
        username, password = data_cp_user[1], data_cp_user[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_users()
        assert cp.internal_page.check_add_button() is False, 'Кнопка "Добавить" отображается'
        cp.top_bar_cp.click_open_profile_dropdown().click_deauth_button()

    # @allure.title('Проверка наличия вкладки связывания БШМ с РГ в ПУ у СуперАдмина')
    # def test_super_admin_sync_button_is_active(self, cp, data_cp_superadmin):
    #     username, password = data_cp_superadmin[1], data_cp_superadmin[2]
    #     cp.cp_auth_form.open().login(username, password)
    # TODO ждет дальнейшей разработки

    # @allure.title('Проверка отсутствия вкладки связывания БШМ с РГ в ПУ у Админа')
    # def test_admin_sync_button_is_disabled(self, cp, data_cp_user):
    #     username, password = data_cp_user[1], data_cp_user[2]
    #     cp.cp_auth_form.open().login(username, password)
    # TODO ждет дальнейшей разработки

    @allure.title('Возможность отправить уведомление за superadmin')
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
        # Проверяем наличие кнопки "Отправить" уведомление после его создания
        time.sleep(7)  # Костыль для того что бы исчез предыдущий нотификейшн в снекбаре. 5 секунд + анимация + запас
        # Так как номер уведомлений идут по убыванию то новое будет первым сверху(или просто на первой странице)
        cp.notifications.find_send_button_by_header_and_status('created', header)
        assert cp.notifications.get_snack_result() == 'sent', 'Созданное уведомление не найдено'

    @allure.title('НЕвозможность отправить уведомление за user так как нет кнопки "Отправить" напротив '
                  'созданного уведомления')
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
        # Так как номер уведомлений идут по убыванию то новое будет первым сверху(или просто на первой странице)
        assert cp.notifications.get_snack_result() == 'created', 'Нет нотификейшена об успешном создании'
        # Проверяем наличие кнопки "Отправить" уведомление после его создания
        time.sleep(7)  # Костыль для того что бы исчез предыдущий нотификейшн в снекбаре. 5 секунд + анимация + запас
        # Так как номер уведомлений идут по убыванию то новое будет первым сверху(или просто на первой странице)
        cp.notifications.find_send_button_by_header_and_status('created', header)
        assert cp.notifications.get_snack_result() == 'sent', 'Созданное уведомление не найдено'
