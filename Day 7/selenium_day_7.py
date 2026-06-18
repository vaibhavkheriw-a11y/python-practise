from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import time


class SeleniumDay7:

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

    def wait_for_element(self, element_locator=()):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.visibility_of_element_located(element_locator)
            )
        except Exception as e:
            assert False, f"Can not wait for {element_locator} element.\n{e}"

    def wait_for_element_clickable(self, element_locator=()):
        try:
            self.wait_for_element(element_locator)
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.element_to_be_clickable(element_locator)
            )
        except Exception as e:
            assert False, f"Can not wait for {element_locator} element.\n{e}"

    def click_on_element(self, element_locator=()):
        try:
            self.find_element(element_locator).click()
        except Exception as e:
            assert False, f"Can not click on {element_locator} element.\n{e}"

    def select_checkbox(self, checkbox_locator=()):
        try:
            checkbox = self.find_element(checkbox_locator)
            if not checkbox.is_selected():
                checkbox.click()
        except Exception as e:
            assert False, f"Can not select checkbox {checkbox_locator}.\n{e}"

    def unselect_checkbox(self, checkbox_locator=()):
        try:
            checkbox = self.find_element(checkbox_locator)
            if checkbox.is_selected():
                checkbox.click()
        except Exception as e:
            assert False, f"Can not unselect checkbox {checkbox_locator}.\n{e}"

    def select_radio_button(self, radio_button_locator=()):
        try:
            radio_button = self.find_element(radio_button_locator)
            if not radio_button.is_selected():
                radio_button.click()
        except Exception as e:
            assert False, f"Can not select radio button {radio_button_locator}.\n{e}"

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

    def get_attribute_value(self, element_locator=(), attribute_name=""):
        try:
            return self.find_element(element_locator).get_attribute(attribute_name)
        except Exception as e:
            assert False, f"Can not get {attribute_name} attribute.\n{e}"

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

    def select_multi_options_by_text(self, dropdown_locator=(), options_text_list=[]):
        try:
            dropdown = Select(self.find_element(dropdown_locator))
            for option_text in options_text_list:
                dropdown.select_by_visible_text(option_text)
        except Exception as e:
            assert False, f"Can not select multiple options from dropdown.\n{e}"

    def deselect_all_multi_options(self, dropdown_locator=()):
        try:
            Select(self.find_element(dropdown_locator)).deselect_all()
        except Exception as e:
            assert False, f"Can not deselect all options from dropdown.\n{e}"

    def take_screenshot(self, file_path="screenshot.png"):
        try:
            self.my_webdriver.save_screenshot(file_path)
        except Exception as e:
            assert False, f"Can not take screenshot.\n{e}"

    def run_javascript(self, script="", *args):
        try:
            return self.my_webdriver.execute_script(script, *args)
        except Exception as e:
            assert False, f"Can not run javascript.\n{e}"

    def switch_to_tab(self, tab_number):
        try:
            self.my_webdriver.switch_to.window(self.my_webdriver.window_handles[tab_number])
        except Exception as e:
            assert False, f"Can not switch to tab {tab_number}.\n{e}"

    def get_all_window_handles(self):
        try:
            return self.my_webdriver.window_handles
        except Exception as e:
            assert False, f"Can not get window handles.\n{e}"

    def switch_to_window_handle(self, window_handle):
        try:
            self.my_webdriver.switch_to.window(window_handle)
        except Exception as e:
            assert False, f"Can not switch to window handle.\n{e}"

    def switch_to_window_by_title(self, title=""):
        try:
            for window_handle in self.my_webdriver.window_handles:
                self.my_webdriver.switch_to.window(window_handle)
                if self.my_webdriver.title == title:
                    return
            assert False, f"Can not find window with title {title}."
        except Exception as e:
            assert False, f"Can not switch to window with title {title}.\n{e}"

    def close_current_window(self):
        try:
            self.my_webdriver.close()
        except Exception as e:
            assert False, f"Can not close current window.\n{e}"

    def mouse_over(self, element_locator=()):
        try:
            ActionChains(self.my_webdriver).move_to_element(self.find_element(element_locator)).perform()
        except Exception as e:
            assert False, f"Can not mouse over on {element_locator} element.\n{e}"

    def mouse_click(self, element_locator=()):
        try:
            ActionChains(self.my_webdriver).click(self.find_element(element_locator)).perform()
        except Exception as e:
            assert False, f"Can not mouse click on {element_locator} element.\n{e}"

    def mouse_right_click(self, element_locator=()):
        try:
            ActionChains(self.my_webdriver).context_click(self.find_element(element_locator)).perform()
        except Exception as e:
            assert False, f"Can not right click on {element_locator} element.\n{e}"

    def mouse_double_click(self, element_locator=()):
        try:
            ActionChains(self.my_webdriver).double_click(self.find_element(element_locator)).perform()
        except Exception as e:
            assert False, f"Can not double click on {element_locator} element.\n{e}"

    def wait_for_popup(self):
        try:
            WebDriverWait(self.my_webdriver, 10).until(expected_conditions.alert_is_present())
        except Exception as e:
            assert False, f"Can not wait for popup.\n{e}"

    def accept_popup(self):
        try:
            self.my_webdriver.switch_to.alert.accept()
        except Exception as e:
            assert False, f"Can not accept popup.\n{e}"

    def dismiss_popup(self):
        try:
            self.my_webdriver.switch_to.alert.dismiss()
        except Exception as e:
            assert False, f"Can not dismiss popup.\n{e}"

    def get_popup_text(self):
        try:
            return self.my_webdriver.switch_to.alert.text
        except Exception as e:
            assert False, f"Can not get popup text.\n{e}"

    def fill_popup_data(self, fill_str=""):
        try:
            self.my_webdriver.switch_to.alert.send_keys(fill_str)
        except Exception as e:
            assert False, f"Can not fill data in popup.\n{e}"

    def wait_for_seconds(self, sec):
        time.sleep(sec)

    def exit_webdriver(self):
        try:
            self.my_webdriver.quit()
        except Exception as e:
            assert False, f"Can not exit webdriver.\n{e}"
