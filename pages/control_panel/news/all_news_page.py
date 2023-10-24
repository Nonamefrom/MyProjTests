import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from utils.exceptions.not_found_exception import NotFoundException

class AllNewsPage(BasePage):
    H1_TEXT = (By.XPATH, '//div[@class="col text-h1-bold"]')
    ADD_NEW = (By.XPATH, '//span[contains(text(),"Добавить")]')
    VIEW_NEXT_NEWS_PAGE = (By.XPATH, '//span[8]')

    @allure.step("Получение текста заголовка Н1")
    def news_h1_text(self):
        wait = WebDriverWait(self.driver, 10)
        phrase = wait.until(EC.visibility_of_element_located(self.H1_TEXT)).text
        return phrase

    @allure.step("Клик добавить новую")
    def click_add_new(self):
        self.click(self.ADD_NEW)

    @allure.step("Переход на следующую страницу новостей")
    def click_view_next_page(self):
        self.click(self.VIEW_NEXT_NEWS_PAGE)

#Поиск и клик по наименованию опции, даты окончания действия, статусу публикации
    @allure.step("Поиск новости по заголовку")
    def find_new_by_name(self, elem):
        find_locator = f'//div[contains(text(),"{elem}")]'
        self.element_is_visible((By.XPATH, find_locator), timeout=5)
        self.click((By.XPATH, find_locator), timeout=5)

    @allure.step("Поиск последней новости по дате публикации")
    def find_new_by_date(self, elem):
        find_locator = f'(//div[contains(text(),"{elem}")])[1]'
        self.element_is_visible((By.XPATH, find_locator), timeout=5)
        self.click((By.XPATH, find_locator), timeout=5)

    #Только поиск перехода на следующую страницу
    def find_view_next_page(self):
        self.element_is_visible(self.VIEW_NEXT_NEWS_PAGE)
        return True

    # Только поиск по имени новости
    def check_new_by_name(self, elem):
        find_locator = f'//div[contains(text(),"{elem}")]'
        self.element_is_visible((By.XPATH, find_locator), timeout=5)
        return True

    # Только поиск по дате публикации
    def check_new_by_date(self, elem):
        find_locator = f'(//div[contains(text(),"{elem}")])[1]'
        self.element_is_visible((By.XPATH, find_locator), timeout=5)
        return True

    #Функция перебора страниц в поиске новости по имени
    def find_new_by_name(self, elem):
        while True:
            try:
                if self.check_new_by_name(elem):
                    self.find_new_by_name(elem)
                    break  # Выходим из цикла, если элемент найден
            except TimeoutException:
                if self.find_view_next_page():
                    self.click_view_next_page()
                else:
                    raise NotFoundException(f"Элемент '{elem}' не найден") from TimeoutException

    #Функция перебора страниц в поиске новости по имени
    def find_new_by_date(self, elem):
        while True:
            try:
                if self.check_new_by_date(elem):
                    self.find_new_by_date(elem)
                    break  # Выходим из цикла, если элемент найден
            except TimeoutException:
                if self.find_view_next_page():
                    self.click_view_next_page()
                else:
                    raise NotFoundException(f"Элемент '{elem}' не найден") from TimeoutException
