from selenium_day_7 import SeleniumDay7
from selenium.webdriver.common.by import By

MY_URL = "https://the-internet.herokuapp.com/checkboxes"

checkbox_one = (By.XPATH, "(//input[@type='checkbox'])[1]")
checkbox_two = (By.XPATH, "(//input[@type='checkbox'])[2]")

my_page_driver = SeleniumDay7()
my_page_driver.go(MY_URL)

my_page_driver.wait_for_element(checkbox_one)
my_page_driver.select_checkbox(checkbox_one)
my_page_driver.wait_for_element(checkbox_two)
my_page_driver.unselect_checkbox(checkbox_two)

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()