import allure
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from pages.base_page import BasePage


class B2bEmployeePageCab(BasePage):
    H1_EMPLOYEE = (By.XPATH, '(//span[@class="text-h1-bold"])[1]')
    LINK_TO_DASHBOARD = (By.XPATH, '//a[contains(text(),"ссылке")]')
    COPY_LINK_CLIPBOARD = (By.XPATH, '//div[@class="sa-alert__after-wrapper"]//div//*[name()="svg"]')
    BUBBLE_MESSAGE = (By.XPATH, '//*[@class="sa-snackbar__title"]')
    CALL_MODAL_MENU = (By.XPATH, '//button[@data-qa="add-new-employee-btn"]')
    NAME_INPUT = (By.XPATH, '//*[@data-qa="employee-first-name-input"]//input')
    LAST_NAME_INPUT = (By.XPATH, '//*[@data-qa="employee-last-name-input"]//input')
    EMAIL_INPUT = (By.XPATH, '//*[@data-qa="employee-email-input"]//input')
    PHONE_INPUT = (By.XPATH, '//*[@data-qa="employee-phone-input"]//input')
    EMPLOYEE_POSITION = (By.XPATH, '//*[@data-qa="employee-position-select"]//input')
    SUPERVISOR_EMPLOYEE = (By.XPATH, '//*[@data-qa="employee-position-select"]//li[1]')
    SALES_MANAGER_EMPLOYEE = (By.XPATH, '//*[@data-qa="employee-position-select"]//li[2]')
    TIRE_SERVICE_EMPLOYEE = (By.XPATH, '//*[@data-qa="employee-position-select"]//li[3]')
    CAR_WASH_EMPLOYEE = (By.XPATH, '//*[@data-qa="employee-position-select"]//li[4]')
    CAR_SERVICE_EMPLOYEE = (By.XPATH, '//*[@data-qa="employee-position-select"]//li[5]')
    EMPLOYEE_ACCESS = (By.XPATH, '//*[@data-qa="employee-access-type-select"]//input')
    SET_FULL_ACCESS = (By.XPATH, '//span[contains(text(),"Разрешить доступ ко всем опциям")]')
    SET_CHOSE_ACCESS = (By.XPATH, '//span[contains(text(),"Разрешить доступ только к выбранным")]')
    SET_ONLINE_RECORD = (By.XPATH, '//label[contains(text(),"Онлайн-запись")]')
    SET_PWZ = (By.XPATH, '//label[contains(text(),"ПВЗ")]')
    SET_EDUCATION = (By.XPATH, '//label[contains(text(),"Обучение")]')
    SET_FREE_TIRE_SERVICE = (By.XPATH, '//label[contains(text(),"Бесплатный шиномонтаж")]')
    SET_PRIVILEGE = (By.XPATH, '//label[contains(text(),"Привилегии")]')
    DECLINE_ACCESS = (By.XPATH, '//span[contains(text(),"Запретить доступ ко всем опциям")]')
    ADD_EMPLOYEE = (By.XPATH, '//*[@data-qa="add-btn"]')
    CLOSE_MODAL = (By.XPATH, '//*[@data-qa="close-btn"]')
    ERROR_EMPTY_INPUT = (By.XPATH, '//*[contains(text(),"Заполните поле")]')  # 5 валидаций
    ERROR_MAIL_INPUT = (By.XPATH, '//div[@data-qa="employee-email-input"]//div//div')
    ERROR_PHONE_INPUT = (By.XPATH, '//*[@data-qa="employee-phone-input"]//div//div')
    ERROR_CHECKBOX_INPUT = (By.XPATH, '//span[contains(text(),"Необходимо выбрать хотя бы одну опцию")]')
    DELETE_USER = (By.XPATH, '//*[@data-qa="delete-employee-btn"]')
    SAVE_CHANGES = (By.XPATH, '//*[@data-qa="save-btn"]')
    ACCEPT_DELETE = (By.XPATH, '//*[@data-qa="delete-btn"]')

    @allure.step("Заголовок Н1 страницы сотрудников")
    def get_h1_b2b_emp_page(self):
        phrase = wait(self.driver, 3).until(EC.visibility_of_element_located(self.H1_EMPLOYEE)).text
        return phrase

    @allure.step("Переход на дашборд сотрудников")
    def go_to_dashboard(self):
        self.click(self.LINK_TO_DASHBOARD)

    @allure.step("Копируем ссылку на дашборд сотрудников")
    def copy_link(self):
        self.click(self.COPY_LINK_CLIPBOARD)

    @allure.step("Вызов модалки добавления сотрудника")
    def call_modal_menu(self):
        self.click(self.CALL_MODAL_MENU)
        return self

    @allure.step("Ввод имени")
    def input_name(self, text):
        self.fill_text(self.NAME_INPUT, text)
        return self

    @allure.step("Ввод фамилии")
    def input_last_name(self, text):
        self.fill_text(self.LAST_NAME_INPUT, text)
        return self

    @allure.step("Ввод мейла")
    def input_email(self, text):
        self.fill_text(self.EMAIL_INPUT, text)
        return self

    @allure.step("Ввод телефона")
    def input_phone(self, text):
        self.fill_text(self.PHONE_INPUT, text)
        return self

    @allure.step("Выбрать роль Руководитель")
    def set_supervisor_role(self):
        self.click(self.EMPLOYEE_POSITION)
        self.click(self.SUPERVISOR_EMPLOYEE)
        return self

    @allure.step("Выбрать роль менеджер по продажам")
    def set_sales_manager_role(self):
        self.click(self.EMPLOYEE_POSITION)
        self.click(self.SALES_MANAGER_EMPLOYEE)
        return self

    @allure.step("Выбрать роль сотрудник шиномонтажа")
    def set_tire_service_role(self):
        self.click(self.EMPLOYEE_POSITION)
        self.click(self.TIRE_SERVICE_EMPLOYEE)
        return self

    @allure.step("Выбрать роль сотрудник автомойки")
    def set_car_wash_role(self):
        self.click(self.EMPLOYEE_POSITION)
        self.click(self.CAR_WASH_EMPLOYEE)
        return self

    @allure.step("Выбрать роль сотрудник автосервиса")
    def set_car_service_role(self):
        self.click(self.EMPLOYEE_POSITION)
        self.click(self.CAR_SERVICE_EMPLOYEE)
        return self

    @allure.step("Выбрать полный доступ к продуктам")
    def set_full_access(self):
        self.click(self.EMPLOYEE_ACCESS)
        self.click(self.SET_FULL_ACCESS)
        return self

    @allure.step("Выбрать  доступ к выбранным продуктам")
    def set_chose_access(self):
        self.click(self.EMPLOYEE_ACCESS)
        self.click(self.SET_CHOSE_ACCESS)
        return self

    @allure.step("Клик доступ к Онлайн записи")
    def set_online_record(self):
        self.click(self.SET_ONLINE_RECORD)
        return self

    @allure.step("Клик доступ к ПВЗ")
    def set_access_pwz(self):
        self.click(self.SET_PWZ)
        return self

    @allure.step("Клик доступ к Обучение")
    def set_access_education(self):
        self.click(self.SET_EDUCATION)
        return self

    @allure.step("Клик доступ к Бесплатный шиномонтаж")
    def set_access_free_tire_service(self):
        self.click(self.SET_FREE_TIRE_SERVICE)
        return self

    @allure.step("Клик доступ к Привилегии")
    def set_access_privilege(self):
        self.click(self.SET_PRIVILEGE)
        return self

    @allure.step("Запретить доступ к продуктам")
    def decline_access(self):
        self.click(self.EMPLOYEE_ACCESS)
        self.click(self.DECLINE_ACCESS)
        return self

    @allure.step("Клик 'Добавить'")
    def click_add_employee(self):
        self.click(self.ADD_EMPLOYEE)
        return self

    @allure.step("Закрыть модалку ввода данных")
    def close_modal(self, text):
        self.fill_text(self.CLOSE_MODAL, text)
        return self

    @allure.step("Получение текста ошибки пустых полей")
    def error_empty_massage_clients(self):
        phrase = wait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.ERROR_EMPTY_INPUT)).text
        return phrase

    @allure.step("Получение количества ошибок пустых полей")
    def count_error_empty_massage_clients(self):
        elements = wait(self.driver, timeout=5).until(EC.visibility_of_all_elements_located(self.ERROR_EMPTY_INPUT))
        error_texts = [element.text for element in elements]
        return len(error_texts)

    @allure.step("Получение текстa ошибки mail'a")
    def error_mail_massage(self):
        phrase = wait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.ERROR_MAIL_INPUT)).text
        return phrase

    @allure.step("Получение текстa ошибки телефонa")
    def error_phone_massage(self):
        phrase = wait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.ERROR_PHONE_INPUT)).text
        return phrase

    @allure.step("Получение текстa ошибки блока чекбоксов")
    def error_checkbox_massage(self):
        phrase = wait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.ERROR_CHECKBOX_INPUT)).text
        return phrase

    @allure.step("Клик удалить пользователя в окне редактирования")
    def delete_employee(self):
        self.click(self.DELETE_USER)
        return self

    @allure.step("Подтверждение удаления")
    def accept_delete_employee(self):
        self.click(self.ACCEPT_DELETE)
        self.driver.refresh()
        return self

    @allure.step("Получаем текст из бабл-уведолмения")
    def get_bubble_text(self):
        phrase = wait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.BUBBLE_MESSAGE)).text
        return phrase
