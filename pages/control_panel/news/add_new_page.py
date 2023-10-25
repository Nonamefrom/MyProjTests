import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage


class AddNewPage(BasePage):
    PUBLICATION_DATE = (By.XPATH, '//input[@type="date"]')
    NAME_OF_ARTICLE = (By.XPATH, '(//input[@type="text"])[1]')
    AUTHOR_OF_ARTICLE = (By.XPATH, '(//input[@type="text"])[2]')
    IMPORTANT_NEW_CHECKBOX = (By.XPATH, '// label[contains(text(), "Важная новость")]')
    SET_COVER_ARTICLE = (By.XPATH, '//span[@class="sa-file-uploader__text-link"]')
    SAVE_BUTTON = (By.XPATH, '(//span)[31]')
    PUBLICATE_BUTTON = (By.XPATH, '(//button[@type="button"])[20]')


    @allure.step("Вставить дату публикации")
    def input_publication_date(self, date):
        self.fill_text(self.PUBLICATION_DATE, date)

    @allure.step("Ввод названия статьи")
    def input_article_name(self, text):
        self.fill_text(self.NAME_OF_ARTICLE, text)

    @allure.step("Ввод автора статьи")
    def input_author_article(self, text):
        self.fill_text(self.NAME_OF_ARTICLE, text)

    @allure.step("Выбрать обложку статьи")
    def set_cover_article(self):
        self.click(self.SET_COVER_ARTICLE)

    @allure.step("Сохранить статью")
    def save_article(self):
        self.click(self.SAVE_BUTTON)

    @allure.step("Опубликовать статью")
    def publicate_article(self):
        self.click(self.PUBLICATE_BUTTON)
