# -*- coding: utf-8 -*-
from model.notification import Notification
from pages.control_panel.notification import NotificationPage

testdata = [
    # Так как список РН партнёров может состоять только из цифр и запятых - этот набор данных для проверки их комбинаций
    Notification(number='1', notif_type='with', blink='partner.svrauto.ru/options/5/info'),  #
    Notification(number='2', notif_type='with', blink='//partner.svrauto.ru/options/5/info'),  #
    Notification(number='3', notif_type='with', blink='/partner.svrauto.ru/options/5/info'),  #
    Notification(number='4', notif_type='with', blink='htt://partner.svrauto.ru/options/5/info'),  #
    Notification(number='5', notif_type='with', blink='ht://partner.svrauto.ru/options/5/info'),  #
    Notification(number='6', notif_type='with', blink='h://partner.svrauto.ru/options/5/info'),  #
    Notification(number='7', notif_type='with', blink='https://partner.svrauto. ru/options/5/info'),  #
    Notification(number='8', notif_type='with', blink='https://partner.svrauto.ru/ options/5/info'),  #
    Notification(number='9', notif_type='with', blink='https://partner.svra uto.ru/options/5/info'),  #
    Notification(number='10', notif_type='with', blink='https://par tner.svrauto.ru/options/5/info')  #
]
