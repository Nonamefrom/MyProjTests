import time
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    # Examples
    # def __init__(self, driver, url=None):
    #     self.driver = driver
    #     self.url = url
    #     self.wait = wait(driver, timeout=5, poll_frequency=0.1)
    #
    # def open(self):
    #     self.driver.get(self.url)
    #     return self
    #
    # def element_is_visible(self, locator):
    #     return self.wait.until(EC.visibility_of_element_located(locator))
    #
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

