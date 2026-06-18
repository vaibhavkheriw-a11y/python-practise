from day_10 import Day10
from selenium.webdriver.common.by import By


URL = "https://the-internet.herokuapp.com/checkboxes"

unchecked_checkbox = (By.XPATH, "(//input[@type='checkbox'])[1]")

wd = Day10()
wd.go(URL)
wd.element_selection_state_to_be(unchecked_checkbox, False)
