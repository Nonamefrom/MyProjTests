# Методы работают с Новостями и опциями в Панели Управления
# не срабатывает клик по опции
import time

import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from utils.exceptions.not_found_exception import NotFoundException


class CommonSteps(BasePage):
    VIEW_NEXT_PAGE = (By.XPATH, '//*[@class="sa-icon sa-icon--name--Right sa-pagination__next-icon"]')

    @allure.step("Переход на следующую страницу")
    def click_view_next_page(self):
        time.sleep(0.5)
        self.click(self.VIEW_NEXT_PAGE)

    # ПУ - Поиск и клик по наименованию опции, даты окончания действия, статусу публикации
    @allure.step("Поиск элемента и клик элемента опции")
    def find_element_on_page(self, elem):
        find_locator = f'//div[contains(text(),"{elem}")]'
        self.element_is_visible((By.XPATH, find_locator), timeout=5)
        self.click((By.XPATH, find_locator), timeout=5)

    # Только поиск перехода на следующую страницу
    def find_view_next_page(self):
        self.element_is_visible(self.VIEW_NEXT_PAGE)
        return True

    # Только поиск элемента опции/новости на странице по введенному параметру
    def check_element_on_page(self, elem):
        find_locator = f'//div[contains(text(),"{elem}")]'
        self.element_is_visible((By.XPATH, find_locator), timeout=5)
        return True

    # Функция перебора страниц в поиске элемента опции,
    def find_elem(self, elem):
        while True:
            try:
                if self.check_element_on_page(elem):
                    self.find_element_on_page(elem)
                    break  # Выходим из цикла, если элемент найден
            except TimeoutException:
                if self.find_view_next_page():
                    self.click_view_next_page()
                else:
                    raise NotFoundException(f"Элемент '{elem}' не найден") from TimeoutException

    # Поиск и клик по наименованию новости, даты окончания действия, статусу публикации
    @allure.step("Поиск новости по заголовку")
    def find_new_by_name(self, elem):
        find_locator = f'//div[contains(text(),"{elem}")]'
        self.element_is_visible((By.XPATH, find_locator), timeout=5)
        self.click((By.XPATH, find_locator), timeout=5)

    # Поиск и клик последней новости по дате публикации
    @allure.step("Поиск последней новости по дате публикации")
    def find_new_by_date(self, elem):
        find_locator = f'(//div[contains(text(),"{elem}")])[1]'
        self.element_is_visible((By.XPATH, find_locator), timeout=5)
        self.click((By.XPATH, find_locator), timeout=5)

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

    # Функция перебора страниц в поиске новости по имени
    def find_click_new_by_name(self, elem):
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

    # Функция перебора страниц в поиске новости по дате публикации
    def find_click_new_by_date(self, elem):
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
