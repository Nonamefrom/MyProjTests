import time
import allure
from model.notification import Notification


@allure.suite('Тесты ПУ')
@allure.sub_suite('Тесты страницы Уведомления в ПУ(поля, валидация, создание, отправка)')
class TestCpNotifications:
    @allure.title('Начальная проверка страницы Уведомления за superadmin')
    def test_notification_page_as_superadmin(self, cp, data_cp_superadmin):
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        assert cp.notifications.h1_text_check() is True
        assert cp.notifications.h3_text_check() is True
        assert cp.notifications.add_button_presence() is True
        assert cp.notifications.add_button_clickable() is True
        assert cp.notifications.modal_opening_check() is True

    @allure.title('Начальная проверка страницы Уведомления за user')
    def test_notification_page_as_user(self, cp, data_cp_user):
        username, password = data_cp_user[1], data_cp_user[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        assert cp.notifications.h1_text_check() is True
        assert cp.notifications.h3_text_check() is True
        assert cp.notifications.add_button_presence() is True
        assert cp.notifications.add_button_clickable() is True
        assert cp.notifications.modal_opening_check() is True

    @allure.title('Проверка имён/подсказок/валидации полей в модалке за user')
    def test_notification_fields_validation_as_user(self, cp, data_cp_user):
        username, password = data_cp_user[1], data_cp_user[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        # проверяем что чекбокса по умолчанию при открытии модалки - нет
        assert cp.notifications.checkbox_rn_is_enable() is False, 'В Чекбоксе "Отправить всем" поставлен чекбокс'
        # проверяем все имена полей, подсказки, плейсхолдеры(если есть)
        assert cp.notifications.rn_field_name_and_hint_check() is True, 'Ошибка проверки имени и подсказки поля РН'
        # проверяем текст рядом с чекбоксом "отправить всем"
        assert cp.notifications.rn_send_to_all_name_check() is True, 'Ошибка проверки имени поля "Отправить всем'
        # проверяем поля ниже
        assert cp.notifications.level_field_name_check() is True, 'Ошибка проверки имени поля "Цвет уведомления"'
        assert cp.notifications.type_field_name_check() is True, 'Ошибка проверки имени поля "Уровень уведомления"'
        assert cp.notifications.header_field_name_check() is True, 'Ошибка проверки имени поля "Заголовок уведомления"'
        assert cp.notifications.text_field_name_check() is True, 'Ошибка проверки имени поля "Текст уведомления"'
        # проверяем работу селектора Цвета уведомления синий/желт/красный/убрать выбор
        cp.notifications.level_select('blue')
        cp.notifications.level_select('yellow')
        cp.notifications.level_select('red')
        cp.notifications.level_select()
        # меняем тип уведомления на "с кнопкой" и проверяем появившиеся поля
        cp.notifications.type_select('with')
        # cp.notifications.type_select('without')  # для отладки
        # cp.notifications.type_select()  # для отладки
        assert cp.notifications.button_text_name_and_hint_check() is True, \
            'Название и подсказка поля "Текст на кнопке" не соответсвуют тому что должны'
        assert cp.notifications.button_link_name_and_hint_check() is True, \
            'Название и подсказка поля "Ссылка на кнопке" не соответсвуют тому что должны'
        # # меняем тип обратно на "без кнопки" и жмём кнопку отправить/сохранить
        cp.notifications.type_select()
        cp.notifications.save()
        # и проверяем ошибки валидации которые должны заменить подсказки
        assert cp.notifications.check_errors_in_modal() is True, \
            'Набор ошибок не соответсвует должному'
        # снова меняем тип уведомления на "с кнопкой"
        cp.notifications.type_select('with')
        cp.notifications.save()
        assert cp.notifications.check_errors_in_modal(btn=True) is True, \
            'Набор ошибок не соответсвует должному'
        # ставим чекбокс "отправить всем" и ставим "без кнопки"
        cp.notifications.type_select('without')
        cp.notifications.checkbox_rn('place')
        cp.notifications.save()
        assert cp.notifications.check_errors_in_modal(btn=False, chkbx=True) is True, \
            'Набор ошибок не соответсвует должному'
        # Возвращаем всё на дефолтные значения
        cp.notifications.type_select()
        cp.notifications.checkbox_rn('remove')
        cp.notifications.save()
        assert cp.notifications.check_errors_in_modal() is True, \
            'Набор ошибок не соответсвует должному'


    @allure.title('Проверка имён/подсказок/валидации полей в модалке за за superadmin')
    def test_notification_fields_validation_as_superadmin(self, cp, data_cp_superadmin):
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        # проверяем что чекбокса по умолчанию при открытии модалки - нет
        assert cp.notifications.checkbox_rn_is_enable() is False, 'В Чекбоксе "Отправить всем" поставлен чекбокс'
        # проверяем все имена полей, подсказки, плейсхолдеры(если есть)
        assert cp.notifications.rn_field_name_and_hint_check() is True, 'Ошибка проверки имени и подсказки поля РН'
        # проверяем текст рядом с чекбоксом "отправить всем"
        assert cp.notifications.rn_send_to_all_name_check() is True, 'Ошибка проверки имени поля "Отправить всем'
        # проверяем поля ниже
        assert cp.notifications.level_field_name_check() is True, 'Ошибка проверки имени поля "Цвет уведомления"'
        assert cp.notifications.type_field_name_check() is True, 'Ошибка проверки имени поля "Уровень уведомления"'
        assert cp.notifications.header_field_name_check() is True, 'Ошибка проверки имени поля "Заголовок уведомления"'
        assert cp.notifications.text_field_name_check() is True, 'Ошибка проверки имени поля "Текст уведомления"'
        # проверяем работу селектора Цвета уведомления синий/желт/красный/убрать выбор
        cp.notifications.level_select('blue')
        cp.notifications.level_select('yellow')
        cp.notifications.level_select('red')
        cp.notifications.level_select()
        # меняем тип уведомления на "с кнопкой" и проверяем появившиеся поля
        cp.notifications.type_select('with')
        # cp.notifications.type_select('without')  # для отладки
        # cp.notifications.type_select()  # для отладки
        assert cp.notifications.button_text_name_and_hint_check() is True, \
            'Название и подсказка поля "Текст на кнопке" не соответсвуют тому что должны'
        assert cp.notifications.button_link_name_and_hint_check() is True, \
            'Название и подсказка поля "Ссылка на кнопке" не соответсвуют тому что должны'
        # # меняем тип обратно на "без кнопки" и жмём кнопку отправить/сохранить
        cp.notifications.type_select()
        cp.notifications.save()
        # и проверяем ошибки валидации которые должны заменить подсказки
        assert cp.notifications.check_errors_in_modal() is True, \
            'Набор ошибок не соответсвует должному'
        # снова меняем тип уведомления на "с кнопкой"
        cp.notifications.type_select('with')
        cp.notifications.save()
        assert cp.notifications.check_errors_in_modal(btn=True) is True, \
            'Набор ошибок не соответсвует должному'
        # ставим чекбокс "отправить всем" и ставим "без кнопки"
        cp.notifications.type_select('without')
        cp.notifications.checkbox_rn('place')
        cp.notifications.save()
        assert cp.notifications.check_errors_in_modal(btn=False, chkbx=True) is True, \
            'Набор ошибок не соответсвует должному'
        # Возвращаем всё на дефолтные значения
        cp.notifications.type_select()
        cp.notifications.checkbox_rn('remove')
        cp.notifications.save()
        assert cp.notifications.check_errors_in_modal() is True, \
            'Набор ошибок не соответсвует должному'


    @allure.title('Проверка невозможности создать уведомление с невалидным набором данных полей/селекторов за user')
    def test_unnable_to_create_notification_with_invalid_data_as_user(self, cp, data_cp_user,
                                                                      suit_notification_invalid):
        username, password = data_cp_user[1], data_cp_user[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        # Вводим данные из suit_notification_invalid
        cp.notifications.fill_notification(suit_notification_invalid)
        cp.notifications.save()
        # Проверяем ошибки согласно suit_notification_invalid
        assert cp.notifications.check_errors_in_modal(suit_notification_invalid) is True, \
            'Набор ошибок не соответсвует должному'

    @allure.title('Проверка невозможности создать уведомление с невалидным набором данных полей/селекторов за user')
    def test_unnable_to_create_notification_with_invalid_data_as_superadmin(self, cp, data_cp_superadmin,
                                                                            suit_notification_invalid):
        username, password = data_cp_superadmin[1], data_cp_superadmin[2]
        cp.cp_auth_form.open().login(username, password)
        cp.side_bar_cp.click_notifications()
        cp.notifications.open_modal()
        # Вводим данные из suit_notification_invalid
        cp.notifications.fill_notification(suit_notification_invalid)
        cp.notifications.save()
        # Проверяем ошибки согласно suit_notification_invalid
        assert cp.notifications.check_errors_in_modal(suit_notification_invalid) is True, \
            'Набор ошибок не соответсвует должному'
