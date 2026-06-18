from day_10 import Day10
from selenium.webdriver.common.by import By

URL = "https://vaibhavkheriwal.netlify.app/"

about_button = (By.XPATH, "//button[text()='About']")

wd = Day10()
wd.go(URL)
wd.presence_of_element_located(about_button)