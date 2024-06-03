import time
import re
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
        return self

    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def fill_text(self, locator, txt, timeout=5):
        element = wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        element.click()
        element.clear()
        element.send_keys(txt)

    def click(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    def go_to_element(self, locator):
        element = wait(self.driver, 2).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)

    def link_end_with(self, link_end):
        return self.driver.current_url.endswith(link_end)

    def get_text(self, elem, timeout=3):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(elem)).text

    def get_attribute_value(self, elem, attr):
        return self.element_is_present(elem).get_attribute(attr)

    def get_cell_count(self, table_loc, timeout=5):
        try:
            return len(wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(table_loc)))
        except:
            return 0

    def activated(self, locator, attr) -> bool:
        """Используется в случаях когда в аттрибуте не было active, но стало active при выборе"""
        value = self.element_is_present(locator).get_attribute(attr)
        # print(value)
        res = re.split('-|__|--| ', value)
        active = 'active'
        for i in res:
            if active in i:
                return True
        else:
            return False

    def disabled(self, locator, attr) -> bool:
        """Используется в случаях когда в аттрибуте не было disable, но стало disabled при отключении"""
        value = self.element_is_present(locator).get_attribute(attr)
        # print(value)
        res = re.split('-|__|--| ', value)
        disabled = 'disabled'
        for i in res:
            if disabled in i:
                return True
        else:
            return False
