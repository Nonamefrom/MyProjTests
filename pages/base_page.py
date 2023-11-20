import time
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
        return self

    def element_is_visible(self, locator, timeout=3):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=3):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=3):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=3):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=3):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=3):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def fill_text(self, locator, txt, timeout=3):
        element = wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        element.click()
        element.clear()
        element.send_keys(txt)

    def click(self, locator, timeout=3):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    def go_to_element(self, element):
        self.driver.execute_script("argument[0].scrollIntoView();", element)
