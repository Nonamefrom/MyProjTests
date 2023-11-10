import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class TopBarCabinetPage(BasePage):
    LINK_TO_MAIN_PAGE = (By.XPATH, '//a[@class="base-header__titles nuxt-link-active"]')
    REGION = (By.XPATH, '//a[@href="/profile/me"]//span')
    PHONE_COMPANY = (By.XPATH, '//span[normalize-space()="8(800)100-77-00"]')
    OPEN_PROFILE_DROPDOWN = (By.XPATH, '//span[contains(text(),"Профиль")]')
    LINK_TO_PROFILE_PAGE = (By.XPATH, '//div[contains(text(),"Мои данные")]')
    DEAUTH_BUTTON = (By.XPATH, '//div[contains(text(),"Выход из приложения")]')

    @allure.step("Открытие дропдауна профиль в КУ")
    def open_profile_dropdown(self):
        self.click(self.OPEN_PROFILE_DROPDOWN)
        return self

    @allure.step("Клик кнопки выйти - деавторизация")
    def click_deauth_button(self):
        self.click(self.DEAUTH_BUTTON)
        return self

    @allure.step("Переход на главную в КУ")
    def go_mainpage_cabinet(self):
        self.click(self.LINK_TO_MAIN_PAGE)
        return self

    @allure.step("Переход в профиль пользователя КУ")
    def open_profile_user_cabinet(self):
        self.click(self.LINK_TO_PROFILE_PAGE)
        return self

    @allure.step("Взять значение Регион")
    def get_region(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.REGION)).text
        return phrase

    @allure.step("Взять значение телефон")
    def get_phone(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.REGION)).text
        return phrase
