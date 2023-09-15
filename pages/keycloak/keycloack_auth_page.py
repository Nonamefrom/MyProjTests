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

    @allure.step("Ввод текста в поля и нажатие кнопки авторизоваться")
    def login(self, email, password):
        self.fill_text(self.NAME_BAR, email)
        self.fill_text(self.PASSWORD_BAR, password)
        self.click(self.SUBMIT_BUTTON)

    @allure.step("Получение текста сообщения валидации при неверных CRUD")
    def error_message(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text
        return phrase

    @allure.step("Получение текста title страницы")
    def is_title_correct(self, expected_title):
        return expected_title == self.driver.title
