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
    USER_PASS = 'adminPass1!'
    INTERNAL_MAIL = 'internal0@svrauto.ru'
    INTERNAL_PASS = 'internal0Pass!'
    B2B_MAIL = 'atuser@mail.ru'
    B2B_PASS = 'ATuser1!'
    MIM_LOGIN = 'CLIENTMIM'
    MIM_PASS = 'QJN5VXYA'


class GenerateData:
    """
    Функция name под декоратором property, позволяют получать имя+время(время в момент обращения к ней).
    Функция name позволяет получать новый телефон в момент обращения, а не объекту созданном при инициализации пакета.
    В модуле создается экземпляр класса gen_data = GenerateData()(пример), вызов - gen_data.name.
    """

    @property
    def phone(self):
        self.nine_digit_number = random.randint(100000000, 999999999)
        return f'9{self.nine_digit_number}'

    @property
    def name(self):
        now = datetime.datetime.now()
        time_dirty = str(now).split(' ')
        time_dirty = '-'.join(time_dirty)
        formated_time = time_dirty[:-7:].replace(':', '.')
        result = f"ИмяТест{formated_time}"
        return result

    LAST_NAME = f"ФамилияТест{test_time}"
    TIME_MAIL = f'test{test_time}@mail.ru'
    TIME_SVR_MAIL = f'test{test_time}@svrlab.ru'
    RANDOM_MAIL = f'test{nine_digit_number}@mail.ru'


class ExpectedResults:
    CONTROL_PANEL_HEADER = 'Панель управления'
    CONTROL_PANEL_PROFILE = 'Профиль'
    SERVICE_BOOKING_H1 = 'Онлайн запись на шиномонтаж'
    CONTROL_PANEL_H1 = 'Управление опциями'
    CP_INTERNAL_PAGE_H1 = 'Пользователи'
    PWZ_H1 = 'Список заказов'
    EMP_DASH_H1 = 'Доступные сервисы'
    H1_LANDING_CABINET = 'Точка движения'
    PARTNER_CABINET_H1 = 'Доступные опции'
    ERROR_TEXT = 'Неправильное имя пользователя или пароль.'
    PASS_ARE_DIFF = 'Пароли не совпадают.'
    MAIL_VALIDATION_PROFILE_CAB = 'Поле электронный адрес должно быть действительным электронным адресом.'
