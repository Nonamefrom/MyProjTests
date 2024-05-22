import random
import time
import allure
from model.notification import Notification


@allure.suite('Тесты ПУ')
@allure.sub_suite('Тесты страницы Уведомления в ПУ: отображение уведомлений только у тех партнёров кому отправляли')
class TestCpAndPcNotifications:

    @allure.title('Создать уведомление только для определённого партнёра')
    def test_create_notification_for_one_partner(self, cp, data_cp_superadmin,
                                                 suit_notification_for_test, data_rn_list):
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        notification = suit_notification_for_test
        # Данные лежат в кортеже, переводим в список, что бы можно было удалять из него
        rn_list = list(data_rn_list)
        # Выбираем случайный рн которому будем отправлять уведомление
        rn = random.choice(rn_list)
        # Удаляем его из списка рн
        rn_list.remove(rn)
        # В данных перевыбираем рн на наш
        notification.rn = str(rn)
        # выключаем на всякий случай чекбокс(если придёт не пустой, а нам надо пустой)
        notification.checkbox = None
        # Заходим в ПУ и создаём уведомление
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        # запоминаем заголовок по которому будем искать уведомление
        cp.notifications.fill_notification(notification)
        cp.notifications.save()
        # Так как номер уведомлений идут по убыванию то новое будет первым сверху(или просто на первой странице)
        assert cp.notifications.get_snack_result() == 'created', 'Нет нотификейшена об успешном создании'
        # Проверяем наличие кнопки "Отправить" уведомление после его создания
        time.sleep(7)  # Костыль для того что бы исчез предыдущий нотификейшн в снекбаре. 5 секунд + анимация + запас
        # Входим в ку и проверяем наличие уведомления с нашим заголовком до отправки уведомления
        cp.driver.switch_to.new_window()
        # Вкладка с ПУ индекс 0, вкладка с КУ индекс 1
        cp.cabinet_landing_page.open()
        cp.cabinet_landing_page.login_all_env(cp, rn)
        cp.top_bar.open_notifications()
        # Проверяем что такого уведомления нет
        assert cp.pc_notifications.find_notification_by_header(notification.header) is False
        cp.driver.switch_to.window(cp.driver.window_handles[0])
        cp.notifications.find_send_button_by_header_and_status('created', notification.header)
        assert cp.notifications.get_snack_result() == 'sent', 'Уведомление не найдено'
        cp.driver.switch_to.window(cp.driver.window_handles[1])
        cp.driver.refresh()
        time.sleep(2)
        cp.top_bar.open_notifications()
        # Проверяем что такое уведомления появилось у этого партнёра и разлогиниваемся
        assert cp.pc_notifications.find_notification_by_header(notification.header) is True
        # закрываем модалку уведомлений
        cp.pc_notifications.close_notifications_modal()
        cp.top_bar.open_profile_dropdown().click_deauth_button()
        time.sleep(2)
        # Входим за другого партнёра что бы проверить что ему не пришло уведомление, берём 1 случайный из оставшихся
        rn = random.choice(rn_list)
        cp.cabinet_landing_page.open()
        cp.cabinet_landing_page.login_all_env(cp, rn)
        cp.top_bar.open_notifications()
        # Проверяем что такого уведомления нет
        assert cp.pc_notifications.find_notification_by_header(notification.header) is False

    @allure.title('Создать уведомление для всех, кроме определённого партнёра')
    def test_create_notification_for_all_partners_except_one(self, cp, data_cp_superadmin,
                                                             suit_notification_for_test, data_rn_list):
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        notification = suit_notification_for_test
        # Данные лежат в кортеже, переводим в список, что бы можно было удалять из него
        rn_list = list(data_rn_list)
        # Выбираем случайный рн которому НЕ будем отправлять уведомление
        rn = random.choice(rn_list)
        # Удаляем его из списка рн
        rn_list.remove(rn)
        # переводим в формат "рн,рн1,рн2,рн3"
        rn_string = ','.join(str(el) for el in rn_list)
        # В данных перевыбираем рн на наш список кому отправляем
        notification.rn = str(rn_string)
        # выключаем на всякий случай чекбокс(если придёт не пустой, а нам надо пустой)
        notification.checkbox = None
        # Заходим в ПУ и создаём уведомление
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        # запоминаем заголовок по которому будем искать уведомление
        cp.notifications.fill_notification(notification)
        cp.notifications.save()
        # Так как номер уведомлений идут по убыванию то новое будет первым сверху(или просто на первой странице)
        assert cp.notifications.get_snack_result() == 'created', 'Нет нотификейшена об успешном создании'
        # Проверяем наличие кнопки "Отправить" уведомление после его создания
        time.sleep(7)  # Костыль для того что бы исчез предыдущий нотификейшн в снекбаре. 5 секунд + анимация + запас
        # Входим в ку и проверяем наличие уведомления с нашим заголовком до отправки уведомления
        cp.driver.switch_to.new_window()
        # Вкладка с ПУ индекс 0, вкладка с КУ индекс 1
        cp.cabinet_landing_page.open()
        cp.cabinet_landing_page.login_all_env(cp, rn)
        cp.top_bar.open_notifications()
        # Проверяем что такого уведомления нет
        assert cp.pc_notifications.find_notification_by_header(notification.header) is False
        cp.driver.switch_to.window(cp.driver.window_handles[0])
        cp.notifications.find_send_button_by_header_and_status('created', notification.header)
        assert cp.notifications.get_snack_result() == 'sent', 'Уведомление не найдено'
        cp.driver.switch_to.window(cp.driver.window_handles[1])
        cp.driver.refresh()
        time.sleep(2)
        cp.top_bar.open_notifications()
        # Проверяем что такое уведомления НЕ появилось у этого партнёра и разлогиниваемся
        assert cp.pc_notifications.find_notification_by_header(notification.header) is False
        # закрываем модалку уведомлений
        cp.pc_notifications.close_notifications_modal()
        cp.top_bar.open_profile_dropdown().click_deauth_button()
        time.sleep(2)
        # Входим за другого партнёра что бы проверить что тем кто был в списке - пришло уведомление
        # Берём 1 случайный из оставшихся
        rn = random.choice(rn_list)
        cp.cabinet_landing_page.open()
        cp.cabinet_landing_page.login_all_env(cp, rn)
        cp.top_bar.open_notifications()
        # Проверяем что такого уведомления нет
        assert cp.pc_notifications.find_notification_by_header(notification.header) is True

    @allure.title('Создать уведомление для всех партнёров(через чекбокс)')
    def test_create_notification_for_all_partners(self, cp, data_cp_superadmin,
                                                  suit_notification_for_test, data_rn_list):
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        notification = suit_notification_for_test
        # Данные лежат в кортеже, переводим в список, что бы можно было удалять из него
        rn_list = list(data_rn_list)
        # Заходим в ПУ и создаём уведомление
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        # запоминаем заголовок по которому будем искать уведомление
        cp.notifications.fill_notification(notification)
        cp.notifications.save()
        # Так как номер уведомлений идут по убыванию то новое будет первым сверху(или просто на первой странице)
        assert cp.notifications.get_snack_result() == 'created', 'Нет нотификейшена об успешном создании'
        # Проверяем наличие кнопки "Отправить" уведомление после его создания
        time.sleep(7)  # Костыль для того что бы исчез предыдущий нотификейшн в снекбаре. 5 секунд + анимация + запас
        # Входим в ку и проверяем наличие уведомления с нашим заголовком до отправки уведомления
        cp.driver.switch_to.new_window()
        # Вкладка с ПУ индекс 0, вкладка с КУ индекс 1
        cp.cabinet_landing_page.open()
        # входим за любой рн из списка и сразу убираем его из списка
        rn = random.choice(rn_list)
        rn_list.remove(rn)
        cp.cabinet_landing_page.login_all_env(cp, rn)
        cp.top_bar.open_notifications()
        # Проверяем что такого уведомления нет
        assert cp.pc_notifications.find_notification_by_header(notification.header) is False
        cp.driver.switch_to.window(cp.driver.window_handles[0])
        cp.notifications.find_send_button_by_header_and_status('created', notification.header)
        assert cp.notifications.get_snack_result() == 'sent', 'Уведомление не найдено'
        cp.driver.switch_to.window(cp.driver.window_handles[1])
        cp.driver.refresh()
        time.sleep(2)
        cp.top_bar.open_notifications()
        # Проверяем что такое уведомления появилось у этого партнёра и разлогиниваемся
        assert cp.pc_notifications.find_notification_by_header(notification.header) is True
        # закрываем модалку уведомлений
        cp.pc_notifications.close_notifications_modal()
        cp.top_bar.open_profile_dropdown().click_deauth_button()
        time.sleep(2)
        # Входим за другого партнёра что бы проверить что тем кто был в списке - тоже пришло уведомление
        # Берём 1 случайный из оставшихся
        rn = random.choice(rn_list)
        cp.cabinet_landing_page.open()
        cp.cabinet_landing_page.login_all_env(cp, rn)
        cp.top_bar.open_notifications()
        # Проверяем что такого уведомления нет
        assert cp.pc_notifications.find_notification_by_header(notification.header) is True
