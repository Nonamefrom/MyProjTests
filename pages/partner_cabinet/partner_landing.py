import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class PartnerLandingPage(BasePage):
    FAKE_AUTH = (By.XPATH,
                 '//a[@class="ml-2 sa-button sa-button--active sa-button--size--md sa-button--theme--primary"]')
    H1_TEXT = (By.XPATH, '//span[@class="yellow"]')
    FAKE_LOGIN_BUTTON = (By.XPATH, '// button[ @ type = "submit"]')

    @allure.step("Получение текста заголовка Н1")
    def partner_landing_h1_text(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.H1_TEXT)).text
        return phrase

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
