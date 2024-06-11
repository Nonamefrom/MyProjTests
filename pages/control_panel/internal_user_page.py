import allure
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from pages.base_page import BasePage


class InternalUserPage(BasePage):
    H1_INTERNAL = (By.XPATH, '//span[@class="text-h1"]')
    BUBBLE_MASSAGE = (By.XPATH, '//*[@data-qa="add-new-user-btn"]')
    CALL_MODAL_MENU = (By.XPATH, '//span[@class="sa-button__content"]')
    NAME_INPUT = (By.XPATH, '//*[@data-qa="first-name-input"]//input')
    LAST_NAME_INPUT = (By.XPATH, '//*[@data-qa="last-name-input"]//input')
    EMAIL_INPUT = (By.XPATH, '//*[@data-qa="email-input"]//input')
    SET_CP_ACCESS = (By.XPATH, '//*[@data-qa="control-panel-group-checkbox"]')
    SET_SB_ACCESS = (By.XPATH, '//*[@data-qa="online-record-group-checkbox"]')
    SAVE_INTERNAL = (By.XPATH, '//*[@data-qa="save-btn"]')
    CLOSE_MODAL = (By.XPATH, '//*[@data-qa="cancel-btn"]')
    ERROR_NAME = (By.XPATH, '//*[@data-qa="first-name-input"]//*[@class="sa-input__message"]')
    ERROR_LAST_NAME = (By.XPATH, '//*[@data-qa="last-name-input"]//*[@class="sa-input__message"]')
    ERROR_MAIL = (By.XPATH, '//*[@data-qa="email-input"]//*[@class="sa-input__message"]')
    DELETE_USER = (By.XPATH, '//*[@data-qa="delete-user-btn"]')

    @allure.step("Заголовок Н1 страницы internal")
    def get_h1_internal_user_page(self):
        phrase = wait(self.driver, 3).until(EC.visibility_of_element_located(self.H1_INTERNAL)).text
        return phrase

    @allure.step("Проверка Отображения клавиши добавления")
    def check_add_button(self):
        try:
            if self.element_is_visible(self.CALL_MODAL_MENU):
                return True
        except:
            return False

    @allure.step("Вызов модалки добавления internal")
    def call_modal_menu(self):
        self.click(self.CALL_MODAL_MENU)
        return self

    @allure.step("Ввод имени")
    def input_name(self, text):
        self.fill_text(self.NAME_INPUT, text)
        return self

    @allure.step("Ввод фамилии")
    def input_last_name(self, text):
        self.fill_text(self.LAST_NAME_INPUT, text)
        return self

    @allure.step("Ввод мейла")
    def input_email(self, text):
        self.fill_text(self.EMAIL_INPUT, text)
        return self

    @allure.step("Клик доступ к Панели управления")
    def set_access_cp(self):
        self.click(self.SET_CP_ACCESS)
        return self

    @allure.step("Клик доступ к Онлайн записи")
    def set_sb_access(self):
        self.click(self.SET_SB_ACCESS)
        return self

    @allure.step("Клик 'Добавить/Сохранить/Удалить сотрудника'")
    def save_internal(self):
        self.click(self.SAVE_INTERNAL)
        return self

    @allure.step("Закрыть модалку ввода данных")
    def close_modal(self, text):
        self.fill_text(self.CLOSE_MODAL, text)
        return self

    @allure.step("Получение текста ошибки Поля 'Имя'")
    def error_empty_name(self):
        phrase = wait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.ERROR_NAME)).text
        return phrase

    @allure.step("Получение текста ошибки Поля 'Фамилия'")
    def error_empty_last_name(self):
        phrase = wait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.ERROR_LAST_NAME)).text
        return phrase

    @allure.step("Получение текстa ошибки mail'a")
    def error_mail_massage(self):
        phrase = wait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.ERROR_MAIL)).text
        return phrase

    @allure.step("Клик удалить пользователя в окне редактирования")
    def delete_internal(self):
        self.click(self.DELETE_USER)
        return self

    @allure.step("Подтверждение удаления")
    def accept_delete_employee(self):
        self.click(self.SAVE_INTERNAL)
        self.driver.refresh()
        return self

    @allure.step("Получаем текст из бабл-уведолмения")
    def get_bubble_text(self):
        phrase = wait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.BUBBLE_MASSAGE)).text
        return phrase

    @allure.step("Добавление сотрудника")
    def add_internal(self, name, last_name, email):
        self.input_name(name)
        self.input_last_name(last_name)
        self.input_email(email)
        self.save_internal()

