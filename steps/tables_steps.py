#Методы для работы с таблицами: пользователи в Панели Управления
import allure

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from utils.exceptions.not_found_exception import NotFoundException


class TablesSteps(BasePage):
    VIEW_NEXT_PAGE = (By.XPATH, '//*[@class="sa-icon sa-icon--name--Right sa-pagination__next-icon"]')

    def create_entity_text_xpath(self, text ):
        locator = f'//span[contains(text(),"{text}")]'
        return locator

    @allure.step("Поиск текста в таблице")
    def is_entity_exists_in_table(self, text):
        locator = (By.XPATH, self.create_entity_text_xpath(text))
        self.element_are_present(locator, timeout=5)
        return True

    @allure.step("Поиск текста в таблице, клик по данному тексту")
    def find_entity_in_table(self, text):
        locator = (By.XPATH, self.create_entity_text_xpath(text))
        self.element_is_visible(locator, timeout=5)
        self.go_to_element(locator)
        self.click(locator, timeout=5)

    @allure.step("Поиск кнопки в пагинации для перехода на следующую страницу")
    def find_next_page_button(self):
        self.element_is_visible(self.VIEW_NEXT_PAGE)
        return True

    @allure.step("Переход на следующую страницу через пагинацию")
    def click_next_page_button(self):
        self.element_is_visible(self.VIEW_NEXT_PAGE)
        self.go_to_element(self.VIEW_NEXT_PAGE)
        self.click(self.VIEW_NEXT_PAGE)

    # Функция перебора страниц в поиске элемента таблицы
    def find_entity(self, text):
        while True:
            try:
                if self.is_entity_exists_in_table(text):
                    self.find_entity_in_table(text)
                    break  # Выходим из цикла, если элемент найден
            except TimeoutException:
                if self.find_next_page_button():
                    self.click_next_page_button()
                else:
                    raise NotFoundException(f"Элемент '{text}' не найден") from TimeoutException

    def count_find_entity(self, text):
        count = 0
        while True:
            try:
                if self.is_entity_exists_in_table(text):
                    count += 1
            except TimeoutException:
                pass  # Пропускаем ошибку, если элемент не найден на текущей странице
            try:
                if not self.find_next_page_button():  # Если кнопка "Следующая страница" не найдена, выходим из цикла
                    break
                self.click_next_page_button()  # Переходим на следующую страницу
            except TimeoutException:
                break  # Если не удалось найти кнопку "Следующая страница", выходим из цикла
        return count
