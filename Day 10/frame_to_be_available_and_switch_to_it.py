from day_10 import Day10
from selenium.webdriver.common.by import By


URL = "https://the-internet.herokuapp.com/iframe"

editor_frame = (By.ID, "mce_0_ifr")
editor_body = (By.ID, "tinymce")

wd = Day10()
wd.go(URL)
wd.frame_to_be_available_and_switch_to_it(editor_frame)
wd.text_to_be_present_in_element(editor_body, "Your content goes here.")
