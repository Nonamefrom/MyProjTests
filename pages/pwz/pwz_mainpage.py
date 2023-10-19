import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class PWZMainPage(BasePage):
    PWZ_PAGE_H1_TEXT = (By.XPATH, '//div[contains(text(),"Список заказов")]')

    @allure.step("Получение текста заголовка Н1")
    def pwz_h1_text(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.PWZ_PAGE_H1_TEXT)).text
        return phrase
# Стартовый набор локаторов и методов, необходимых для проверки авторизации, в дальнейшем будет расширено
