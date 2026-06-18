from day_10 import Day10
from selenium.webdriver.common.by import By


URL = "https://the-internet.herokuapp.com/dynamic_loading/1"

start_button = (By.CSS_SELECTOR, "#start button")
loading_message = (By.ID, "loading")

wd = Day10()
wd.go(URL)
wd.wait_for_element_clickable(start_button).click()
wd.invisibility_of_element_located(loading_message)
