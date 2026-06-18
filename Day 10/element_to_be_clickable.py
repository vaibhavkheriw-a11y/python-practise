from day_10 import Day10
from selenium.webdriver.common.by import By


URL = "https://www.selenium.dev/selenium/web/web-form.html"

submit_button = (By.CSS_SELECTOR, "button[type='submit']")

wd = Day10()
wd.go(URL)
wd.element_to_be_clickable(submit_button)
