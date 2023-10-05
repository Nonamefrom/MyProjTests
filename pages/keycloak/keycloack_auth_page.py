import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    @allure.step("Ввод текста в поля и нажатие кнопки авторизоваться")
    def login(self, email, password):
        self.fill_text(self.NAME_BAR, email)
        self.fill_text(self.PASSWORD_BAR, password)
        self.click(self.SUBMIT_BUTTON)

    @allure.step("Переход - велком стр., клик сотрудник ОЗ, ввод мейла и пароля")
    def login_sb_b2b(self, email, password):
        self.click(self.WELCOME_SB_BUTTON)
        self.click(self.B2B_USER_BUTTON)
        self.fill_text(self.NAME_BAR, email)
        self.fill_text(self.PASSWORD_BAR, password)
        self.click(self.SUBMIT_BUTTON)

    @allure.step("Переход - велком стр., клик оператор ОЗ, ввод мейла и пароля")
    def login_sb_internal(self, email, password):
        self.click(self.WELCOME_SB_BUTTON)
        self.click(self.INTERNAL_USER_BUTTON)
        self.fill_text(self.NAME_BAR, email)
        self.fill_text(self.PASSWORD_BAR, password)
        self.click(self.SUBMIT_BUTTON)

    @allure.step("Переход - велком стр., клик сотрудник ПВЗ, ввод мейла и пароля")
    def login_b2b(self, email, password):
        self.click(self.B2B_USER_BUTTON)
        self.fill_text(self.NAME_BAR, email)
        self.fill_text(self.PASSWORD_BAR, password)
        self.click(self.SUBMIT_BUTTON)

    @allure.step("Переход - велком стр., клик оператор ПВЗ, ввод мейла и пароля")
    def login_internal(self, email, password):
        self.click(self.INTERNAL_USER_BUTTON)
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
    def is_title_correct(self, expected_title):
        return expected_title == self.driver.title

    @allure.step("Получение текста ошибки несовпадения вводимых паролей")
    def error_pass_are_diff(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.PASS_ARE_DIFF)).text
        return phrase

    @allure.step("Отображение переходов b2b или internal")
    def check_b2b_internal_buttons(self):
        self.element_is_visible(self.B2B_USER_BUTTON)
        self.element_is_visible(self.INTERNAL_USER_BUTTON)
