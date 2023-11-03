import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class KeycloackAuthForm(BasePage):
    NAME_BAR = (By.XPATH, '//input[@name="username"]')
    PASSWORD_BAR = (By.XPATH, '//input[@name="password"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@value="Submit"]')
    FORGOT_PASS = (By.XPATH, '//span[contains(text(),"Забыли пароль?")]')
    REMEMBER_ME = (By.XPATH, '//div[@name="rememberMe"]')
    ERROR_MESSAGE = (By.XPATH, '//div[@class="sa-input__message"]')
    RECOVERY_MAIL = (By.XPATH, '//input[@type="text"]')
    RETURN_TO_MAIN = (By.XPATH, '//span[contains(text(),"Не нужно, я вспомнил")]')
    SUBMIT_RECOVERY = (By.XPATH, '//button[@type="submit"]')
    NEW_PASS = (By.XPATH, '//input[@name="password-new"]')
    REPEAT_NEW_PASS = (By.XPATH, '//input[@name="password-confirm"]')
    SAVE_NEW_PASS = (By.XPATH, '//span[@class="sa-button__content"]')
    PASS_ARE_DIFF = (By.XPATH, '//div[contains(text(),"Пароли не совпадают.")]')
    WELCOME_SB_BUTTON = (By.XPATH, '//a[@href="/auth/login"]')
    B2B_USER_BUTTON = (By.XPATH, '(//button)[1]')
    INTERNAL_USER_BUTTON = (By.XPATH, '(//button)[2]')
    H1_AUTH_PAGE = ((By.XPATH, '(//h1)[1]'))

    @allure.step("Ввод текста в поля и нажатие кнопки авторизоваться")
    def login(self, email, password):
        self.fill_text(self.NAME_BAR, email)
        self.fill_text(self.PASSWORD_BAR, password)
        self.click(self.SUBMIT_BUTTON)

    @allure.step("Переход на форму восстановления мейла")
    def click_forgot_pass(self):
        self.click(self.FORGOT_PASS)

    @allure.step("Ввод мейла для восстановления")
    def input_recovery_mail(self, email):
        self.fill_text(self.NAME_BAR, email)
        self.click(self.SUBMIT_RECOVERY)

    @allure.step("Возврат на главный экран КК")
    def click_return_to_main(self):
        self.click(self.RETURN_TO_MAIN)

    @allure.step("Получение текста сообщения валидации при неверных CRUD")
    def error_message(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text
        return phrase

    @allure.step("Восстановление: Ввод нового и повтор пароля, клик сохранение")
    def accept_pass_for_restore(self, new_pass):
        self.fill_text(self.NEW_PASS, new_pass)
        self.fill_text(self.REPEAT_NEW_PASS, new_pass)
        self.click(self.SAVE_NEW_PASS)

    @allure.step("Восстановление: Ввод разных паролей восстановления, клик сохранение")
    def input_different_pass(self, new_pass, wrong_pass):
        self.fill_text(self.NEW_PASS, new_pass)
        self.fill_text(self.REPEAT_NEW_PASS, wrong_pass)
        self.click(self.SAVE_NEW_PASS)

    @allure.step("Получение текста title страницы")
    def check_auth_title(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.PASS_ARE_DIFF)).text
        return phrase

    @allure.step("Получение текста ошибки несовпадения вводимых паролей")
    def error_pass_are_diff(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.PASS_ARE_DIFF)).text
        return phrase

    # При успешном проходе возвращает None, его проверять в assert
    @allure.step("Отображение кнопок b2b или internal")
    def check_b2b_internal_buttons(self):
        try:
            self.element_is_visible(self.B2B_USER_BUTTON)
            self.element_is_visible(self.INTERNAL_USER_BUTTON)
            return True
        except TimeoutException:
            return False

    @allure.step("Получение текста заголовка Н1")
    def auth_h1_text(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.H1_AUTH_PAGE)).text
        return phrase

    def go_to_login(self, role):
        if not self.check_b2b_internal_buttons():
            # Если кнопки не найдены, кликаем на WELCOME_SB_BUTTON
            self.click(self.WELCOME_SB_BUTTON)
        if role == "b2b":
            self.click(self.B2B_USER_BUTTON)
        elif role == "internal":
            self.click(self.INTERNAL_USER_BUTTON)
        else:
            print("Недопустимая роль пользователя, или кнопки недоступны.")
        return self
