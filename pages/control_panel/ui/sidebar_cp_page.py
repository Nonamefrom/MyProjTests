import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SideBarCpPage(BasePage):
    OPTIONS = (By.XPATH, '//a[@href="/options"]')
    NEWS = (By.XPATH, '//a[@href="/news"]')
    SERVICES = (By.XPATH, '//a[@href="/services"]')
    USERS = (By.XPATH, '//a[@href="/users"]')
    STATISTIC = (By.XPATH, '//a[@href="/statistic"]')
    DOWNLOADED_FILES = (By.XPATH, '//a[@href="/files"]')
    JOURNAL = (By.XPATH, '//a[@href="/analytics"]')
    NOTIFICATIONS = (By.XPATH, '//a[@href="/notifications"]')

    @allure.step("Переход на вкладку Опции")
    def click_options(self):
        self.click(self.OPTIONS)

    @allure.step("Переход на вкладку Новости")
    def click_news(self):
        self.click(self.NEWS)

    @allure.step("Переход на вкладку Сервисы")
    def click_services(self):
        self.click(self.SERVICES)

    @allure.step("Переход на вкладку Пользователи")
    def click_users(self):
        self.click(self.USERS)

    @allure.step("Переход на вкладку Статистика")
    def click_statistic(self):
        self.click(self.STATISTIC)

    @allure.step("Переход на вкладку Журнал")
    def click_journal(self):
        self.click(self.JOURNAL)

    @allure.step("Переход на вкладку Загрузка файлов")
    def click_downloaded_files(self):
        self.click(self.DOWNLOADED_FILES)

    @allure.step("Переход на вкладку Уведомления")
    def click_notifications(self):
        self.click(self.NOTIFICATIONS)
