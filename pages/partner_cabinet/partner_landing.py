import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class PartnerLandingPage(BasePage):
    FAKE_AUTH = (By.XPATH, '//div[@class="row dev-login"]//*[@type="button"]')
    LOGO = (By.XPATH, '//*[@data-qa="index-page"]')
    FAKE_LOGIN_BUTTON = (By.XPATH, '// button[ @ type = "submit"]')

    @allure.step("Проверка присутствия ЛОГО 'Точка движения'")
    def check_logo_partner_landing(self):
        try:
            self.element_is_visible(self.LOGO)
            return True
        except TimeoutException:
            return False

    @allure.step("Переход в MIMFaker")
    def login_partner_throw_faker(self):
        self.click(self.FAKE_AUTH)
        self.click(self.FAKE_LOGIN_BUTTON)
        return self

    @allure.step("Проверка отображения кнопки MIMFaker")
    def check_mimfaker_button(self):
        try:
            self.element_is_visible(self.FAKE_AUTH)
            return True
        except TimeoutException:
            return False

#Метод авторизации независимо от окружения
    def login_all_env(self, pages):
        check = pages.cabinet_landing_page.check_mimfaker_button()
        if check is True:
            pages.cabinet_landing_page.login_partner_throw_faker()#через фейкер, если есть клавиша
        else:
            pages.mim_page.login_throw_mim(pages)#через мим, если нет клавиши
