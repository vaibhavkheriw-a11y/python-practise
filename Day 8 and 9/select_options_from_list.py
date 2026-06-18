from selenium_day_8 import SeleniumDay8
from selenium.webdriver.common.by import By


MY_URL = "https://the-internet.herokuapp.com/dropdown"

dropdown = (By.ID, "dropdown")

my_page_driver = SeleniumDay8()
my_page_driver.go(MY_URL)

my_page_driver.explicit_wait_for_element(dropdown)
my_page_driver.select_dropdown_by_text(dropdown, "Option 1")
my_page_driver.wait_for_seconds(1)
my_page_driver.select_dropdown_by_value(dropdown, "2")
my_page_driver.wait_for_seconds(1)
my_page_driver.select_dropdown_by_index(dropdown, 1)

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()
