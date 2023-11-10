import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage

class SideBarCabinetPage(BasePage):
    OPTIONS = (By.XPATH, '//span[contains(text(),"Витрина")]')
    NEW_OPTION = (By.XPATH, '//div[@class="new-options-counter__count sa-text-color-white"]')
    POINTS = (By.XPATH, '//span[contains(text(),"Точки продаж")]')
    NEWS = (By.XPATH, '//span[contains(text(),"Новости")]')
    IMPORTANT_NEW = (By.XPATH, '//img[@alt="new important news"]')
    UNREAD_NEW = (By.XPATH, '//div[@class="new-news-counter__count sa-text-color-white"]')
    LEGALS = (By.XPATH, '//span[contains(text(),"Юридические лица")]')
    B2B_EMPLOYEES = (By.XPATH, '//a[@href="/employee"]//span')
    DOCUMENTS = (By.XPATH, '//a[@href="/contract"]//span')
    FAQ = (By.XPATH, '//a[@href="/qa"]//span')

    @allure.step("Переход на вкладку Витрина")
    def click_options(self):
        self.click(self.OPTIONS)

    @allure.step("Наличие новой опции")
    def check_important_option(self):
        try:
            self.element_is_visible(self.NEW_OPTION)
            return True
        except TimeoutException:
            return False

    @allure.step("Переход на вкладку Точки продаж")
    def click_points(self):
        self.click(self.POINTS)

    @allure.step("Переход на вкладку Новости")
    def click_news(self):
        self.click(self.NEWS)

    @allure.step("Наличие новой важной новости")
    def check_important_new(self):
        try:
            self.element_is_visible(self.IMPORTANT_NEW)
            return True
        except TimeoutException:
            return False

    @allure.step("Наличие новой важной новости")
    def check_unread_new(self):
        try:
            self.element_is_visible(self.UNREAD_NEW)
            return True
        except TimeoutException:
            return False

    @allure.step("Переход на Юр лица")
    def click_legals(self):
        self.click(self.LEGALS)

    @allure.step("Переход на вкладку Сотрудники")
    def click_b2b_employee(self):
        self.click(self.B2B_EMPLOYEES)

    @allure.step("Переход на вкладку Правовые документы")
    def click_documents(self):
        self.click(self.DOCUMENTS)

    @allure.step("Переход на вкладку Вопросы и ответы")
    def click_faq(self):
        self.click(self.FAQ)
