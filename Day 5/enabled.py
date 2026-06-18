from selenium_day_5 import SeleniumDay5
from selenium.webdriver.common.by import By

# data
URL = "https://www.saucedemo.com/"
USERNAME = "visual_user"
PASSWORD = "secret_sauce"

# locator login page
username_textbox = (By.ID, "user-name")
password_textbox = (By.ID, "password")
login_button = (By.ID, "login-button")
all_links = (By.TAG_NAME, "a")

# locator home page
app_logo = (By.XPATH, "//div[@class='app_logo']")

my_browser = SeleniumDay5()
my_browser.navigate_to(URL)
my_browser.wait_for_element_to_be_visible(username_textbox)
my_browser.fill_textbox(username_textbox, USERNAME)
my_browser.wait_for_element_to_be_visible(password_textbox)
my_browser.fill_textbox(password_textbox, PASSWORD)
my_browser.wait_for_element_to_be_visible(login_button)
my_browser.click_on_element(login_button)
print("Logo:", my_browser.enabled_or_not(app_logo))
my_browser.exit_web_driver()