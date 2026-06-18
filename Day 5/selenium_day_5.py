from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

class SeleniumDay5:
    def __init__(self):
        self.my_web_driver = webdriver.Edge()

    def navigate_to(self, url = "null"):
        self.my_web_driver.get(url)

    def fill_textbox(self, textbox_locator = (), fill_str = ""):
        self.my_web_driver.find_element(*textbox_locator).send_keys(fill_str)

    def click_on_element(self, element_locator = ()):
        self.my_web_driver.find_element(*element_locator).click()

    def displayed_or_not(self, element_locator = ()):
        return self.my_web_driver.find_element(*element_locator).is_displayed()
    
    def enabled_or_not(self, element_locator = ()):
        return self.my_web_driver.find_element(*element_locator).is_enabled()

    def find_urls(self, element_locator = ()):
        elements_list = []
        for element in self.my_web_driver.find_elements(*element_locator):
            if element.accessible_name:
                elements_list.append(f"{element.get_attribute("href")}")
        return elements_list
    
    def sort_list(self, your_list = [], sort_in_reverse = False):
        return sorted(your_list, reverse = sort_in_reverse)
    
    def wait_for_element_to_be_visible(self, element_locator = ()):
        WebDriverWait(self.my_web_driver, 10).until(expected_conditions.visibility_of_element_located(element_locator))

    def wait_for_seconds(self, seconds):
        time.sleep(seconds)

    def exit_web_driver(self):
        self.my_web_driver.close()