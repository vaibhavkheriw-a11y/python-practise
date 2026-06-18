from selenium_day_8 import SeleniumDay8
from selenium.webdriver.common.by import By


MY_URL = "https://the-internet.herokuapp.com/dynamic_loading/1"

start_button = (By.XPATH, "//button[text()='Start']")
finish_text = (By.ID, "finish")

my_page_driver = SeleniumDay8()
my_page_driver.go(MY_URL)

my_page_driver.explicit_wait_for_element(start_button)
my_page_driver.wait_for_element_clickable(start_button)
my_page_driver.click_on_element(start_button)
my_page_driver.explicit_wait_for_element(finish_text, 15)

print(my_page_driver.get_text_of_element(finish_text))

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()
