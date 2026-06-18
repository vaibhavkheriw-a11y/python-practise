from selenium_day_8 import SeleniumDay8
from selenium.webdriver.common.by import By


MY_URL = "https://the-internet.herokuapp.com/javascript_alerts"

alert_button = (By.XPATH, "//button[text()='Click for JS Alert']")
result_text = (By.ID, "result")

my_page_driver = SeleniumDay8()
my_page_driver.go(MY_URL)

my_page_driver.explicit_wait_for_element(alert_button)
my_page_driver.wait_for_element_clickable(alert_button)
my_page_driver.click_on_element(alert_button)
my_page_driver.wait_for_alert()

print(my_page_driver.get_alert_text())
my_page_driver.accept_alert()
my_page_driver.explicit_wait_for_element(result_text)
print(my_page_driver.get_text_of_element(result_text))

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()
