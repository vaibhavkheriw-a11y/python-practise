from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import time


class SeleniumDay8:

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

    def find_element(self, element_locator=()):
        try:
            return self.my_webdriver.find_element(*element_locator)
        except Exception as e:
            assert False, f"Can not find {element_locator} element.\n{e}"

    def implicit_wait(self, seconds):
        try:
            self.my_webdriver.implicitly_wait(seconds)
        except Exception as e:
            assert False, f"Can not apply implicit wait.\n{e}"

    def explicit_wait_for_element(self, element_locator=(), seconds=10):
        try:
            WebDriverWait(self.my_webdriver, seconds).until(
                expected_conditions.visibility_of_element_located(element_locator)
            )
        except Exception as e:
            assert False, f"Can not wait for {element_locator} element.\n{e}"

    def wait_for_element_clickable(self, element_locator=(), seconds=10):
        try:
            self.explicit_wait_for_element(element_locator, seconds)
            WebDriverWait(self.my_webdriver, seconds).until(
                expected_conditions.element_to_be_clickable(element_locator)
            )
        except Exception as e:
            assert False, f"Can not wait for {element_locator} element.\n{e}"

    def wait_for_frame_and_switch(self, frame_locator=(), seconds=10):
        try:
            WebDriverWait(self.my_webdriver, seconds).until(
                expected_conditions.frame_to_be_available_and_switch_to_it(frame_locator)
            )
        except Exception as e:
            assert False, f"Can not switch to frame {frame_locator}.\n{e}"

    def scroll_to_element(self, element_locator=()):
        try:
            self.my_webdriver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                self.find_element(element_locator)
            )
        except Exception as e:
            assert False, f"Can not scroll to {element_locator} element.\n{e}"

    def click_on_element(self, element_locator=()):
        try:
            self.scroll_to_element(element_locator)
            self.find_element(element_locator).click()
        except Exception as e:
            assert False, f"Can not click on {element_locator} element.\n{e}"

    def fill_data(self, element_locator=(), fill_str=""):
        try:
            self.find_element(element_locator).send_keys(fill_str)
        except Exception as e:
            assert False, f"Can not fill data in {element_locator} element.\n{e}"

    def get_text_of_element(self, element_locator=()):
        try:
            return self.find_element(element_locator).text
        except Exception as e:
            assert False, f"Can not get text of {element_locator} element.\n{e}"

    def select_dropdown_by_text(self, dropdown_locator=(), text=""):
        try:
            Select(self.find_element(dropdown_locator)).select_by_visible_text(text)
        except Exception as e:
            assert False, f"Can not select {text} from dropdown.\n{e}"

    def select_dropdown_by_value(self, dropdown_locator=(), value=""):
        try:
            Select(self.find_element(dropdown_locator)).select_by_value(value)
        except Exception as e:
            assert False, f"Can not select {value} from dropdown.\n{e}"

    def select_dropdown_by_index(self, dropdown_locator=(), index=0):
        try:
            Select(self.find_element(dropdown_locator)).select_by_index(index)
        except Exception as e:
            assert False, f"Can not select index {index} from dropdown.\n{e}"

    def select_options_by_text_list(self, dropdown_locator=(), options_text_list=[]):
        try:
            dropdown = Select(self.find_element(dropdown_locator))
            for option_text in options_text_list:
                dropdown.select_by_visible_text(option_text)
        except Exception as e:
            assert False, f"Can not select options from dropdown.\n{e}"

    def select_all_options_from_dropdown(self, dropdown_locator=()):
        try:
            dropdown = Select(self.find_element(dropdown_locator))
            for option in dropdown.options:
                dropdown.select_by_visible_text(option.text)
        except Exception as e:
            assert False, f"Can not select all options from dropdown.\n{e}"

    def drag_slider_by_offset(self, slider_locator=(), x_offset=0, y_offset=0):
        try:
            ActionChains(self.my_webdriver).drag_and_drop_by_offset(
                self.find_element(slider_locator), x_offset, y_offset
            ).perform()
        except Exception as e:
            assert False, f"Can not drag slider {slider_locator}.\n{e}"

    def drag_and_drop(self, source_locator=(), target_locator=()):
        try:
            ActionChains(self.my_webdriver).drag_and_drop(
                self.find_element(source_locator), self.find_element(target_locator)
            ).perform()
        except Exception as e:
            assert False, f"Can not drag and drop element.\n{e}"

    def mouse_over(self, element_locator=()):
        try:
            ActionChains(self.my_webdriver).move_to_element(self.find_element(element_locator)).perform()
        except Exception as e:
            assert False, f"Can not mouse over on {element_locator} element.\n{e}"

    def right_click(self, element_locator=()):
        try:
            ActionChains(self.my_webdriver).context_click(self.find_element(element_locator)).perform()
        except Exception as e:
            assert False, f"Can not right click on {element_locator} element.\n{e}"

    def wait_for_alert(self, seconds=10):
        try:
            WebDriverWait(self.my_webdriver, seconds).until(expected_conditions.alert_is_present())
        except Exception as e:
            assert False, f"Can not wait for alert.\n{e}"

    def accept_alert(self):
        try:
            self.my_webdriver.switch_to.alert.accept()
        except Exception as e:
            assert False, f"Can not accept alert.\n{e}"

    def get_alert_text(self):
        try:
            return self.my_webdriver.switch_to.alert.text
        except Exception as e:
            assert False, f"Can not get alert text.\n{e}"

    def wait_for_seconds(self, sec):
        time.sleep(sec)

    def exit_webdriver(self):
        try:
            self.my_webdriver.quit()
        except Exception as e:
            assert False, f"Can not exit webdriver.\n{e}"
