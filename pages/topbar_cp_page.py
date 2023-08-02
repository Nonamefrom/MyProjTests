import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class TopBarCpPage(BasePage):
    LINK_TO_MAIN_PAGE = (By.XPATH, '//span[@class="base-header__title web text-h3"]')
    OPEN_PROFILE_DROPDOWN = (By.XPATH, '//h4[@class="base-header-profile__title"]')
    LINK_TO_PROFILE_PAGE = (By.XPATH, '//div[@class="menu__item-text text-h4-bold mr-3"]')
    DEAUTH_BUTTON = (By.XPATH, '//div[@class="menu__item-text text-h4-bold mr-3 red"]')

    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step("Открытие дропдауна профиль в ПУ")
    def click_open_profile_dropdown(self):
        self.click(self.OPEN_PROFILE_DROPDOWN)
        return self

    @allure.step("Клик кнопки выйти - деавторизация")
    def click_deauth_button(self):
        self.click(self.DEAUTH_BUTTON)
        return self

    @allure.step("Переход на главную в ПУ")
    def click_open_mainpage_controlpanel(self):
        self.click(self.LINK_TO_MAIN_PAGE)
        return self

    @allure.step("Переход в профиль пользователя ПУ")
    def click_open_profile_user_controlpanel(self):
        self.click(self.LINK_TO_PROFILE_PAGE)
        return self
