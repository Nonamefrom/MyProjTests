import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from steps.common_steps import CommonSteps
from pages.base_page import BasePage


class PwzOptionPage(BasePage):

    base_timeout = 10
    OPTION_NAME_H1 = (By.XPATH, '//*[@class="col option-page__option-header"]//*[@class="text-h1-bold"]')
    ADMIN_TAB = (By.XPATH, '//*[@data-qa="option-tab-4"]')

    @allure.step("Получение текста заголовка Н1")
    def pwz_h1_text(self):
        wait = WebDriverWait(self.driver, self.base_timeout)
        phrase = wait.until(EC.visibility_of_element_located(self.OPTION_NAME_H1)).text
        return phrase

    def admin_tab_status(self):
        self.admin.get_tab_status()













