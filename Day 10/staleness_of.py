from day_10 import Day10
from selenium.webdriver.common.by import By


URL = "https://the-internet.herokuapp.com/add_remove_elements/"

add_button = (By.XPATH, "//button[text()='Add Element']")
delete_button = (By.XPATH, "//button[text()='Delete']")

wd = Day10()
wd.go(URL)
wd.wait_for_element_clickable(add_button).click()
delete_element = wd.presence_of_element_located(delete_button)
delete_element.click()
wd.staleness_of(delete_element)
