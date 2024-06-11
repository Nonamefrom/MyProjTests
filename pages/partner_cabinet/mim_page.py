import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data.test_data import RegData


MIM_LOGIN = RegData.MIM_LOGIN
MIM_PASS = RegData.MIM_PASS


class MimAuthPage(BasePage):
    FORM_LOGIN = (By.XPATH, '//input[@name="login"]')
    FORM_PASS = (By.XPATH, '//input[@name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')
    H1_LOGIN_PAGE = (By.XPATH, '//h1[contains(text(),"Войдите в МИМ")]')
    H1_MIM_PAGE = (By.XPATH, '//span[contains(text(),"МИМ")]')
    GO_TO_PARTNER_CABINET = (By.XPATH, '//a[contains(text(),"Кабинет услуг")]')

    @allure.step("Ввод текста в поля и нажатие кнопки Войти")
    def login_with_mim(self, pages):
        pages.mim_page.open()
        auth_mim_h1 = pages.mim_page.check_auth_title()
        assert auth_mim_h1 == 'Войдите в МИМ', f"Expected '{auth_mim_h1}' but got other H1"
        self.fill_text(self.FORM_LOGIN, MIM_LOGIN)
        self.fill_text(self.FORM_PASS, MIM_PASS)
        self.click(self.LOGIN_BUTTON)
        mim_h1 = pages.mim_page.check_mim_title()
        assert mim_h1 == 'МИМ', f"Expected '{mim_h1}' but got other H1"
        self.click(self.GO_TO_PARTNER_CABINET)
        return self

    @allure.step("Получение текста H1 авторизации МИМ")
    def check_auth_title(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.H1_LOGIN_PAGE)).text
        return phrase

    @allure.step("Получение текста H1 страницы МИМ")
    def check_mim_title(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.H1_MIM_PAGE)).text
        return phrase
