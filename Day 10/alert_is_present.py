from day_10 import Day10
from selenium.webdriver.common.by import By


URL = "https://the-internet.herokuapp.com/javascript_alerts"

alert_button = (By.XPATH, "//button[text()='Click for JS Alert']")

wd = Day10()
wd.go(URL)
wd.wait_for_element_clickable(alert_button).click()
alert = wd.alert_is_present()
print(alert.text)
alert.accept()
