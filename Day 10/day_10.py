from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time


class Day10:

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

    def title_is(self, title):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.title_is(title)
            )
        except Exception as e:
            assert False, f"Title is not {title}.\n{e}"

    def title_contains(self, text):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.title_contains(text)
            )
        except Exception as e:
            assert False, f"Title does not contain {text}.\n{e}"

    def url_contains(self, text):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.url_contains(text)
            )
        except Exception as e:
            assert False, f"URL does not contain {text}.\n{e}"

    def url_to_be(self, url):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.url_to_be(url)
            )
        except Exception as e:
            assert False, f"URL is not {url}.\n{e}"

    def presence_of_element_located(self, element_locator=()):
        try:
            return WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.presence_of_element_located(element_locator)
            )
        except Exception as e:
            assert False, f"Element not present in DOM: {element_locator}.\n{e}"

    def visibility_of_element_located(self, element_locator=()):
        try:
            return WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.visibility_of_element_located(element_locator)
            )
        except Exception as e:
            assert False, f"Element not visible: {element_locator}.\n{e}"

    def visibility_of(self, element_locator=()):
        try:
            return WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.visibility_of(
                    self.my_webdriver.find_element(*element_locator)
                )
            )
        except Exception as e:
            assert False, f"Element is not visible: {element_locator}.\n{e}"

    def presence_of_all_elements_located(self, element_locator=()):
        try:
            return WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.presence_of_all_elements_located(element_locator)
            )
        except Exception as e:
            assert False, f"Elements not present: {element_locator}.\n{e}"

    def text_to_be_present_in_element(self, element_locator=(), text=""):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.text_to_be_present_in_element(element_locator, text)
            )
        except Exception as e:
            assert False, f"Text '{text}' not present in element {element_locator}.\n{e}"

    def text_to_be_present_in_element_value(self, element_locator=(), text=""):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.text_to_be_present_in_element_value(
                    element_locator, text
                )
            )
        except Exception as e:
            assert False, f"Text '{text}' not present in element value {element_locator}.\n{e}"

    def frame_to_be_available_and_switch_to_it(self, frame_locator=()):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.frame_to_be_available_and_switch_to_it(frame_locator)
            )
        except Exception as e:
            assert False, f"Frame not available: {frame_locator}.\n{e}"

    def invisibility_of_element_located(self, element_locator=()):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.invisibility_of_element_located(element_locator)
            )
        except Exception as e:
            assert False, f"Element is still visible: {element_locator}.\n{e}"

    def element_to_be_clickable(self, element_locator=()):
        try:
            return WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.element_to_be_clickable(element_locator)
            )
        except Exception as e:
            assert False, f"Element not clickable: {element_locator}.\n{e}"

    def staleness_of(self, element_locator=()):
        try:
            if isinstance(element_locator, tuple):
                element = self.my_webdriver.find_element(*element_locator)
            else:
                element = element_locator

            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.staleness_of(element)
            )
        except Exception as e:
            assert False, f"Element is not stale: {element_locator}.\n{e}"

    def element_to_be_selected(self, element_locator=()):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.element_to_be_selected(
                    self.my_webdriver.find_element(*element_locator)
                )
            )
        except Exception as e:
            assert False, f"Element is not selected: {element_locator}.\n{e}"

    def element_located_to_be_selected(self, element_locator=()):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.element_located_to_be_selected(element_locator)
            )
        except Exception as e:
            assert False, f"Located element is not selected: {element_locator}.\n{e}"

    def element_selection_state_to_be(self, element_locator=(), state=True):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.element_selection_state_to_be(
                    self.my_webdriver.find_element(*element_locator), state
                )
            )
        except Exception as e:
            assert False, f"Element selection state is not {state}: {element_locator}.\n{e}"

    def element_located_selection_state_to_be(self, element_locator=(), state=True):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.element_located_selection_state_to_be(
                    element_locator, state
                )
            )
        except Exception as e:
            assert False, f"Element selection state is not {state}: {element_locator}.\n{e}"

    def alert_is_present(self):
        try:
            return WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.alert_is_present()
            )
        except Exception as e:
            assert False, f"Alert is not present.\n{e}"

    def wait_for_element(self, element_locator=()):
        try:
            return self.visibility_of_element_located(element_locator)
        except Exception as e:
            assert False, f"Can not wait for {element_locator} element.\n{e}"

    def wait_for_element_clickable(self, element_locator=()):
        try:
            return self.element_to_be_clickable(element_locator)
        except Exception as e:
            assert False, f"Can not wait for clickable element {element_locator}.\n{e}"

    def get_text_of_element(self, element_locator=()):
        try:
            return self.my_webdriver.find_element(*element_locator).text
        except Exception as e:
            assert False, f"Can not get text of {element_locator} element.\n{e}"

    def wait_for_seconds(self, sec):
        time.sleep(sec)

    def switch_to_tab(self, tab_number):
        try:
            self.my_webdriver.switch_to.window(
                self.my_webdriver.window_handles[tab_number]
            )
        except Exception as e:
            assert False, f"Can not switch to tab {tab_number}.\n{e}"

    def fill_data(self, upload_locator=(), file_path=""):
        try:
            self.my_webdriver.find_element(*upload_locator).send_keys(file_path)
        except Exception as e:
            assert False, f"Can not fill data in {upload_locator}.\n{e}"

    def exit_webdriver(self):
        try:
            self.my_webdriver.quit()
        except Exception as e:
            assert False, f"Can not exit webdriver.\n{e}"