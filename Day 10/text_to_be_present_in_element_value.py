from day_10 import Day10
from selenium.webdriver.common.by import By


URL = "https://www.selenium.dev/selenium/web/web-form.html"

text_box = (By.NAME, "my-text")

wd = Day10()
wd.go(URL)
wd.fill_data(text_box, "Selenium Python")
wd.text_to_be_present_in_element_value(text_box, "Selenium Python")
