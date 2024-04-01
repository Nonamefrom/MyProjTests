import random
import datetime


nine_digit_number = random.randint(100000000, 999999999)
now = datetime.datetime.now()
time_1 = str(now).split(' ')
time_1 = '-'.join(time_1)
test_time = time_1[:-7:].replace(':', '.')


class RegData:
    EMAIL = 'admin@svrauto.ru'
    WRONG_MAIL = 'admin@admin@ru23'
    WRONG_USER_PASS = '123456789'
    USER_PASS = 'adminPass'
    INTERNAL_MAIL = 'internal0@svrauto.ru'
    INTERNAL_PASS = 'internal0Pass'
    B2B_MAIL = 'atuser@mail.ru'
    B2B_PASS = 'ATuser'
    MIM_LOGIN = 'CLIENTMIM'
    MIM_PASS = 'QJN5VXYA'


class GenerateData:
    PHONE = f'9{nine_digit_number}'
    NAME = f"ИмяТест{test_time}"
    LAST_NAME = f"ФамилияТест{test_time}"
    MAIL = f'test{test_time}@mail.ru'


class ExpectedResults:
    CONTROL_PANEL_HEADER = 'Панель управления'
    CONTROL_PANEL_PROFILE = 'Профиль'
    SERVICE_BOOKING_H1 = 'Онлайн запись на шиномонтаж'
    CONTROL_PANEL_H1 = 'Управление опциями'
    PWZ_H1 = 'Список заказов'
    EMP_DASH_H1 = 'Доступные сервисы'
    H1_LANDING_CABINET = 'Точка движения'
    PARTNER_CABINET_H1 = 'Доступные опции'
    ERROR_TEXT = 'Неправильное имя пользователя или пароль.'
    PASS_ARE_DIFF = 'Пароли не совпадают.'
    MAIL_VALIDATION_PROFILE_CAB = 'Поле электронный адрес должно быть действительным электронным адресом.'

#
