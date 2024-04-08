import time

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TopBarCpPage(BasePage):
    LINK_TO_MAIN_PAGE = (By.XPATH, '//*[@data-qa="index-page-link"]')
    OPEN_PROFILE_DROPDOWN = (By.XPATH, '//*[@data-qa="toggle-profile-menu"]')
    OPEN_PROFILE_DROPDOWN_PWZ = (By.XPATH, '//*[@class="base-header-profile__content"]')
    LINK_TO_PROFILE_PAGE = (By.XPATH, '//*[@data-qa="profile-link"]')
    DEAUTH_BUTTON = (By.XPATH, '//*[@data-qa="logout-btn"]')
    DEAUTH_BUTTON_PWZ = (By.XPATH, '//*[@class="sa-icon sa-icon--name--Exit"]')

    @allure.step("Открытие дропдауна профиль в ПУ")
    def click_open_profile_dropdown(self):
        if (self.link_end_with('/orders') is True) or (self.link_end_with('/appointments') is True):
            self.click(self.OPEN_PROFILE_DROPDOWN_PWZ)
            return self
        else:
            self.click(self.OPEN_PROFILE_DROPDOWN)
            return self

    @allure.step("Клик кнопки выйти - деавторизация")
    def click_deauth_button(self):
        time.sleep(0.0001)
        if (self.link_end_with('/orders') is True) or (self.link_end_with('/appointments') is True):
            self.click(self.DEAUTH_BUTTON_PWZ)
            return self
        else:
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
