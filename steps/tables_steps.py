#Методы для работы с таблицами: пользователи в Панели Управления
import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from utils.exceptions.not_found_exception import NotFoundException


class TablesSteps(BasePage):
    VIEW_NEXT_PAGE = (By.XPATH, '//*[@class="sa-icon sa-icon--name--Right sa-pagination__next-icon"]')

    @allure.step("Переход на следующую страницу")
    def click_view_next_page(self):
        self.click(self.VIEW_NEXT_PAGE)

# ПУ - Поиск и клик по наименованию опции, даты окончания действия, статусу публикации
    @allure.step("Поиск элемента таблицы и клик по нему")
    def find_element_of_table(self, elem):
        find_locator = f'//span[contains(text(),"{elem}")]'
        self.element_is_visible((By.XPATH, find_locator), timeout=5)
        self.click((By.XPATH, find_locator), timeout=5)

# Только поиск перехода на следующую страницу
    def find_view_next_page(self):
        self.element_is_visible(self.VIEW_NEXT_PAGE)
        return True

# Только поиск элемента опции/новости на странице по введенному параметру
    def check_element_of_table(self, elem):
        find_locator = f'//span[contains(text(),"{elem}")]'
        self.element_is_visible((By.XPATH, find_locator), timeout=5)
        return True

#Функция перебора страниц в поиске элемента таблицы,
    def find_option(self, elem):
        while True:
            try:
                if self.check_element_of_table(elem):
                    self.find_element_of_table(elem)
                    break  # Выходим из цикла, если элемент найден
            except TimeoutException:
                if self.find_view_next_page():
                    self.click_view_next_page()
                else:
                    raise NotFoundException(f"Элемент '{elem}' не найден") from TimeoutException
