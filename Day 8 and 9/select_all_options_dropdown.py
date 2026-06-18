from selenium_day_8 import SeleniumDay8
from selenium.webdriver.common.by import By


MY_URL = "https://output.jsbin.com/osebed/2"

multi_select_dropdown = (By.ID, "fruits")

my_page_driver = SeleniumDay8()
my_page_driver.go(MY_URL)

my_page_driver.explicit_wait_for_element(multi_select_dropdown)
my_page_driver.select_all_options_from_dropdown(multi_select_dropdown)

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()
