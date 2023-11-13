import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class ProfilePageCabinet(BasePage):
    H1 = (By.XPATH, '//div[contains(text(),"Профиль")]')
    REGION_NAME = (By.XPATH, '//*[@data-qa="region-name"]')
    EDIT_REGION = (By.XPATH, '//*[@data-qa="region-edit"]')
    REGION_BAR = (By.XPATH, '//input[@placeholder="Введите название"]')
    LOGIN_BAR = (By.XPATH, '//*[@data-qa="login"]')
    USER_NAME_BAR = (By.XPATH, '//*[@data-qa="user-name"]')
    MAIL_BAR = (By.XPATH, '//*[@data-qa="email"]//input')
    REGISTRATION_DATE_BAR = (By.XPATH, '//*[@data-qa="user-created-at"]')
    CANCEL_BUTTON = (By.XPATH, '//*[@data-qa="cansel"]')
    SAVE_BUTTON = (By.XPATH, '//*[@data-qa="submit"]')
    ERROR_MAIL_VALID = (By.XPATH, '//div[@class="sa-input__message"]')

    @allure.step("Заголовок Н1 страницы")
    def get_h1_profile(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.H1)).text
        return phrase

    @allure.step("Заголовок Н1 страницы")
    def get_header_text(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.REGION_NAME)).text
        return phrase

    @allure.step("Ввод региона в поле")
    def set_region(self, text):
        self.click(self.EDIT_REGION)
        self.fill_text(self.REGION_BAR, text)
        region_input = f'//span[contains(text(),"{text}")]'
        self.click((By.XPATH, region_input), timeout=5)
        return self

    @allure.step("Ввод меил")
    def set_mail(self, text):
        self.fill_text(self.MAIL_BAR, text)
        return self

    @allure.step("Сохранение изменений в профиле")
    def save_change_profile(self):
        self.click(self.SAVE_BUTTON)
        return self

    @allure.step("Взять значение Регион")
    def get_region(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.REGION_NAME)).text
        return phrase

    @allure.step("Текст валидации мейла")
    def get_error_mail(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.ERROR_MAIL_VALID)).text
        return phrase

    @allure.step("Меил из поля страницы профиля")
    def get_mail(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.MAIL_BAR))
        return element.get_attribute("value")
