from selenium_day_7 import SeleniumDay7
from selenium.webdriver.common.by import By


MY_URL = "https://output.jsbin.com/osebed/2"

multi_select_dropdown = (By.ID, "fruits")

my_page_driver = SeleniumDay7()
my_page_driver.go(MY_URL)

my_page_driver.wait_for_element(multi_select_dropdown)
my_page_driver.select_multi_options_by_text(multi_select_dropdown, ["Apple", "Orange"])
my_page_driver.wait_for_seconds(2)
my_page_driver.deselect_all_multi_options(multi_select_dropdown)

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()
