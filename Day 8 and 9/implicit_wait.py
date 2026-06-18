from selenium_day_8 import SeleniumDay8
from selenium.webdriver.common.by import By


MY_URL = "https://www.saucedemo.com/"

username_textbox = (By.ID, "user-name")
password_textbox = (By.ID, "password")

my_page_driver = SeleniumDay8()
my_page_driver.implicit_wait(10)
my_page_driver.go(MY_URL)

my_page_driver.fill_data(username_textbox, "standard_user")
my_page_driver.fill_data(password_textbox, "secret_sauce")

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()
