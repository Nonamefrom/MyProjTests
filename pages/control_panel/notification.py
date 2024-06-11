import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from model.notification import Notification


class NotificationPage(BasePage):
    # Текст на странице "Уведомления"
    TEXT_H1 = 'Уведомления'  # тут почему-то нет пробелов хотя в локаторе они есть, там: ' Уведомления '
    TEXT_H1_LOC = By.XPATH, '//span[@class="text-h1"][contains(text(),"Уведомления")]'
    TEXT_H3 = 'Уведомления для партнеров в «Кабинете услуг»'  # аналогично н1
    TEXT_H3_LOC = By.XPATH, '//div[contains(text(),"Уведомления для партнеров в «Кабинете услуг»")]'
    # Кнопки на странице уведомлений ПУ
    ADD_BUTTON_TEXT = 'ДОБАВИТЬ'  # аналогично н1, только тут капсом
    ADD_BUTTON = By.XPATH, '//*[@data-qa="add-new-notification-btn"]'
    ADD_BUTTON_TEXT_LOC = By.XPATH, '//*[@data-qa="add-new-notification-btn"]//*[@class="sa-button__content"]'
    # Кнопки редактировать/просмотр и отправить
    EDIT_BUTTON_LOC = By.XPATH, '//*[@class="sa-icon sa-icon--name--Edit"]'
    SEND_BUTTON_LOC = By.XPATH, '//*[@class="sa-icon sa-icon--name--MailInbox"]'
    # Модалка с добавлением/изменением/просмотром нотификейшена
    MODAL_TEXT_H3 = By.XPATH, '//*[@class="sa-side-modal__header text-h3-bold"]'
    # Поле ввода RN Партнёров
    # #брать [1] после фикса дублей локаторов
    RN_FIELD_NAME_TEXT = 'RN партнеров'
    RN_FIELD_HINT_TEXT = 'Через запятую, пример: «4762932,23498348,234372»'
    RN_FIELD_NAME = By.XPATH, '//*[@data-qa="rn-id-input"][1]//*[@class="sa-input__label"]'
    RN_FIELD_LOC = By.XPATH, '//*[@data-qa="rn-id-input"][1]//input'
    RN_FIELD_ACTIVE = ('sa-input sa-input--size--md sa-input--component--input sa-input--status--error '
                       'sa-input--full-width mb-5')
    RN_FIELD_DISABLED = ('sa-input sa-input--size--md sa-input--component--input sa-input--status--error '
                         'sa-input--disabled sa-input--full-width mb-5')
    RN_FIELD_HINT_LOC = By.XPATH, '//*[@data-qa="rn-id-input"]//*[@class="sa-input__message"]'
    RN_ERROR_LOC = By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div'
    # Чекбокс "Отправить уведомлением всем партнёрам"
    SEND_TO_ALL_CHKBOX_NAME = 'Отправить уведомление всем партнерам'
    SEND_TO_ALL_CHKBOX_LOC = By.XPATH, '//*[@class="sa-checkbox__control"]'
    SEND_TO_ALL_CHKBOX_STATE = By.XPATH, '//*[@class="sa-checkbox__box"]//div//input[@type="checkbox"]'
    SEND_TO_ALL_CHKBOX_NAME_LOC = By.XPATH, '//div[@class="sa-checkbox__box"]//label[@class="sa-checkbox__label"]'
    # Поле выбора цвета(уровня) уведомления
    LEVEL_FIELD_NAME = 'Цвет уведомления'
    LEVEL_FILED_NAME_LOC = By.XPATH, '//div[@class="notification-data"]//div[3]//label'
    LEVEL_FIELD_LOC = By.XPATH, '//div[@class="notification-data"]//div[3]//div[@class="sa-select__input-wrapper"]//input'
    LEVEL_BLUE_TEXT = 'Синий (обычное уведомление)'
    LEVEL_BLUE_LOC = By.XPATH, '//div[@class="v-popper__inner"]//div//ul//li[1]//span'
    LEVEL_YELLOW_TEXT = 'Желтый (важное уведомление)'
    LEVEL_YELLOW_LOC = By.XPATH, '//*[@class="v-popper__inner"]//div//ul//li[2]//span'
    LEVEL_RED_TEXT = 'Красный (очень важное уведомление)'
    LEVEL_RED_LOC = By.XPATH, '//div[@class="v-popper__inner"]//div//ul//li[3]//span'
    LEVEL_ERROR_LOC = By.XPATH, '//div[@class="notification-data"]//div[3]//div[@class="sa-select__message"]'  # обязательное поле
    # Поле выбора типа уведомления (с кнопкой или без)
    TYPE_FIELD_NAME = 'Тип уведомления'
    TYPE_FIELD_NAME_LOC = By.XPATH, '//div[@class="notification-data"]//div[4]//label'
    TYPE_FIELD_LOC = By.XPATH, '//div[@class="notification-data"]//div[4]//div[@class="sa-select__input-wrapper"]//input'
    TYPE_ONLY_TEXT_TEXT = 'Заголовок с текстом'
    TYPE_ONLY_TEXT_LOC = By.XPATH, '//div[@class="notification-data"]//div[4]//div[@aria-hidden="false"]//li[1]'
    TYPE_TEXT_AND_BUTTON_TEXT = 'Заголовок с текстом и кнопкой'
    TYPE_TEXT_AND_BUTTON_LOC = By.XPATH, '//div[@class="notification-data"]//div[4]//div[@aria-hidden="false"]//li[2]'
    TYPE_ERROR_LOC = By.XPATH, '//div[@class="notification-data"]//div[4]//div[@class="sa-select__message"]'  # обязательное поле
    # Поле ввода заголовка уведомления
    HEADER_FIELD_NAME = 'Заголовок уведомления'
    HEADER_FIELD_NAME_LOC = By.XPATH, '//div[@class="notification-data"]//div[5]//label'
    HEADER_FIELD_LOC = By.XPATH, '//div[@data-qa="rn-id-input"][2]//input'
    HEADER_ERROR_LOC = By.XPATH, '//div[@class="notification-data"]//div[5]//div[@class="sa-input__message"]'  # Обязательное поле
    # Поле ввода текста уведомления
    NOTIFICATION_TEXT_FIELD_NAME = 'Текст уведомления'
    NOTIFICATION_TEXT_FIELD_NAME_LOC = By.XPATH, '//div[@class="notification-data"]//div[6]//label'
    TEXT_FIELD_LOC = By.XPATH, '//div[@data-qa="rn-id-input"][3]//input'
    NOTIFICATION_TEXT_FIELD_ERROR = By.XPATH, ''  # Не обязательное поле
    # Поле ввода текста на кнопке
    BTN_NAME_NAME = 'Текст на кнопке'  # name of field button name
    BTN_NAME_NAME_LOC = By.XPATH, '//div[@class="notification-data"]//div[7]//div[1]//label'
    BTN_NAME_HINT = 'Пример: «Открыть»'
    BTN_NAME_HINT_LOC = By.XPATH, '//div[@class="notification-data"]//div[7]//div[1]//div[2]/div'
    BTN_TEXT_FIELD_LOC = By.XPATH, '//div[7]/div[1]/div[1]/input[@class="sa-input__input"]'
    BTN_TEXT_ERROR_LOC = By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[7]/div[1]/div[2]/div'  # Обязательное поле
    # Поле ввода ссылки перехода при нажатии на кнопку
    BTN_LINK_NAME = 'Ссылка'
    BTN_LINK_NAME_LOC = By.XPATH, '//div[@class="notification-data"]//div[7]//div[2]//label'
    BTN_LINK_HINT = 'Пример: «https://partner.svrauto.ru/options/5/info»'
    BTN_LINK_HINT_LOC = By.XPATH, '//div[@class="notification-data"]//div[7]//div[2]//div[2]/div'
    BTN_LINK_FIELD_LOC = By.XPATH, '//div/div[7]/div[2]/div[1]/input[@class="sa-input__input"]'
    BTN_LINK_ERROR_LOC = By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[7]/div[2]/div[2]/div'  # Обязательное поле
    # Внизу 2 кнопки отменить и добавить/сохранить
    CANCEL_BUTTON_LOC = By.XPATH, '//*[@data-qa="cancel-btn"]'
    SAVE_BUTTON_LOC = By.XPATH, '//*[@data-qa="save-btn"]'

    # ПУ ВКЛАДКА "УВЕДОМЛЕНИЯ" ОШИБКИ
    RN_OR_CHCKBOX = 'Поле RN партнеров обязательно'
    RN_INVALID_FORMAT = 'Поле "ID партнеров" имеет ошибочный формат'
    LEVEL_IS_MANDATORY = 'Поле "Уровень" обязательно для заполнения'
    TYPE_IS_MANDATORY = 'Поле "Тип" обязательно для заполнения'
    HEADER_IS_MANDATORY = 'Поле "Заголовок" обязательно для заполнения'
    BTN_NAME_IS_MANDATORY = 'Поле "Текст кнопки" обязательно для заполнения'
    BTN_NAME_LENGTH = 'Количество символов в поле "Текст кнопки" не может превышать 20'
    BTN_LINK_IS_MANDATORY = 'Поле "Ссылка кнопки" обязательно для заполнения'
    BTN_LINK_WRONG_FORMAT = 'Поле "Ссылка кнопки" имеет ошибочный формат'
    SNACKBAR_NOTIFICATION_LOC = (By.XPATH, '//div[@class="sa-snackbar__title"]')
    SNACK_ERROR_INCORRECT_TEXT = 'Указанные данные некорректны'
    SNACK_CREATE_SUCCESS_TEXT = 'Уведомление успешно создано'
    SNACK_SAVE_SUCCESS_TEXT = 'Уведомление успешно обновлено'
    SNACK_SEND_SUCCESS_TEXT = 'Уведомление отправлено'
    SNACK_SENT_EARLIER_TEXT = 'Уведомление уже было отправлено ранее'
    # СТАТУСЫ УВЕДОМЛЕНИЙ: СОЗДАНО, ОТПРАВЛЕНО
    NOTIFICATION_STATUS_SENT = 'Отправлено'
    NOTIFICATION_STATUS_CREATED = 'Создано'

    @allure.step('Проверка текста Н1 на странице уведомлений')
    def h1_text_check(self) -> bool:
        h1 = self.get_text(self.TEXT_H1_LOC)
        # print(h1)
        if h1 == self.TEXT_H1:
            return True
        else:
            raise AttributeError(f'H1 text is differ from expected: "{h1}"')

    @allure.step('Проверка текста Н3 на странице уведомлений')
    def h3_text_check(self) -> bool:
        h3 = self.get_text(self.TEXT_H3_LOC)
        if h3 == self.TEXT_H3:
            return True
        else:
            raise AttributeError(f'H3 text is differ from expected: "{h3}"')

    @allure.step('Проверка наличия кнопки "Добавить" на странице уведомлений')
    def add_button_presence(self) -> bool:
        if self.element_is_visible(self.ADD_BUTTON):
            text = self.get_text(self.ADD_BUTTON_TEXT_LOC)
            if text == self.ADD_BUTTON_TEXT:
                return True
            else:
                raise AttributeError(f'button text is differ from expected: "{text}"')

    @allure.step('Проверка кликабельности кнопки "Добавить" на странице уведомлений')
    def add_button_clickable(self) -> bool:
        if self.element_is_clickable(self.ADD_BUTTON) is not False:
            return True
        elif self.element_is_clickable(self.ADD_BUTTON) is False:
            return False

    @allure.step('Проверка открытия модалки нового уведомления при нажатии на "Добавить"')
    def open_modal(self):
        """Открыть модалку через "ДОБАВИТЬ" """
        self.click(self.ADD_BUTTON)

    @allure.step('Нажатие Добавить/Сохранить изменения в модалке уведомления"')
    def save(self):
        """Кнопка СОХРАНИТЬ/ДОБАВИТЬ на модалке уведомления"""
        self.click(self.SAVE_BUTTON_LOC)
        time.sleep(0.5)

    @allure.step('Нажатие кнопки Отменить на модалке уведомления')
    def cancel(self):
        """Кнопка ОТМЕНИТЬ на модалке уведомления"""
        self.click(self.CANCEL_BUTTON_LOC)

    @allure.step('Проверка открытия модалки нового уведомления при нажатии на "Добавить"')
    def modal_opening_check(self) -> bool:
        """Проверка открытия привязана к отображению кнопок Отменить и Сохранить на модалке"""
        self.open_modal()
        if self.element_is_clickable(self.CANCEL_BUTTON_LOC) is not False:
            if self.element_is_clickable(self.SAVE_BUTTON_LOC) is not False:
                return True
            else:
                raise AttributeError(f'"{self.SAVE_BUTTON_LOC}" is not clickable')
        else:
            raise AttributeError(f'"{self.CANCEL_BUTTON_LOC}" is not clickable')

    @allure.step('Проверка чекбокса "Отправить всем"')
    def checkbox_rn_is_enable(self):
        """Если стоит - то Тру, если не стоит - Фолс"""
        try:
            if self.element_is_present(self.SEND_TO_ALL_CHKBOX_STATE).get_attribute("value") == 'false':
                # print(self.element_is_present(self.SEND_TO_ALL_CHKBOX_STATE).get_attribute("value"))
                return False
            elif self.element_is_present(self.SEND_TO_ALL_CHKBOX_STATE).get_attribute("value") == 'true':
                # print(self.element_is_present(self.SEND_TO_ALL_CHKBOX_STATE).get_attribute("value"))
                return True
            else:
                raise ValueError(f'smth wrong with checkbox value: "{value}"')
        except:
            raise AttributeError('smth go wrong in checkbox_rn_is_enable, can"t take "value"')

    @allure.step('Выбор "Тип уведомления"')
    def type_select(self, select=None):
        """Выбирает Цвет(Уровень):
        None / ничего не ставим в скобках => отмена выбора в селекторе
        "without" => Заголовок с текстом
        "with" => Заголовок с текстом и кнопкой"""
        self.click(self.TYPE_FIELD_LOC)
        if select is not None:
            if select == 'without':
                self.click(self.TYPE_ONLY_TEXT_LOC)
            elif select == 'with':
                self.click(self.TYPE_TEXT_AND_BUTTON_LOC)
        else:
            actual_choice = self.element_is_present(self.TYPE_FIELD_LOC).get_attribute('placeholder')
            if actual_choice == self.TYPE_ONLY_TEXT_TEXT:
                self.click(self.TYPE_ONLY_TEXT_LOC)
            elif actual_choice == self.TYPE_TEXT_AND_BUTTON_TEXT:
                self.click(self.TYPE_TEXT_AND_BUTTON_LOC)

    @allure.step('Выбор "Цвет уведомления"')
    def level_select(self, select=None):
        """Выбирает Цвет(Уровень):
        None / ничего не ставим в скобках => отмена выбора
        "blue" => Синий (обычное уведомление)
        "yellow" => Желтый (важное уведомление)
        "red" => Красный (очень важное уведомление)"""
        # time.sleep(1)
        self.click(self.LEVEL_FIELD_LOC)
        if select is not None:
            if select == 'blue':
                self.click(self.LEVEL_BLUE_LOC)
            elif select == 'yellow':
                self.click(self.LEVEL_YELLOW_LOC)
            elif select == 'red':
                self.click(self.LEVEL_RED_LOC)
        else:
            actual_choice = self.element_is_present(self.LEVEL_FIELD_LOC).get_attribute('placeholder')
            if actual_choice == self.LEVEL_BLUE_TEXT:
                self.click(self.LEVEL_BLUE_LOC)
            elif actual_choice == self.LEVEL_YELLOW_TEXT:
                self.click(self.LEVEL_YELLOW_LOC)
            elif actual_choice == self.LEVEL_RED_TEXT:
                self.click(self.LEVEL_RED_LOC)

    @allure.step('Читаем ошибку из нотификейшена в снекбаре')
    def get_snack_result(self):
        """incorrect - ошибка некорректного сохранения
        created - сообщение об успешном создании
        saved - сообщение об успешном сохранении
        sent - сообщение об успешной отправке
        earlier - ошибка отправки так как было отправлено ранее"""
        text = self.get_text(self.SNACKBAR_NOTIFICATION_LOC)
        # print(text)
        if text == self.SNACK_ERROR_INCORRECT_TEXT:
            return 'incorrect'
        elif text == self.SNACK_CREATE_SUCCESS_TEXT:
            return 'created'
        elif text == self.SNACK_SAVE_SUCCESS_TEXT:
            return 'saved'
        elif text == self.SNACK_SEND_SUCCESS_TEXT:
            return 'sent'
        elif text == self.SNACK_SENT_EARLIER_TEXT:
            return 'earlier'
        else:
            raise ValueError(f'Неизвестный текст в : "{text}" в "get_snack_result"')

    def wait_till_snack_disappear(self):
        return self.element_is_not_visible(self.SNACKBAR_NOTIFICATION_LOC, 7)


    @allure.step('Смотрим ошибку под полем ввода РН')
    def get_rn_error(self):
        text = self.get_text(self.RN_ERROR_LOC)
        if text == self.RN_OR_CHCKBOX:
            return 'empty'
        elif text == self.RN_INVALID_FORMAT:
            return 'incorrect'
        elif text == self.RN_FIELD_HINT_TEXT:
            # Если ошибки нет - по тому же локатору находится подсказка под полем
            return False
        else:
            raise ValueError(f'Неизвестный текст подсказки: "{text}" под полем ввода РН')

    @allure.step('Смотрим ошибку под полем выбора Уровня уведомления')
    def get_level_error(self):
        try:
            text = self.get_text(self.LEVEL_ERROR_LOC)
            if text == self.LEVEL_IS_MANDATORY:
                return 'empty'
            else:
                raise ValueError(f'Неизвестный текст ошибки: "{text}" в "get_level_error"')
        except:
            return False

    @allure.step('Смотрим ошибку под полем выбора Типа уведомления')
    def get_type_error(self):
        try:
            text = self.get_text(self.TYPE_ERROR_LOC)
            if text == self.TYPE_IS_MANDATORY:
                return 'empty'
            else:
                raise ValueError(f'Неизвестная ошибка под полем ввода РН "{text}" в "get_type_error"')
        except:
            return False

    @allure.step('Смотрим ошибку под полем ввода Заголовка уведомления')
    def get_header_error(self):
        try:
            text = self.get_text(self.HEADER_ERROR_LOC)
            if text == self.HEADER_IS_MANDATORY:
                return 'empty'
            if text == self.HEADER_INCORRECT:
                return 'incorrect'
            else:
                raise ValueError(f'Неизвестная ошибка заголовка "{text}" в "get_header_error"')
        except:
            return False

    @allure.step('Смотрим ошибку под полем ввода текста на кнопке уведомления')
    def get_btn_text_error(self):
        text = self.get_text(self.BTN_TEXT_ERROR_LOC)
        if text == self.BTN_NAME_IS_MANDATORY:
            return 'empty'
        if text == self.BTN_NAME_LENGTH:
            return 'length'
        elif text == self.BTN_NAME_HINT:
            return False
        else:
            raise ValueError(f'Неизвестное значение text: "{text}" в "get_btn_text_error"')

    @allure.step('Смотрим ошибку под полем ввода ссылки на кнопке уведомления')
    def get_btn_link_error(self):
        text = self.get_text(self.BTN_LINK_ERROR_LOC)
        if text == self.BTN_LINK_IS_MANDATORY:
            return 'empty'
        elif text == self.BTN_LINK_WRONG_FORMAT:
            return 'incorrect'
        elif text == self.BTN_LINK_HINT:
            return False
        else:
            raise ValueError(f'Неизвестное значение text: "{text}" в "get_btn_link_error"')

    @allure.step('Установка/Снятие чекбокса "Отправить всем"')
    def checkbox_rn(self, action=False):
        """Ставит или убирает чекбокс в зависимости от того что надо сделать.
         None - без чекбокса
         True - с чекбоксом
         click - будет нажиматься чекбокс независимо от того поставлен чекбокс или нет"""
        time.sleep(0.5)
        actual = self.checkbox_rn_is_enable()
        # print(actual)
        if action == 'click':
            self.click(self.SEND_TO_ALL_CHKBOX_LOC)
        elif (action is True) and (actual is False):
            self.click(self.SEND_TO_ALL_CHKBOX_LOC)
        elif (action is True) and (actual is True):
            pass
        elif (action is False) and (actual is True):
            self.click(self.SEND_TO_ALL_CHKBOX_LOC)
        elif (action is False) and (actual is False):
            pass
        else:
            raise ValueError(f'Неизвестное значение action: "{action}" в "checkbox_rn"')

    @allure.step('Заполнение уведомления')
    def fill_notification(self, notification):
        """Заполнение формы уведомления"""
        # Вводим перечень rn если есть
        if notification.rn is not None:
            self.fill_text(self.RN_FIELD_LOC, notification.rn)
        # Ставим чекбокс "Отправить всем" если есть
        self.checkbox_rn(notification.checkbox)
        # Выбор уровня(Цвета уведомления)
        if notification.level is not None:
            self.level_select(notification.level)
        # Выбор Типа уведомления
        if notification.notif_type is not None:
            self.type_select(notification.notif_type)
        # Вводим Заголовок уведомления если есть
        if notification.header is not None:
            self.fill_text(self.HEADER_FIELD_LOC, notification.header)
        # Вводим Текст уведомления если есть
        if notification.text is not None:
            self.fill_text(self.TEXT_FIELD_LOC, notification.text)
        # Если уведомление с кнопкой или без:
        if notification.notif_type in ('with', 'without'):
            # вводим текст на кнопке и ссылку на кнопке
            if notification.bname is not None:
                self.fill_text(self.BTN_TEXT_FIELD_LOC, notification.bname)
            if notification.blink is not None:
                self.fill_text(self.BTN_LINK_FIELD_LOC, notification.blink)
        elif notification.notif_type is None:
            pass
        else:
            raise ValueError(f'Неизвестное значение notification.notif_type: "{notification.notif_type}" '
                             f'в "fill_notification"')

    @allure.step('Поиск кнопки отправки уведомления по заголовку и статусу')
    def find_send_button_by_header_and_status(self, status, header):
        """Поиск уведомления по заголовку и статусу('created' или 'sent') уведомления"""
        if status == 'created':
            state = self.NOTIFICATION_STATUS_CREATED
        elif status == 'sent':
            state = self.NOTIFICATION_STATUS_SENT
        else:
            raise ValueError(f'Неизвестное значение status: "{status}"')
        try:
            row = By.XPATH, '//tbody[@class="sa-table-content"]//tr'
            elements = self.elements_are_visible(row)
        except:
            elements = []
        count = len(elements)
        if count > 0:
            for i in range(1, count + 1):
                if ((header == self.get_text((By.XPATH, f'//tbody[@class="sa-table-content"]//tr[{i}]//td[2]//span')))
                    and (state == self.get_text(
                        (By.XPATH, f'//tbody[@class="sa-table-content"]//tr[{i}]//td[5]//div')))):
                    self.click((By.XPATH, f'//tbody[@class="sa-table-content"]//tr[{i}]//td[6]//button[2]'))
                    break
        else:
            return False

    @allure.step('Поиск кнопки редактирования уведомления по заголовку и статусу')
    def find_edit_button_by_header_and_status(self, status, header):
        """Поиск уведомления по заголовку и статусу('created' или 'sent') уведомления"""
        if status == 'created':
            state = self.NOTIFICATION_STATUS_CREATED
        elif status == 'sent':
            state = self.NOTIFICATION_STATUS_SENT
        else:
            raise ValueError(f'Неизвестное значение status: "{status}"')
        try:
            row = By.XPATH, '//tbody[@class="sa-table-content"]//tr'
            elements = self.elements_are_visible(row)
        except:
            elements = []
        count = len(elements)
        if count > 0:
            for i in range(1, count + 1):
                if ((header == self.get_text((By.XPATH, f'//tbody[@class="sa-table-content"]//tr[{i}]//td[2]//span')))
                    and (state == self.get_text(
                        (By.XPATH, f'//tbody[@class="sa-table-content"]//tr[{i}]//td[5]//div')))):
                    self.click((By.XPATH, f'//tbody[@class="sa-table-content"]//tr[{i}]//td[6]//button[1]'))
                    break
        else:
            return False

    @allure.step('Читаем данные с модалки уведомления')
    def read_notification(self):
        rn = self.get_attribute_value(self.RN_FIELD_LOC, 'value')
        if rn == '':
            rn = None
        checkbox = self.checkbox_rn_is_enable()
        level = self.get_attribute_value(self.LEVEL_FIELD_LOC, 'placeholder')
        if level == self.LEVEL_BLUE_TEXT:
            level = 'blue'
        elif level == self.LEVEL_YELLOW_TEXT:
            level = 'yellow'
        elif level == self.LEVEL_RED_TEXT:
            level = 'red'
        else:
            raise ValueError(f'Неизвестный тип уведомления: {level}')
        notif_type = self.get_attribute_value(self.TYPE_FIELD_LOC, 'placeholder')
        if notif_type == self.TYPE_ONLY_TEXT_TEXT:
            notif_type = 'without'
        elif notif_type == self.TYPE_TEXT_AND_BUTTON_TEXT:
            notif_type = 'with'
        else:
            raise ValueError(f'Неизвестный тип уведомления: {notif_type}')
        header = self.get_attribute_value(self.HEADER_FIELD_LOC, 'value')
        text = self.get_attribute_value(self.TEXT_FIELD_LOC, 'value')
        bname, blink = None, None
        if notif_type == 'with':
            bname = self.get_attribute_value(self.BTN_TEXT_FIELD_LOC, 'value')
            blink = self.get_attribute_value(self.BTN_LINK_FIELD_LOC, 'value')

        notification = (Notification(rn=rn, checkbox=checkbox, level=level, notif_type=notif_type, header=header,
                                     text=text, bname=bname, blink=blink))
        return notification
