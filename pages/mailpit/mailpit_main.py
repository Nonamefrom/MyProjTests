import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class MailPitMain(BasePage):
    GO_TO_MAIN = (By.XPATH, '//span[@class="ms-2"]')
    SEARCH_BOX = (By.XPATH, '//input[@placeholder="Search mailbox"]')
    SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
    DROPDOWN = (By.XPATH, '//select[@class="form-select form-select-sm d-inline w-auto me-2"]')
    SET_25_PERPAGE = (By.XPATH, '//option[@value="25"]')
    SET_50_PERPAGE = (By.XPATH, '//option[@value="50"]')
    SET_100_PERPAGE = (By.XPATH, '//option[@value="100"]')
    SET_200_PERPAGE = (By.XPATH, '//option[@value="200"]')
    NEXT_PAGE = (By.XPATH, '//i[@class="bi bi-caret-right-fill"]')
    PREF_PAGE = (By.XPATH, '//i[@class="bi bi-caret-left-fill"]')
    OPEN_UNREAD = (By.XPATH, "//a[@class='list-group-item list-group-item-action active']")
    MARK_ALL_READ = (By.XPATH, '//button[normalize-space()="Mark all read"]')
    DELETE_ALL = (By.XPATH, '//button[normalize-space()="Delete all"]')
    RESTORE_URL = (By.XPATH, '//a[contains(text(),"Сбросить пароль")]')
    MAIL_THEME = (By.XPATH, '(//tr)[13]')

    @allure.step("Ввод текста в поля и нажатие кнопки авторизоваться")
    def login(self, email, password):
        self.fill_text(self.NAME_BAR, email)
        self.fill_text(self.PASSWORD_BAR, password)
        self.click(self.SUBMIT_BUTTON)

    @allure.step("Переход на форму восстановления мейла")
    def click_forgot_pass(self):
        self.click(self.FORGOT_PASS)

    @allure.step("Ввод мейла для восстановления")
    def input_recovery_mail(self, email):
        self.fill_text(self.NAME_BAR, email)
        self.click(self.SUBMIT_RECOVERY)

    @allure.step("Отобразить по 25 писем на странице")
    def set_25mails_view(self):
        self.click(self.DROPDOWN)
        self.click(self.SET_25_PERPAGE)

    @allure.step("Отобразить по 50 писем на странице")
    def set_50mails_view(self):
        self.click(self.DROPDOWN)
        self.click(self.SET_50_PERPAGE)

    @allure.step("Отобразить по 100 писем на странице")
    def set_100mails_view(self):
        self.click(self.DROPDOWN)
        self.click(self.SET_100_PERPAGE)

    @allure.step("Отобразить по 200 писем на странице")
    def set_200mails_view(self):
        self.click(self.DROPDOWN)
        self.click(self.SET_200_PERPAGE)

    @allure.step("Переход на следующую страницу писем")
    def click_next_page(self):
        self.click(self.NEXT_PAGE)

    @allure.step("Переход на предыдущую страницу с письмами")
    def click_pref_page(self):
        self.click(self.PREF_PAGE)

    @allure.step("Пометка всех писем прочитанными")
    def click_mark_all_read(self):
        self.click(self.MARK_ALL_READ)

    @allure.step("Удаление всех писем")
    def clear_mailbox(self):
        self.click(self.DELETE_ALL)

    @allure.step("Отображать только не прочтенные")
    def show_unread_letters(self):
        self.click(self.OPEN_UNREAD)

    @allure.step("Поиск письма по клиенту")
    def find_by_client(self, elem):
        find_locator = f'(//div[contains(text(),"{elem}")])[1]'
        self.element_is_visible((By.XPATH, find_locator))
        self.click((By.XPATH, find_locator), timeout=5)
        return self

    @allure.step("Поиск письма по теме")
    def find_by_theme(self, elem):
        find_locator = f'(//b[contains(text(),"{elem}")])[1]'
        self.element_is_visible((By.XPATH, find_locator))
        self.click((By.XPATH, find_locator), timeout=5)

    @allure.step("Клик ссылки восстановления из письма")
    def click_restore_url(self, driver):
        time.sleep(2)
        iframe = driver.find_element(By.XPATH, '//iframe[@id="preview-html"]')  # Экземпляр iframe
        driver.switch_to.frame(iframe)  # Переход в iframe html документа
        self.click(self.RESTORE_URL)

    @allure.step("Получение текста заголовка письма")
    def mail_theme_text(self, driver):
        """Сюда надо передать фикстура.драйвер для работы"""
        time.sleep(2)
        iframe = driver.find_element(By.XPATH, '//iframe[@id="preview-html"]')  # Экземпляр iframe
        driver.switch_to.frame(iframe)
        phrase = wait(driver, 1).until(EC.visibility_of_element_located(self.MAIL_THEME)).text
        return phrase
