from selenium_day_7 import SeleniumDay7
from selenium.webdriver.common.by import By


MY_URL = "https://demoqa.com/buttons"

double_click_button = (By.ID, "doubleClickBtn")
double_click_message = (By.ID, "doubleClickMessage")

my_page_driver = SeleniumDay7()
my_page_driver.go(MY_URL)

my_page_driver.wait_for_element(double_click_button)
my_page_driver.wait_for_element_clickable(double_click_button)
my_page_driver.mouse_double_click(double_click_button)
my_page_driver.wait_for_element(double_click_message)

print(my_page_driver.get_text_of_element(double_click_message))

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()
