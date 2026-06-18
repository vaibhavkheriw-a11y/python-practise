from selenium_day_6 import SeleniumDay6
from selenium.webdriver.common.by import By

MY_URL = "https://the-internet.herokuapp.com/login"
USER = "tomsmith"
PASS = "SuperSecretPassword!"

heading_text = (By.XPATH, "//h2[contains(text(), 'Login Page')]")
subheading_test = (By.CLASS_NAME, "subheader")
elemental_selenium_link = (By.LINK_TEXT, "Elemental Selenium")
elemental_selenium_partial_link = (By.PARTIAL_LINK_TEXT, "Elemental")
username_textbox = (By.NAME, "username")
password_textbox = (By.ID, "password")
login_button = (By.TAG_NAME, "button")
logged_in = (By.ID, "flash")

my_page_driver = SeleniumDay6()
my_page_driver.go(MY_URL)
my_page_driver.wait_for_element(heading_text)
my_page_driver.wait_for_element(subheading_test)
my_page_driver.wait_for_element(elemental_selenium_link)
my_page_driver.wait_for_element(elemental_selenium_partial_link)
my_page_driver.wait_for_element(username_textbox)
my_page_driver.wait_for_element(password_textbox)
my_page_driver.wait_for_element(login_button)

print(my_page_driver.get_text_of_element(heading_text))
print(my_page_driver.get_text_of_element(subheading_test))
print(my_page_driver.get_text_of_element(elemental_selenium_link))
print(my_page_driver.get_text_of_element(elemental_selenium_partial_link))

my_page_driver.fill_data(username_textbox, USER)
my_page_driver.fill_data(password_textbox, PASS)
my_page_driver.click_on_element(login_button)
my_page_driver.wait_for_element(logged_in)

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()