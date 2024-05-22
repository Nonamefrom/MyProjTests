import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from model.notification import Notification


class PartnerCabinetNotifications(BasePage):
    NOTIFICATION_CLOSE_BUTTON = (By.XPATH, '//div[@class="sa-side-modal__modal"]//div//*[@class="sa-icon sa-icon--name-'
                                           '-Close sa-icon--clickable sa-side-modal__close-icon"]')
    NOTIFICATION_HEADER = (By.XPATH, '//div[@class="notification-modal-list"]//div//div//div')

    @allure.step('Поиск уведомления по заголовку в модальном окне в КУ')
    def find_notification_by_header(self, header) -> bool:
        row = self.NOTIFICATION_HEADER
        elements = self.elements_are_visible(row)
        l = len(elements)
        count = 0
        for i in range(1, l + 1):
            text = self.get_text((By.XPATH, f'//div[@class="notification-modal-list"]//div[{i}]//div//div'))
            if header == text:
                count += 1
        if count == 1:
            return True
        else:
            return False

    def close_notifications_modal(self):
        self.click(self.NOTIFICATION_CLOSE_BUTTON)
