import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class InfoTab(BasePage):
    ACTIVE = '[@class="sa-tab--route-active sa-tab--exact-route-active sa-tab sa-tab--active"]'
    NOT_ACTIVE = '[@class="sa-tab"]'
    # Вкладка 0: "Информация"
    INFO_TAB = (By.XPATH, '//*[@data-qa="option-tab-4"]')
    INFO_TAB_NOT_ACTIVE = (By.XPATH, f'//*{NOT_ACTIVE}[@data-qa="option-tab-4"]')
    INFO_TAB_ACTIVE = (By.XPATH, f'//*{ACTIVE}[@data-qa="option-tab-4"]')
