from selenium_day_6 import SeleniumDay6
from selenium.webdriver.common.by import By

MY_URL = "https://the-internet.herokuapp.com/windows"

heading_text = (By.XPATH, "//h3[contains(text(), 'new')]")

my_page_driver = SeleniumDay6()
my_page_driver.go(MY_URL)
my_page_driver.wait_for_element(heading_text)
print(my_page_driver.get_text_of_element(heading_text))
my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()