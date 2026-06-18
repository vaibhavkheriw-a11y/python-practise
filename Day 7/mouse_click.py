from selenium_day_7 import SeleniumDay7
from selenium.webdriver.common.by import By


MY_URL = "https://demoqa.com/buttons"

click_me_button = (By.XPATH, "//button[text()='Click Me']")
click_message = (By.ID, "dynamicClickMessage")

my_page_driver = SeleniumDay7()
my_page_driver.go(MY_URL)

my_page_driver.wait_for_element(click_me_button)
my_page_driver.wait_for_element_clickable(click_me_button)
my_page_driver.mouse_click(click_me_button)
my_page_driver.wait_for_element(click_message)

print(my_page_driver.get_text_of_element(click_message))

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()
