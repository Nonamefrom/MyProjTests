import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class PromocodeTab(BasePage):
    ACTIVE = '[@class="sa-tab--route-active sa-tab--exact-route-active sa-tab sa-tab--active"]'
    NOT_ACTIVE = '[@class="sa-tab"]'
    # Вкладка 2: "Доп.информация"
    ADDITIONAL_TAB = (By.XPATH, '//*[@data-qa="option-tab-4"]')
    ADDITIONAL_TAB_NOT_ACTIVE = (By.XPATH, f'//*{NOT_ACTIVE}[@data-qa="option-tab-4"]')
    ADDITIONAL_TAB_ACTIVE = (By.XPATH, f'//*{ACTIVE}[@data-qa="option-tab-4"]')
    ADDITIONAL_TAB_H3 = (By.XPATH, '//*[@class="option-additional-page"]//*[@class="text-h3-bold mb-3"]')

    @allure.step("Получение текста заголовка Н3 вкладки Доп.информация")
    def additional_tab_h3_text(self):
        wait = WebDriverWait(self.driver, self.base_timeout)
        phrase = wait.until(EC.visibility_of_element_located(self.ADDITIONAL_TAB_H3)).text
        return phrase
