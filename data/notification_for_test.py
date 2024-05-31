from model.notification import Notification
from pages.control_panel.notification import NotificationPage
import random
import datetime

# Варианты чекбокса "Отправить всем": True/False

# Варианты селекторов
# Цвет уведомления
# BLUE = 'blue'
# YELLOW = 'yellow'
# RED = 'red'
# Тип уведомления
# NO_BUTTON = 'without'
# BUTTON = 'with'

now = datetime.datetime.now()
time = str(now)[:-7]

testdata = [
    # Просто 1 набор валидных данных для проверки связанных с уведомлением, иное чем валидация.
    # Проверяем кейс с введённым рн партнёра без чекбокса + валидные данные
    Notification(number='1',
                 rn=None, checkbox=True,
                 level='blue',
                 notif_type='without',
                 header=f'test time: {time}',
                 text='CP/AdminRights/Check "Send Notification" button',
                 bname=None,
                 blink=None
                 )
]
