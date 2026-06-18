from day_10 import Day10
from selenium.webdriver.common.by import By


URL = "https://the-internet.herokuapp.com/checkboxes"

selected_checkbox = (By.XPATH, "(//input[@type='checkbox'])[2]")

wd = Day10()
wd.go(URL)
wd.element_located_selection_state_to_be(selected_checkbox, True)
