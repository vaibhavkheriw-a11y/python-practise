from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time

class SeleniumDay6:

    def __init__(self):
        try:
            self.my_webdriver = webdriver.Edge()
        except Exception as e:
            assert False, f"Can not create webdriver.\n{e}"

    def go(self, url):
        try:
            self.my_webdriver.get(url)
        except Exception as e:
            assert False, f"Can not navigate to {url}.\n{e}"

    def wait_for_element(self, element_locator = ()):
        try:
            WebDriverWait(self.my_webdriver, 10).until(expected_conditions.visibility_of_element_located(element_locator))
        except Exception as e:
            assert False, f"Can not wait for {element_locator} element.\n{e}"

    def wait_for_element_clickable(self, element_locator = ()):
        try:
            self.wait_for_element(element_locator)
            WebDriverWait(self.my_webdriver, 10).until(expected_conditions.element_to_be_clickable(element_locator))
        except Exception as e:
            assert False, f"Can not wait for {element_locator} element.\n{e}"

    def click_on_element(self, element_locator = ()):
        try:
            self.my_webdriver.find_element(*element_locator).click()
        except Exception as e:
            assert False, f"Can not click on {element_locator} element.\n{e}"

    def get_text_of_element(self, element_locator = ()):
        try:
            return self.my_webdriver.find_element(*element_locator).text
        except Exception as e:
            assert False, f"Can not get text of {element_locator} element.\n{e}"

    def wait_for_seconds(self, sec):
        time.sleep(sec)

    def switch_to_tab(self, tab_number):
        try:
            self.my_webdriver.switch_to.window(self.my_webdriver.window_handles[tab_number])
        except Exception as e:
            assert False, f"Can not switch to tab {tab_number}."

    def fill_data(self, upload_locator = (), file_path = ""):
        try:
            self.my_webdriver.find_element(*upload_locator).send_keys(file_path)
        except Exception as e:
            assert False, f"Can not fill data"

    def exit_webdriver(self):
        try:
            self.my_webdriver.quit()
        except Exception as e:
            assert False, f"Can not exit webdriver.\n{e}"