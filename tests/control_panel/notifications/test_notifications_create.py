import time
import allure
import pytest
from model.notification import Notification


@allure.suite('Тесты ПУ')
@allure.sub_suite('Тесты страницы Уведомления в ПУ(поля, валидация, создание)')
class TestCpNotifications:

    @allure.title('Проверка открытия страницы уведомления в ПУ у Администратора')
    @allure.id('CP/Notification/№ 1')
    def test_notification_page_as_superadmin(self, cp, data_cp_superadmin):
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        assert cp.notifications.h1_text_check() is True
        assert cp.notifications.h3_text_check() is True

    @allure.title('Проверка открытия страницы уведомления в ПУ у Пользователя')
    @allure.id('CP/Notification/№ 2')
    def test_notification_page_as_user(self, cp, data_cp_user):
        username, password = data_cp_user[1], data_cp_user[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        assert cp.notifications.h1_text_check() is True
        assert cp.notifications.h3_text_check() is True

    @allure.title('Проверка открытия модалки у Администратора')
    @allure.id('CP/Notification/№ 3')
    def test_notification_superadmin_can_open_modal(self, cp, data_cp_superadmin):
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        assert cp.notifications.modal_opening_check() is True

    @allure.title('Проверка открытия модалки у Пользователя')
    @allure.id('CP/Notification/№ 4')
    def test_notification_user_can_open_modal(self, cp, data_cp_user):
        username, password = data_cp_user[1], data_cp_user[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        assert cp.notifications.modal_opening_check() is True

    @allure.title('Проверка отображения ошибки отсутствия РН в поле РН при отсутствующем чекбоксе')
    @allure.id('CP/Notification/№ 5')
    @pytest.mark.parametrize('test_data, expected', [(False, 'empty'), (True, False)])
    def test_notification_no_checkbox_error_if_no_rn(self, cp, data_cp_user, test_data, expected):
        username, password = data_cp_user[1], data_cp_user[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        cp.notifications.checkbox_rn(action=test_data)
        cp.notifications.save()
        assert cp.notifications.get_rn_error() == expected, \
            f'Ожидалось {expected} но получили{cp.notifications.get_rn_error()}'
        assert cp.notifications.get_snack_result() == 'incorrect', \
            f'Ожидалось сообщение об ошибке но получили {cp.notifications.get_snack_result()}'

    @allure.title('Проверка валидации поля при вводе перечня РН невалидного формата из цифр запятых и пробелов')
    @allure.id('CP/Notification/№ 6')
    def test_notification_rn_list_validation_as_user(self, cp, data_cp_user, suit_notification_invalid_rn):
        username, password = data_cp_user[1], data_cp_user[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        cp.notifications.fill_notification(suit_notification_invalid_rn)
        cp.notifications.save()
        assert cp.notifications.get_rn_error() == 'incorrect', \
            f'Ожидалось что {suit_notification_invalid_rn.rn} не пройдёт валидацию'
        assert cp.notifications.get_snack_result() == 'incorrect', \
            f'Ожидалось сообщение об ошибке но получили {cp.notifications.get_snack_result()}'

    @allure.title('Проверка валидации отсутствия выбора в "Цвет уведомления"')
    @allure.id('CP/Notification/№ 7')
    @pytest.mark.parametrize('test_data, expected', [(None, 'empty'), ('blue', False),('yellow', False),('red', False)])
    def test_notification_level_validation_as_user(self, cp, data_cp_user, test_data, expected):
        username, password = data_cp_user[1], data_cp_user[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        cp.notifications.level_select(test_data)
        cp.notifications.save()
        assert cp.notifications.get_level_error() == expected, \
            f'Ожидалось {expected} но получили {cp.notifications.get_level_error()}'
        assert cp.notifications.get_snack_result() == 'incorrect', \
            f'Ожидалось сообщение об ошибке но получили {cp.notifications.get_snack_result()}'

    @allure.title('Проверка валидации отсутствия выбора в "Тип уведомления"')
    @allure.id('CP/Notification/№ 8')
    @pytest.mark.parametrize('test_data, expected', [(None, 'empty'), ('with', False), ('without', False)])
    def test_notification_level_validation_as_user(self, cp, data_cp_user, test_data, expected):
        username, password = data_cp_user[1], data_cp_user[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        cp.notifications.type_select(test_data)
        cp.notifications.save()
        assert cp.notifications.get_type_error() == expected, \
            f'Ожидалось {expected} но получили {cp.notifications.get_type_error()}'
        assert cp.notifications.get_snack_result() == 'incorrect', \
            f'Ожидалось сообщение об ошибке но получили {cp.notifications.get_snack_result()}'

    @allure.title('Проверка валидации отсутствия текста в "Заголовок уведомления"')
    @allure.id('CP/Notification/№ 9')
    @pytest.mark.parametrize('test_data, expected', [(None, 'empty'), ('some header', False)])
    def test_notification_header_validation_as_user(self, cp, data_cp_user, test_data, expected):
        username, password = data_cp_user[1], data_cp_user[2]
        notification = Notification(header=test_data)
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        cp.notifications.fill_notification(notification)
        cp.notifications.save()
        assert cp.notifications.get_header_error() == expected, \
            f'Ожидалось {expected} но получили {cp.notifications.get_header_error()}'
        assert cp.notifications.get_snack_result() == 'incorrect', \
            f'Ожидалось сообщение об ошибке но получили {cp.notifications.get_snack_result()}'

    @allure.title('Проверка валидации "Текста на кнопке" при типе "С кнопкой"')
    @allure.id('CP/Notification/№ 10')
    @pytest.mark.parametrize('test_data, expected', [(None, 'empty'), ('name', False),
                                                     ('still valid btn name', False)
                                                     , ('tooo long button name', 'length')
                                                     , ('toooo long button name', 'length')])
    def test_notification_btn_name_validation_as_user(self, cp, data_cp_user, test_data, expected):
        username, password = data_cp_user[1], data_cp_user[2]
        notification = Notification(notif_type='with', bname=test_data)
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        cp.notifications.fill_notification(notification)
        cp.notifications.save()
        assert cp.notifications.get_btn_text_error() == expected, \
            f'Ожидалось {expected} но получили {cp.notifications.get_btn_text_error()}'
        assert cp.notifications.get_snack_result() == 'incorrect', \
            f'Ожидалось сообщение об ошибке но получили {cp.notifications.get_snack_result()}'

    @allure.title('Проверка валидации "Ссылка на кнопке" при типе "С кнопкой"')
    @allure.id('CP/Notification/№ 10')
    @pytest.mark.parametrize('test_data, expected', [(None, 'empty'),
                                                     ('https://partner.svrauto.ru/options/5/info', False)])
    def test_notification_btn_link_empty_validation_as_user(self, cp, data_cp_user, test_data, expected):
        username, password = data_cp_user[1], data_cp_user[2]
        notification = Notification(notif_type='with', blink=test_data)
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        cp.notifications.fill_notification(notification)
        cp.notifications.save()
        assert cp.notifications.get_btn_link_error() == expected, \
            f'Ожидалось {expected} но получили {cp.notifications.get_btn_link_error()}'
        assert cp.notifications.get_snack_result() == 'incorrect', \
            f'Ожидалось сообщение об ошибке но получили {cp.notifications.get_snack_result()}'

    @allure.title('Проверка валидации "Ссылки на кнопке" при типе "С кнопкой"')
    @allure.id('CP/Notification/№ 11')
    def test_notification_btn_link_formate_validation_as_user(self, cp, data_cp_user, suit_notification_invalid_links):
        username, password = data_cp_user[1], data_cp_user[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        cp.notifications.fill_notification(suit_notification_invalid_links)
        cp.notifications.save()
        assert cp.notifications.get_btn_link_error() == 'incorrect', \
            f'Ожидалось {expected} но получили {cp.notifications.get_btn_link_error()}'
        assert cp.notifications.get_snack_result() == 'incorrect', \
            f'Ожидалось сообщение об ошибке но получили {cp.notifications.get_snack_result()}'

    @allure.title('Создание валидного уведомления и проверка его содержимого(сохранилось только важное из введённого)')
    @allure.id('CP/Notification/№ 18')
    def test_notification_check_created_notification(self, cp, data_cp_user, suit_notification_valid):
        username, password = data_cp_user[1], data_cp_user[2]
        notification = suit_notification_valid
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        cp.notifications.fill_notification(notification)
        cp.notifications.save()
        assert cp.notifications.get_snack_result() == 'created'
        cp.notifications.find_edit_button_by_header_and_status('created', notification.header)
        created_notification = cp.notifications.read_notification()
        # print(notification)
        # print(created_notification)
        assert notification == created_notification
