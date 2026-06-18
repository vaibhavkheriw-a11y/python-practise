from selenium_day_7 import SeleniumDay7
from selenium.webdriver.common.by import By

MY_URL = "https://demoqa.com/radio-button"

yes_radio_button = (By.XPATH, "//label[@for='yesRadio']")
result_text = (By.CLASS_NAME, "text-success")

my_page_driver = SeleniumDay7()
my_page_driver.go(MY_URL)

my_page_driver.wait_for_element(yes_radio_button)
my_page_driver.wait_for_element_clickable(yes_radio_button)
my_page_driver.select_radio_button(yes_radio_button)
my_page_driver.wait_for_element(result_text)
print(my_page_driver.get_text_of_element(result_text))

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()
