from day_10 import Day10
from selenium.webdriver.common.by import By


URL = "https://the-internet.herokuapp.com/checkboxes"

selected_checkbox = (By.XPATH, "(//input[@type='checkbox'])[2]")

wd = Day10()
wd.go(URL)
wd.element_located_to_be_selected(selected_checkbox)
