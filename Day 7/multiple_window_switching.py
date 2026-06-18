from selenium_day_7 import SeleniumDay7
from selenium.webdriver.common.by import By


MY_URL = "https://the-internet.herokuapp.com/windows"

new_tab_link = (By.XPATH, "//a[text()='Click Here']")
new_tab_heading = (By.XPATH, "//h3")

my_page_driver = SeleniumDay7()
my_page_driver.go(MY_URL)

my_page_driver.wait_for_element(new_tab_link)
my_page_driver.wait_for_element_clickable(new_tab_link)
my_page_driver.click_on_element(new_tab_link)

my_page_driver.switch_to_tab(1)
my_page_driver.wait_for_element(new_tab_heading)
print(my_page_driver.get_text_of_element(new_tab_heading))

my_page_driver.switch_to_tab(0)
my_page_driver.wait_for_element(new_tab_link)

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()
