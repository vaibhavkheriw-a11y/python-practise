from day_10 import Day10
from selenium.webdriver.common.by import By


URL = "https://the-internet.herokuapp.com/dynamic_loading/1"

start_button = (By.CSS_SELECTOR, "#start button")
finish_message = (By.ID, "finish")

wd = Day10()
wd.go(URL)
wd.wait_for_element_clickable(start_button).click()
wd.text_to_be_present_in_element(finish_message, "Hello World!")
