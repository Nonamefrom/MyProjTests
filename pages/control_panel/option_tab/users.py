import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class UsersTab(BasePage):
    ACTIVE = '[@class="sa-tab--route-active sa-tab--exact-route-active sa-tab sa-tab--active"]'
    NOT_ACTIVE = '[@class="sa-tab"]'
    # Вкладка 1: "Пользователи"
    USERS_TAB = (By.XPATH, '//*[@data-qa="option-tab-4"]')
    USERS_TAB_NOT_ACTIVE = (By.XPATH, f'//*{NOT_ACTIVE}[@data-qa="option-tab-4"]')
    USERS_TAB_ACTIVE = (By.XPATH, f'//*{ACTIVE}[@data-qa="option-tab-4"]')
    USERS_TAB_H3 = (By.XPATH, '//*[@class="option-page-users"]//div//div[@class="text-h3-bold"]')
    USERS_OPEN_ROWS = (By.XPATH, '//*[@data-qa="open-users-row-btn"]')

    @allure.step("Получение текста заголовка Н3 вкладки Пользователи")
    def users_h3_text(self):
        wait = WebDriverWait(self.driver, self.base_timeout)
        phrase = wait.until(EC.visibility_of_element_located(self.USERS_TAB_H3)).text
        return phrase
