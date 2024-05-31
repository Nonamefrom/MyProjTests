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
    # Синее уведомление  / с рн / без чекбокса / без кнопки
    Notification(number='1',
                 rn="123", checkbox=False,
                 level='blue',
                 notif_type='without',
                 header=f'test time: {time}',
                 text="с рн без чекбокса синее без кнопки",
                 bname=None,
                 blink=None
                 )
    # Желтое уведомление  / без рн / с чекбоксом / без кнопки
    , Notification(number='2',
                   rn=None, checkbox=True,
                   level='blue',
                   notif_type='without',
                   header=f'test time: {time}',
                   text='без рн с чекбоксом желтое без кнопки ',
                   bname=None,
                   blink=None
                   )
    # Красное уведомление  / с рн / с чекбоксом / без кнопки
    , Notification(number='3',
                   rn="123", checkbox=True,
                   level='blue',
                   notif_type='without',
                   header=f'test time: {time}',
                   text='с рн и чекбоксом красное без кнопки',
                   bname=None,
                   blink=None
                   )
    # Синее уведомление  / с рн / без чекбокса / с кнопкой
    , Notification(number='4',
                   rn="123", checkbox=False,
                   level='blue',
                   notif_type='with',
                   header=f'test time: {time}',
                   text='рн без чекбокса синее с кнопкой',
                   bname='не нажимай',
                   blink='https://partner.svrauto.ru'
                   )
    # Желтое уведомление  / без рн / с чекбоксом / с кнопкой
    , Notification(number='5',
                   rn=None, checkbox=True,
                   level='yellow',
                   notif_type='with',
                   header=f'test time: {time}',
                   text='без рн с чекбоксом желтое с кнопкой',
                   bname='не нажимай',
                   blink='https://partner.svrauto.ru'
                   )
    # Красное уведомление  / с рн / с чекбоксом / с кнопкой
    , Notification(number='6',
                   rn="123,124,125", checkbox=True,
                   level='red',
                   notif_type='with',
                   header=f'test time: {time}',
                   text='с рн и чекбоксом красное с кнопкой',
                   bname='не нажимай',
                   blink='https://partner.svrauto.ru'
                   )

]
