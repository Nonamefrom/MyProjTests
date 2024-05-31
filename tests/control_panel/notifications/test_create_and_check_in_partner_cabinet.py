import random
import time
import allure
from model.notification import Notification
import datetime
import copy


@allure.suite('Тесты ПУ')
@allure.sub_suite('Тесты отправки Уведомлений партнёрам')
class TestCpAndPcNotifications:

    @allure.title('Проверка отправки уведомления только тому партнёру чей рн указан в поле рн')
    @allure.id('CP/Notification/№ 14')
    def test_create_notification_for_one_partner(self, cp, data_cp_superadmin,
                                                 suit_notification_for_test, data_rn_list):
        now = datetime.datetime.now()
        test_time = str(now)[:-7]
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        notification = copy.deepcopy(suit_notification_for_test)
        rn_list = list(data_rn_list)
        rn = random.choice(rn_list)  # Выбираем случайный рн которому будем отправлять уведомление
        rn_list.remove(rn)  # Удаляем его из списка рн
        notification.rn = str(rn)  # В данных перевыбираем рн на наш
        notification.checkbox = False   # выключаем чекбокс(если придёт не пустой, а нам надо пустой)
        notification.header = str(f'only for {rn}: {test_time}')
        # Заходим в ПУ и создаём уведомление
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        cp.notifications.fill_notification(notification)
        cp.notifications.save()
        assert cp.notifications.get_snack_result() == 'created', 'Нет нотификейшена об успешном создании'
        time.sleep(7)  # Костыль для того что бы исчез предыдущий нотификейшн в снекбаре. 5 секунд + анимация + запас
        cp.driver.switch_to.new_window()
        cp.cabinet_landing_page.open()
        cp.cabinet_landing_page.login_all_env(cp, rn)
        cp.top_bar.open_notifications()
        assert cp.pc_notifications.find_notification_by_header(notification.header) is False, \
            f'Уведомление с заголовком {notification.header} еще не отправлено, но уже найдено у партнёра'
        cp.driver.switch_to.window(cp.driver.window_handles[0])
        cp.notifications.find_send_button_by_header_and_status('created', notification.header)
        assert cp.notifications.get_snack_result() == 'sent', 'Уведомление не найдено'
        cp.driver.switch_to.window(cp.driver.window_handles[1])
        cp.driver.refresh()
        time.sleep(2)
        cp.top_bar.open_notifications()
        assert cp.pc_notifications.find_notification_by_header(notification.header) is True, \
            f'Уведомление с заголовком {notification.header} отправлено, но не найдено у партнёра'
        cp.pc_notifications.close_notifications_modal()
        cp.top_bar.open_profile_dropdown().click_deauth_button()
        time.sleep(2)
        rn = random.choice(rn_list)
        cp.cabinet_landing_page.open()
        cp.cabinet_landing_page.login_all_env(cp, rn)
        cp.top_bar.open_notifications()
        assert cp.pc_notifications.find_notification_by_header(notification.header) is False, \
            f'Уведомление с заголовком {notification.header} найдено у партнёра который не должен был его получить'

    @allure.title('Проверка отправки уведомления списку партнёров чей рн указан в поле рн')
    @allure.id('CP/Notification/№ 15')
    def test_create_notification_for_all_partners_except_one(self, cp, data_cp_superadmin,
                                                             suit_notification_for_test, data_rn_list):
        now = datetime.datetime.now()
        test_time = str(now)[:-7]
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        notification = copy.deepcopy(suit_notification_for_test)
        rn_list = list(data_rn_list)  # Выбираем случайный рн которому НЕ будем отправлять уведомление
        rn = random.choice(rn_list)  # Удаляем его из списка рн
        rn_list.remove(rn)
        rn_string = ','.join(str(el) for el in rn_list)
        notification.rn = str(rn_string)  # В данных перевыбираем рн на наш список кому отправляем
        notification.checkbox = False  # выключаем чекбокс(если придёт не пустой, а нам надо пустой)
        notification.header = str(f'not for {rn}: {test_time}')
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        cp.notifications.fill_notification(notification)
        cp.notifications.save()
        assert cp.notifications.get_snack_result() == 'created', 'Нет нотификейшена об успешном создании'
        time.sleep(7)  # Костыль для того что бы исчез предыдущий нотификейшн в снекбаре. 5 секунд + анимация + запас
        cp.driver.switch_to.new_window()
        cp.cabinet_landing_page.open()
        cp.cabinet_landing_page.login_all_env(cp, rn)
        cp.top_bar.open_notifications()
        assert cp.pc_notifications.find_notification_by_header(notification.header) is False, \
            f'Уведомление с заголовком {notification.header} еще не отправлено, но уже найдено у партнёра'
        cp.driver.switch_to.window(cp.driver.window_handles[0])
        cp.notifications.find_send_button_by_header_and_status('created', notification.header)
        assert cp.notifications.get_snack_result() == 'sent', 'Уведомление не найдено'
        cp.driver.switch_to.window(cp.driver.window_handles[1])
        cp.driver.refresh()
        time.sleep(2)
        cp.top_bar.open_notifications()
        assert cp.pc_notifications.find_notification_by_header(notification.header) is False, \
            f'Уведомление с заголовком {notification.header} найдено у партнёра который не должен был его получить'
        cp.pc_notifications.close_notifications_modal()
        cp.top_bar.open_profile_dropdown().click_deauth_button()
        time.sleep(2)
        rn = random.choice(rn_list)
        cp.cabinet_landing_page.open()
        cp.cabinet_landing_page.login_all_env(cp, rn)
        cp.top_bar.open_notifications()
        assert cp.pc_notifications.find_notification_by_header(notification.header) is True, \
            f'Уведомление с заголовком {notification.header} не найдено у партнёра который должен был его получить'

    @allure.title('Проверка отправки уведомления всем партнёрам если стоит чекбокс "всем"')
    @allure.id('CP/Notification/№ 16')
    def test_create_notification_for_all_partners(self, cp, data_cp_superadmin,
                                                  suit_notification_for_test, data_rn_list):
        now = datetime.datetime.now()
        test_time = str(now)[:-7]
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        notification = copy.deepcopy(suit_notification_for_test)
        rn_list = list(data_rn_list)
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        notification.header = str(f'for all partners: {test_time}')
        cp.notifications.fill_notification(notification)
        cp.notifications.save()
        assert cp.notifications.get_snack_result() == 'created', 'Нет нотификейшена об успешном создании'
        time.sleep(7)  # Костыль для того что бы исчез предыдущий нотификейшн в снекбаре. 5 секунд + анимация + запас
        cp.driver.switch_to.new_window()
        cp.cabinet_landing_page.open()
        rn = random.choice(rn_list)
        rn_list.remove(rn)
        cp.cabinet_landing_page.login_all_env(cp, rn)
        cp.top_bar.open_notifications()
        assert cp.pc_notifications.find_notification_by_header(notification.header) is False, \
            f'Уведомление с заголовком {notification.header} еще не отправлено, но уже найдено у партнёра'
        cp.driver.switch_to.window(cp.driver.window_handles[0])
        cp.notifications.find_send_button_by_header_and_status('created', notification.header)
        assert cp.notifications.get_snack_result() == 'sent', 'Уведомление не найдено'
        cp.driver.switch_to.window(cp.driver.window_handles[1])
        cp.driver.refresh()
        time.sleep(2)
        cp.top_bar.open_notifications()
        assert cp.pc_notifications.find_notification_by_header(notification.header) is True, \
            f'Уведомление с заголовком {notification.header} отправлено, но не найдено у партнёра'

    @allure.title('Проверка отправки уведомления всем партнёрам если стоит чекбокс "всем" если в поле есть перечень рн')
    @allure.id('CP/Notification/№ 17')
    def test_create_notification_for_all_partners_despite_rn_list_in_rn_field(self, cp, data_cp_superadmin,
                                                                              suit_notification_for_test, data_rn_list):
        now = datetime.datetime.now()
        test_time = str(now)[:-7]
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        notification = copy.deepcopy(suit_notification_for_test)
        rn_list = list(data_rn_list)
        notification.rn = ','.join(str(el) for el in rn_list)
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        notification.header = str(f'for all partners despite rn list: {test_time}')
        cp.notifications.fill_notification(notification)
        cp.notifications.save()
        assert cp.notifications.get_snack_result() == 'created', 'Нет нотификейшена об успешном создании'
        time.sleep(7)  # Костыль для того что бы исчез предыдущий нотификейшн в снекбаре. 5 секунд + анимация + запас
        cp.driver.switch_to.new_window()
        cp.cabinet_landing_page.open()
        rn = random.choice(rn_list)
        rn_list.remove(rn)
        cp.cabinet_landing_page.login_all_env(cp, rn)
        cp.top_bar.open_notifications()
        assert cp.pc_notifications.find_notification_by_header(notification.header) is False, \
            f'Уведомление с заголовком {notification.header} еще не отправлено, но уже найдено у партнёра'
        cp.driver.switch_to.window(cp.driver.window_handles[0])
        cp.notifications.find_send_button_by_header_and_status('created', notification.header)
        assert cp.notifications.get_snack_result() == 'sent', 'Уведомление не найдено'
        cp.driver.switch_to.window(cp.driver.window_handles[1])
        cp.driver.refresh()
        time.sleep(2)
        cp.top_bar.open_notifications()
        assert cp.pc_notifications.find_notification_by_header(notification.header) is True, \
            f'Уведомление с заголовком {notification.header} отправлено, но не найдено у партнёра'
