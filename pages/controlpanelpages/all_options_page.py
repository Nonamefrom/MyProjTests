import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait as wait
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
    ADD_NEW_OPTION = (By.XPATH, '//span[@class="sa-button__content"]')
    VIEW_NEXT_OPTIONS_PAGE = (By.XPATH, '//span[5]')


    def __init__(self, driver, url):
        super().__init__(driver, url)

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

    @allure.step("Переход на следующую страницу опций")
    def click_view_next_page(self):
        self.click(self.VIEW_NEXT_OPTIONS_PAGE)

#Поиск и клик по наименованию опции, даты окончания действия, статусу публикации
    @allure.step("Поиск элемента и клик элемента опции")
    def find_element_of_option(self, elem):
        find_locator = f'//div[contains(text(),"{elem}")]'
        self.element_is_visible((By.XPATH, find_locator), timeout=5)
        self.click((By.XPATH, find_locator), timeout=5)

#Только поиск перехода на следующую страницу
    def find_view_next_page(self):
        self.element_is_visible(self.VIEW_NEXT_OPTIONS_PAGE)
        return True

#Только поиск элемента опции на странице по введенному параметру
    def check_element_of_option(self, elem):
        find_locator = f'//div[contains(text(),"{elem}")]'
        self.element_is_visible((By.XPATH, find_locator), timeout=5)
        return True

#Функция перебора страниц в поиске элемента опции,
    def find_option(self, elem):
        while True:
            try:
                if self.check_element_of_option(elem):
                    self.find_element_of_option(elem)
                    break  # Выходим из цикла, если элемент найден
            except TimeoutException:
                if self.find_view_next_page():
                    self.click_view_next_page()
                else:
                    raise Exception(f"Элемент '{elem}' не найден")

