import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AllOptionsCpPage(BasePage):
    FILTER_DRDWN = (By.XPATH, '//div[@class="options-filters__filter mb-6 mr-4"]//div[@class="sa-select__simple-text"]')
    ANY_STATUS = (By.XPATH, '//span[contains(text(),"Любой статус")]')
    ACTUAL_STATUS = (By.XPATH, '//span[contains(text(),"Только актуальные")]')
    ENDED_STATUS = (By.XPATH, '//span[contains(text(),"Только завершенные")]')
    SORT_DRDWN = (By.XPATH, '//div[@class="options-filters__filter mb-6"]//div[@class="sa-select__simple-text"]')
    DATE_START_DESC = (By.XPATH, '//span[contains(text(),"Дата старта (от старых к новым)")]')
    DATE_START_ASC = (By.XPATH, '//span[contains(text(),"Дата старта (от новых к старым)")]')
    DATE_END_DESC = (By.XPATH, '//span[contains(text(),"Дата окончания (от старых к новым)")]')
    DATE_END_ASC = (By.XPATH, '//span[contains(text(),"Дата окончания (от новых к старым)")]')
    ADD_NEW_OPTION = (By.XPATH, '//button[@type="button"]')
    H1_TEXT = (By.XPATH, '//span[@class="text-h1"]')

    @allure.step("Получение текста заголовка Н1")
    def cp_h1_text(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.H1_TEXT)).text
        return phrase

    @allure.step("Включить фильтр Любой статус опции")
    def click_filter_anystatus(self):
        self.click(self.FILTER_DRDWN)
        self.click(self.ANY_STATUS)

    @allure.step("Включить фильтр Активные опции")
    def click_filter_actualstatus(self):
        self.click(self.FILTER_DRDWN)
        self.click(self.ACTUAL_STATUS)

    @allure.step("Включить фильтр Завершенные опции")
    def click_filter_endedstatus(self):
        self.click(self.FILTER_DRDWN)
        self.click(self.ENDED_STATUS)

    @allure.step("Включить по дате старта сорт. от старых к новым опциям")
    def click_sort_startdate_desc(self):
        self.click(self.SORT_DRDWN)
        self.click(self.DATE_START_DESC)

    @allure.step("Включить по дате старта сорт. от новых к старым опциям")
    def click_sort_startdate_asc(self):
        self.click(self.SORT_DRDWN)
        self.click(self.DATE_START_ASC)

    @allure.step("Включить по дате окончания сорт. от старых к новым опциям")
    def click_sort_enddate_desc(self):
        self.click(self.SORT_DRDWN)
        self.click(self.DATE_END_DESC)

    @allure.step("Включить по дате окончания сорт. от новых к старым опциям")
    def click_sort_enddate_asc(self):
        self.click(self.SORT_DRDWN)
        self.click(self.DATE_END_ASC)

    @allure.step("Создать/Добавить новую опцию")
    def click_add_new_option(self):
        self.click(self.ADD_NEW_OPTION)
