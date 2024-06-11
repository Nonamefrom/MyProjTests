import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class PartnerLandingPage(BasePage):
    FAKE_AUTH = (By.XPATH, '//div[@class="row dev-login"]//*[@type="button"]')
    LOGO = (By.XPATH, '//*[@data-qa="index-page"]')
    H1_TEXT = (By.XPATH, '//span[@class="yellow"]')
    FAKE_LOGIN_BUTTON = (By.XPATH, '// button[ @ type = "submit"]')
    FAKE_SELECTOR = (By.XPATH, '//select[@aria-label="Default select example"]')
    FAKE_SELECTOR_ROW = (By.XPATH, '//select[@aria-label="Default select example"]//option')

    @allure.step("Проверка присутствия ЛОГО 'Точка движения'")
    def check_logo_partner_landing(self):
        try:
            self.element_is_visible(self.LOGO)
            return True
        except TimeoutException:
            return False

    @allure.step("Переход в MIMFaker")
    def login_partner_with_faker(self, rn=None):
        self.click(self.FAKE_AUTH)
        # Если rn == None, то мы не выбираем, а сразу жмём "логин" с тем что выбрано
        if rn is not None:
            rn = int(rn)  # вдруг пришёл не инт, а строка
            self.select_by_rn_in_faker(rn)

        self.click(self.FAKE_LOGIN_BUTTON)

    @allure.step("Проверка отображения кнопки MIMFaker")
    def check_mimfaker_button(self):
        try:
            self.element_is_visible(self.FAKE_AUTH)
            return True
        except TimeoutException:
            return False

    # Метод авторизации независимо от окружения
    def login_all_env(self, pages, rn=None):
        """Сюда надо передать фикстуру для работы"""
        check = self.check_mimfaker_button()
        if check is True:
            self.login_partner_with_faker(rn)  # через фейкер, если есть клавиша

        else:
            pages.mim_page.login_with_mim(pages)  # через мим, если нет клавиши

    def select_by_rn_in_faker(self, rn=None):
        row = self.FAKE_SELECTOR_ROW
        elements = self.elements_are_visible(row)
        l = len(elements)
        for i in range(1, l + 1):
            text = self.get_text((By.XPATH, f'//select[@aria-label="Default select example"]//option[{i}]'))
            text = text[:-1].split('(')
            if int(text[1]) == rn:
                self.click((By.XPATH, f'//select[@aria-label="Default select example"]//option[{i}]'))
                break
