# -*- coding: utf-8 -*-
from model.notification import Notification
from pages.control_panel.notification import NotificationPage

# Расшифровка значений:
#     case_name - имя теста, обязательно указывать для идентификации, не должно быть None
#     case_name - указывать только на английском пока что
#     number=None - порядковый номер уведомления
#     rn=None - перечень РН Партнёров, для позитивных кейсов - только перечень корректного формата
#     rn_error=None - наличие ошибки, если не указан(в позитивном) или None(в негативном) - значит ошибки нет
#     checkbox=None - наличие чекбокса, если не указан(в позитивном) или None(в негативном) - значит ошибки нет
#     level=None - если None или ничего - ничего не ставим, если указано - выбирать только из существующих вариантов
#     level_error=None - наличие ошибки, если не указан(в позитивном) или None(в негативном) - значит ошибки нет
#     notif_type=None - если None или ничего - ничего не ставим,если указано - выбирать только из существующих вариантов
#     notif_type_error=None  - наличие ошибки, если не указан(в позитивном) или None(в негативном) - значит ошибки нет
#     header=None - если None или ничего - ничего не ставим, если указано - выбирать только из существующих вариантов
#     header_error=None - наличие ошибки, если не указан(в позитивном) или None(в негативном) - значит ошибки нет
#     text=None - если None или ничего - ничего не ставим, если указано - выбирать только из существующих вариантов
#     bname=None - если None или ничего - ничего не ставим, если указано - выбирать только из существующих вариантов
#     bname_error=None - наличие ошибки, если не указан(в позитивном) или None(в негативном) - значит ошибки нет
#     blink=None - если None или ничего - ничего не ставим, если указано - выбирать только из существующих вариантов
#     blink_error=None - наличие ошибки, если не указан(в позитивном) или None(в негативном) - значит ошибки нет
#     snack=None - желательно указывать в позитивном тоже, что бы проверить что успешный снекбар отобразился,
#     в негативном - обязателен!
#
# Варианты чекбокса "Отправить всем":  checkbox=None / checkbox='place'
# NONE = checkbox=None  В идеале ставить 'remove' но так как по умолчанию не ставится - можно и None
# YES = checkbox='place' Лучше не использовать простой клик 'click'
# так как если по умолчанию будет ставиться чекбокс - повторный клик его снимет,
# а так будет проверка ставить ли чекбокс если он уже там есть

# Варианты селекторов
# Цвет уведомления
# BLUE = 'blue'
# YELLOW = 'yellow'
# RED = 'red'
# Тип уведомления
# NO_BUTTON = 'without'
# BUTTON = 'with'

testdata = [
    # Проверяем кейс без рн и без чекбокса + валидные данные
    Notification(case_name='CP/Notifications/Negative case #1',
                 rn=None, checkbox=None,
                 rn_error='empty',
                 level='blue',
                 level_error=None,
                 notif_type='without',
                 notif_type_error=None,
                 header="НЕГАТИВНЫЙ 1",
                 header_error=None,
                 text="",
                 bname=None,
                 bname_error=None,
                 blink=None,
                 blink_error=None,
                 snack='incorrect'
                 )
    # Проверяем кейс с невалидным форматом перечня рн (запятая в конце) и без чекбокса + валидные данные
    , Notification(case_name='CP/Notifications/Negative case #2',
                   rn="123,124,", checkbox=None,
                   rn_error='incorrect',
                   level='blue',
                   level_error=None,
                   notif_type='without',
                   notif_type_error=None,
                   header="НЕГАТИВНЫЙ 2",
                   header_error=None,
                   text="",
                   bname=None,
                   bname_error=None,
                   blink=None,
                   blink_error=None,
                   snack='incorrect'
                   )
    # Проверяем кейс с невалидным форматом перечня рн (пробел после запятой) и без чекбокса + валидные данные
    , Notification(case_name='CP/Notifications/Negative case #3',
                   rn="123, 124", checkbox=None,
                   rn_error='incorrect',
                   level='blue',
                   level_error=None,
                   notif_type='without',
                   notif_type_error=None,
                   header="НЕГАТИВНЫЙ 3",
                   header_error=None,
                   text="",
                   bname=None,
                   bname_error=None,
                   blink=None,
                   blink_error=None,
                   snack='incorrect'
                   )

]
