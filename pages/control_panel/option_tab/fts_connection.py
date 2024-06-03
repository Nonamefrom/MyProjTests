import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class FtsConnection(BasePage):
    ACTIVE = '[@class="sa-tab--route-active sa-tab--exact-route-active sa-tab sa-tab--active"]'
    NOT_ACTIVE = '[@class="sa-tab"]'
    # Вкладка привязки расширенной гарантии к БШМ
    FTS_TAB = (By.XPATH, '//*[@data-qa="option-tab-6"]')
    FTS_TAB_ACTIVE = (By.XPATH, f'//*{ACTIVE}[@data-qa="option-tab-6"]')
    FTS_TAB_NOT_ACTIVE = (By.XPATH, f'//*{NOT_ACTIVE}[@data-qa="option-tab-6"]')
    FTS_TAB_CORDIANT = (By.XPATH, '//*[@data-qa="option-tab-4"]')
    FTS_TAB_CORDIANT_ACTIVE = (By.XPATH, f'//*{ACTIVE}[@data-qa="option-tab-4"]')
    FTS_TAB_CORDIANT_NOT_ACTIVE = (By.XPATH, f'//*{NOT_ACTIVE}[@data-qa="option-tab-4"]')

    FTS_TAB_H1 = (By.XPATH, '//*[@class="text-h1-bold"]')
    FTS_TAB_NAME = 'Привязка расширенной гарантии'
    FTS_TAB_H3 = (By.XPATH, '//div[@class="text-h3-bold mb-4"]')
    FTS_TAB_LINK_BUTTON = (By.XPATH, '//button[@data-qa="connect-warranty-btn"]')
    FTS_TAB_LINK_BUTTON_NAME = 'Связать'

    @allure.step('Получение текста заголовка Н3 вкладки "Привязка РГ"')
    def fts_connection_tab_h3_text(self):
        wait = WebDriverWait(self.driver, self.base_timeout)
        phrase = wait.until(EC.visibility_of_element_located(self.ADDITIONAL_TAB_H3)).text
        return phrase

    @allure.step('Проверка наличия и состояния кнопки связывания бшм с рг')
    def link_button_is_present(self):
        active = self.activated(self.FTS_TAB_LINK_BUTTON, 'class')
        disabled = self.disabled(self.FTS_TAB_LINK_BUTTON, 'class')
        if active is True:
            return True
        elif disabled is True:
            opt_name = self.get_text(self.FTS_TAB_H1)
            if 'cordiant' in opt_name.lower():
                return True

    @allure.step('Проверка наличия и работы вкладки связывания бшм с рг')
    def link_to_warranty_tab_present(self):
        opt_name = self.get_text(self.FTS_TAB_H1)
        try:
            if 'cordiant' in opt_name.lower():
                if self.element_is_visible(self.FTS_TAB_CORDIANT_NOT_ACTIVE):
                    self.click(self.FTS_TAB_CORDIANT)
                    if self.element_is_visible(self.FTS_TAB_CORDIANT_ACTIVE):
                        if self.element_is_visible(self.FTS_TAB_LINK_BUTTON):
                            return True
            else:
                if self.element_is_visible(self.FTS_TAB_NOT_ACTIVE):
                    self.click(self.FTS_TAB)
                    if self.element_is_visible(self.FTS_TAB_ACTIVE):
                        if self.element_is_visible(self.FTS_TAB_LINK_BUTTON):
                            return True
        except:
            return False
