from selenium_day_8 import SeleniumDay8
from selenium.webdriver.common.by import By


MY_URL = "https://demoqa.com/buttons"

right_click_button = (By.ID, "rightClickBtn")
right_click_message = (By.ID, "rightClickMessage")

my_page_driver = SeleniumDay8()
my_page_driver.go(MY_URL)

my_page_driver.explicit_wait_for_element(right_click_button)
my_page_driver.wait_for_element_clickable(right_click_button)
my_page_driver.right_click(right_click_button)
my_page_driver.explicit_wait_for_element(right_click_message)

print(my_page_driver.get_text_of_element(right_click_message))

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()
