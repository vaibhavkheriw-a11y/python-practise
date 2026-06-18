from day_10 import Day10
from selenium.webdriver.common.by import By


URL = "https://the-internet.herokuapp.com/checkboxes"

checkboxes = (By.CSS_SELECTOR, "input[type='checkbox']")

wd = Day10()
wd.go(URL)
all_checkboxes = wd.presence_of_all_elements_located(checkboxes)
print(f"Total checkboxes found: {len(all_checkboxes)}")
