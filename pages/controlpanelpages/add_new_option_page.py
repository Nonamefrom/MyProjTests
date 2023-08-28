import time

import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class AddNewOptionCpPage(BasePage):
    LINK_TO_ALL_OPTIONS = (By.XPATH, '//span[contains(text(),"Все опции")]')
    INPUT_OPTION_NAME = (By.XPATH, '(//input[@type="text"])[1]')
    DRDWN_OPTION_TYPE = (By.XPATH, '(//input[@type="text"])[2]')
    SET_STANDART_SERVICE = (By.XPATH, '//span[contains(text(),"Стандартный сервис")]')
    SET_ONLINE_RECORD_SERVICE = (By.XPATH, '//span[contains(text(),"Сервис онлайн записи")]')
    SET_CODES_SERVICE = (By.XPATH, '//span[contains(text(),"Сервис кодов")]')
    SET_EDUCATION_SERVICE = (By.XPATH, '//span[contains(text(),"Сервис обучения")]')
    SET_FTS_NOKIAN_SERVICE = (By.XPATH, '//span[contains(text(),"Бшм nokian")]')
    SET_FTS_CORDIANT_SERVICE = (By.XPATH, '//span[contains(text(),"Бшм cordiant")]')
    SET_FTS_VIATTI_SERVICE = (By.XPATH, '//span[contains(text(),"Бшм viatti")]')
    SET_WARRANTY_SERVICE = (By.XPATH, '//span[contains(text(),"Расширенная гарантия")]')
    CHCKBX_AUTOLIMIT_DISABLE = (By.XPATH, '(//label[contains(text(),"Включить автолимиты")])[1]')
    SET_PWZ_SERVICE = (By.XPATH, '//span[contains(text(),"Пункт выдачи заказов")]')
    SET_STARTDATE_OPTION = (By.XPATH, '(//input[@type="datetime-local"])[1]')
    SET_ENDDATE_OPTION = (By.XPATH, '(//input[@type="datetime-local"])[2]')
    INPUT_MAINTEXT_OPTION = (By.XPATH, '//div[@class="ProseMirror"]')
    RADIO_CHECK_NOTIF_OFF = (By.XPATH, '//input[@value="false"]')
    RADIO_CHECK_NOTIF_ON = (By.XPATH, '//input[@value="true"]')
    NOTIF_FOR_CLIENT = (By.XPATH, '(//input[@type="text"])[3]')
    ERROR_NOTIF_CLIENT = (By.XPATH, '(//div[contains(text(),"Заполните текст уведомления")])')
    NOTIF_LIFETIME = (By.XPATH, '//input[@placeholder="000:00:00"]')
    MANAGER_MAILS = (By.XPATH, '(//input[@type="text"])[5]')
    MANAGER_ERROR = (By.XPATH,
                     '//div[@class="option-form__notification-emails"]//div[@class="sa-input__messages-wrapper"]//div[1])')

    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step("Вернутся на экран Опций")
    def go_to_all_option(self):
        self.click(self.LINK_TO_ALL_OPTIONS)

    @allure.step("Ввод названия опции")
    def input_option_name(self, text):
        self.fill_text(self.INPUT_OPTION_NAME, text)

    @allure.step("Выбрать стандартный сервис опции")
    def set_standart_option_type(self):
        self.click(self.DRDWN_OPTION_TYPE)
        self.click(self.SET_STANDART_SERVICE)

    @allure.step("Выбрать Онлайн запись")
    def set_online_record_type(self):
        self.click(self.DRDWN_OPTION_TYPE)
        self.click(self.SET_ONLINE_RECORD_SERVICE)

    @allure.step("Выбрать Сервис кодов")
    def set_service_code_type(self):
        self.click(self.DRDWN_OPTION_TYPE)
        self.click(self.SET_CODES_SERVICE)

    @allure.step("Выбрать сервис обучения")
    def set_education_option_type(self):
        self.click(self.DRDWN_OPTION_TYPE)
        self.click(self.SET_EDUCATION_SERVICE)

    @allure.step("Выбрать сервис БШМ Нокиан")
    def set_fts_nokian_type(self):
        self.click(self.DRDWN_OPTION_TYPE)
        self.click(self.SET_FTS_NOKIAN_SERVICE)

    @allure.step("Выбрать сервис БШМ Кордиант")
    def set_fts_cordiant_type(self):
        self.click(self.DRDWN_OPTION_TYPE)
        self.click(self.SET_FTS_CORDIANT_SERVICE)

    @allure.step("Выбрать сервис БШМ Виатти")
    def set_fts_viatti_type(self):
        self.click(self.DRDWN_OPTION_TYPE)
        self.click(self.SET_FTS_VIATTI_SERVICE)

    @allure.step("Выбрать сервис гарантии")
    def set_warranty_type(self):
        self.click(self.DRDWN_OPTION_TYPE)
        self.click(self.SET_WARRANTY_SERVICE)

    @allure.step("Выключение автолимита гарантии")
    def disable_autolimit_warranty(self):
        self.click(self.CHCKBX_AUTOLIMIT_DISABLE)

    @allure.step("Выбрать сервис ПВЗ")
    def set_pwz_type(self):
        self.click(self.DRDWN_OPTION_TYPE)
        self.click(self.SET_PWZ_SERVICE)

    @allure.step("Ввод старта действия опции")
    def input_start_date(self, text):
        self.fill_text(self.SET_STARTDATE_OPTION, text)

    @allure.step("Ввод окончания действия опции")
    def input_end_date(self, text):
        self.fill_text(self.SET_ENDDATE_OPTION, text)

    @allure.step("Ввод текста опции")
    def input_maintext_option(self, text):
        self.fill_text(self.INPUT_MAINTEXT_OPTION, text)

    @allure.step("Включение Сообщения пользователям")
    def enable_massage_users(self):
        self.click(self.RADIO_CHECK_NOTIF_OFF)

    @allure.step("Выключение Сообщения пользователям")
    def disable_massage_users(self):
        self.click(self.RADIO_CHECK_NOTIF_ON)

    @allure.step("Установка отображения Сообщения пользователям")
    def input_massage_users(self, text):
        self.fill_text(self.NOTIF_FOR_CLIENT, text)

#Требует отладки
    @allure.step("Установка времени отображения Сообщения пользователям")
    def set_viewtime_massage_users(self, text):
        try:
            element = wait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.NOTIF_LIFETIME)            )
            element.click()
            for digit in text:
                element.send_keys(digit)
                time.sleep(1)
        except Exception as e:
            print(f"An error occurred: {e}")

    @allure.step("Установка почты менеджеров")
    def set_managers_mail(self, text):
        self.fill_text(self.MANAGER_MAILS, text)

    @allure.step("Получение текста при пустующем поле Сообщения клиентов")
    def error_empty_massage_clients(self):
        phrase = wait.until(EC.visibility_of_element_located(self.ERROR_NOTIF_CLIENT)).text
        return phrase

    @allure.step("Получение текста при невалидных мейлах менеджеров")
    def error_empty_massage_clients(self):
        phrase = wait.until(EC.visibility_of_element_located(self.ERROR_NOTIF_CLIENT)).text
        return phrase
