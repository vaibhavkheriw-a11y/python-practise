from selenium_day_6 import SeleniumDay6
from selenium.webdriver.common.by import By

MY_URL = "https://the-internet.herokuapp.com/windows"

new_tab_link = (By.XPATH, "//a[text()='Click Here']")
next_tab_heading = (By.XPATH, "//h3")

my_page_driver = SeleniumDay6()
my_page_driver.go(MY_URL)
my_page_driver.wait_for_element(new_tab_link)
my_page_driver.wait_for_element_clickable(new_tab_link)
my_page_driver.click_on_element(new_tab_link)

my_page_driver.switch_to_tab(1)
my_page_driver.wait_for_element(next_tab_heading)

my_page_driver.switch_to_tab(0)
my_page_driver.wait_for_element(new_tab_link)

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()