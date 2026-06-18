from selenium_day_7 import SeleniumDay7
from selenium.webdriver.common.by import By


MY_URL = "https://the-internet.herokuapp.com/infinite_scroll"

heading_text = (By.XPATH, "//h3")

my_page_driver = SeleniumDay7()
my_page_driver.go(MY_URL)

my_page_driver.wait_for_element(heading_text)
my_page_driver.run_javascript("window.scrollTo(0, document.body.scrollHeight);")
my_page_driver.wait_for_seconds(2)
my_page_driver.run_javascript("window.scrollTo(0, 0);")

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()
