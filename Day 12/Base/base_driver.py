from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import os
import time


class BaseDriver:

    def __init__(self):
        try:
            self.my_webdriver = webdriver.Edge()
            self.my_webdriver.maximize_window()
        except Exception as e:
            assert False, f"Can not create webdriver.\n{e}"

    def go(self, url):
        try:
            self.my_webdriver.get(url)
        except Exception as e:
            assert False, f"Can not navigate to {url}.\n{e}"

    def find_element(self, element_locator=()):
        try:
            return self.my_webdriver.find_element(*element_locator)
        except Exception as e:
            assert False, f"Can not find {element_locator} element.\n{e}"

    def wait_for_element(self, element_locator=(), seconds=10):
        try:
            WebDriverWait(self.my_webdriver, seconds).until(
                expected_conditions.visibility_of_element_located(element_locator)
            )
        except Exception as e:
            assert False, f"Can not wait for {element_locator} element.\n{e}"

    def wait_for_element_clickable(self, element_locator=(), seconds=10):
        try:
            self.wait_for_element(element_locator, seconds)
            WebDriverWait(self.my_webdriver, seconds).until(
                expected_conditions.element_to_be_clickable(element_locator)
            )
        except Exception as e:
            assert False, f"Can not wait for {element_locator} element.\n{e}"

    def click_on_element(self, element_locator=()):
        try:
            self.wait_for_element_clickable(element_locator)
            self.find_element(element_locator).click()
        except Exception as e:
            assert False, f"Can not click on {element_locator} element.\n{e}"

    def fill_data(self, element_locator=(), fill_str=""):
        try:
            self.wait_for_element(element_locator)
            self.find_element(element_locator).send_keys(fill_str)
        except Exception as e:
            assert False, f"Can not fill data in {element_locator} element.\n{e}"

    def get_text_of_element(self, element_locator=()):
        try:
            self.wait_for_element(element_locator)
            return self.find_element(element_locator).text
        except Exception as e:
            assert False, f"Can not get text of {element_locator} element.\n{e}"

    def take_screenshot(self, file_name="screenshot.png"):
        try:
            project_path = os.path.dirname(os.path.dirname(__file__))
            screenshot_path = os.path.join(project_path, "Screenshots", file_name)
            self.my_webdriver.save_screenshot(screenshot_path)
        except Exception as e:
            assert False, f"Can not take screenshot.\n{e}"

    def wait_for_seconds(self, sec):
        time.sleep(sec)

    def exit_webdriver(self):
        try:
            self.my_webdriver.quit()
        except Exception as e:
            assert False, f"Can not exit webdriver.\n{e}"
