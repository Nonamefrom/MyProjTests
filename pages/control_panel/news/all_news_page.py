import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class AllNewsPage(BasePage):
    H1_TEXT = (By.XPATH, '//div[@class="col text-h1-bold"]')
    ADD_NEW = (By.XPATH, '//span[contains(text(),"Добавить")]')

    @allure.step("Получение текста заголовка Н1")
    def news_h1_text(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.H1_TEXT)).text
        return phrase

    @allure.step("Клик добавить новую")
    def click_add_new(self):
        self.click(self.ADD_NEW)
