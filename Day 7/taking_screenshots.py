from selenium_day_7 import SeleniumDay7
from selenium.webdriver.common.by import By
import os


MY_URL = "https://www.saucedemo.com/"

username_textbox = (By.ID, "user-name")
screenshot_path = os.path.join(os.path.dirname(__file__), "a.png")

my_page_driver = SeleniumDay7()
my_page_driver.go(MY_URL)

my_page_driver.wait_for_element(username_textbox)
my_page_driver.take_screenshot(screenshot_path)

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()
