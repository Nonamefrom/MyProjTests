import time
from typing import Tuple

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from steps.common_steps import CommonSteps as cs


class AdminTab(BasePage):
    TAB_ACTIVE = "sa-tab--route-active sa-tab--exact-route-active sa-tab sa-tab--active"
    TAB_NOT_ACTIVE = "sa-tab"
    # Вкладка 4: Администрирование
    ADMIN_TAB_ID = (By.XPATH, '//*[@data-qa="option-tab-4"]')
    ADMIN_TAB_NAME = 'Администрирование'
    ADMIN_TAB_NOT_ACTIVE = (By.XPATH, '//*[@class="sa-tab"][@data-qa="option-tab-4"]')
    ADMIN_TAB_ACTIVE = (
        By.XPATH, '//*[@class="sa-tab--route-active sa-tab--exact-route-active sa-tab sa-tab--active"]'
                  '[@data-qa="option-tab-4"]')
    # Кнопка "Синхронизация с парусом" для нажатия и для проверки активна/не активна
    SYNC_BUTTON = (By.XPATH, '//*[@data-qa="sync-parus-btn"]')
    SYNC_BUTTON_ACTIVE = (
        By.XPATH, '//*[@data-qa="sync-parus-btn"]'
                  '[@class="sa-button sa-button--active sa-button--size--md sa-button--theme--primary"]')
    SYNC_BUTTON_DISABLE = (
        By.XPATH, '//*[@data-qa="sync-parus-btn"]'
                  '[@class="sa-button sa-button--disabled sa-button--size--md sa-button--theme--primary"]')
    # Статус активной и отключенной кнопки Синхронизации с Парусом
    SYNC_BUTTON_ACTIVE_VALUE = "sa-button sa-button--active sa-button--size--md sa-button--theme--primary"
    SYNC_BUTTON_DISABLE_VALUE = "sa-button sa-button--disabled sa-button--size--md sa-button--theme--primary"

    @allure.step("Проверка наличия кнопки 'Администрирование' в ПВЗ")
    def tab_status(self):
        time.sleep(0.5)  # Необходимая задержка для смены статуса вкладки 0.1 а 0.5 ради перестраховки
        value = (wait(self.driver, timeout=5).
                 until(EC.visibility_of_element_located(self.ADMIN_TAB)).get_attribute('class'))
        # print(value)  # для отладки
        if value == self.TAB_NOT_ACTIVE:
            return False
        elif value == self.TAB_ACTIVE:
            return True
        else:
            raise ValueError(value)  # Что бы увидеть что нам вернулось значение, которое не прошло по условиям

    @allure.step("Проверка состояние кнопки синхронизации с Парусом по классу кнопки")
    def sync_button_class(self):
        value = self.get_attribute_value(self.SYNC_BUTTON, 'class')
        if value == self.SYNC_BUTTON_DISABLE_VALUE:
            return False
        elif value == self.SYNC_BUTTON_ACTIVE_VALUE:
            return True
        else:
            raise ValueError(value)  # Что бы увидеть что нам вернулось значение, которое не прошло по условиям

    @allure.step("Клик по вкладке 'Администрирование' в ПВЗ")
    def admin_tab(self):
        self.click(self.ADMIN_TAB_ID)

    @allure.step("Проверка состояния кнопки синхронизации с Парусом")
    def sync_button_status(self):
        disabled = self.disabled(self.SYNC_BUTTON, 'class')
        active = self.activated(self.SYNC_BUTTON, 'class')
        # print(f'disabled: {disabled}\n active: {active}')
        if (disabled is True) and (active is False):
            return False
        elif (disabled is False) and (active is True):
            return True

    @allure.step("Нажатие кнопки синхронизации с Парусом")
    def press_sync_button(self):
        self.click(self.SYNC_BUTTON)
