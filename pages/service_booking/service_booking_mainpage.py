import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class Service_BookingMainPage(BasePage):
    H1_TEXT = (By.XPATH, '//span[@class="text-h1-bold"]')

    @allure.step("Получение текста заголовка Н1")
    def sb_h1_text(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.H1_TEXT)).text
        return phrase
