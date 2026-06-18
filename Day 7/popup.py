from selenium_day_7 import SeleniumDay7
from selenium.webdriver.common.by import By


MY_URL = "https://the-internet.herokuapp.com/javascript_alerts"

alert_button = (By.XPATH, "//button[text()='Click for JS Alert']")
result_text = (By.ID, "result")

my_page_driver = SeleniumDay7()
my_page_driver.go(MY_URL)

my_page_driver.wait_for_element(alert_button)
my_page_driver.wait_for_element_clickable(alert_button)
my_page_driver.click_on_element(alert_button)
my_page_driver.wait_for_popup()

print(my_page_driver.get_popup_text())
my_page_driver.accept_popup()
my_page_driver.wait_for_element(result_text)
print(my_page_driver.get_text_of_element(result_text))

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()
