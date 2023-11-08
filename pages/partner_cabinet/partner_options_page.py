import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class PartnerOptionsPage(BasePage):
    H1_TEXT = (By.XPATH, '//span[contains(text(),"Доступные опции")]')

    @allure.step("Получение текста заголовка Н1")
    def partner_cabinet_h1_text(self):
        wait = WebDriverWait(self.driver, 5)
        phrase = wait.until(EC.visibility_of_element_located(self.H1_TEXT)).text
        return phrase
# Стартовый набор локаторов и методов, необходимых для проверки авторизации, в дальнейшем будет расширено
