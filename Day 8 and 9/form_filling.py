from selenium_day_8 import SeleniumDay8
from selenium.webdriver.common.by import By


MY_URL = "https://demoqa.com/text-box"

full_name_textbox = (By.ID, "userName")
email_textbox = (By.ID, "userEmail")
current_address_textbox = (By.ID, "currentAddress")
permanent_address_textbox = (By.ID, "permanentAddress")
submit_button = (By.ID, "submit")
output_box = (By.ID, "output")

my_page_driver = SeleniumDay8()
my_page_driver.go(MY_URL)

my_page_driver.explicit_wait_for_element(full_name_textbox)
my_page_driver.fill_data(full_name_textbox, "Vaibhav Kheriwal")
my_page_driver.fill_data(email_textbox, "vaibhav@example.com")
my_page_driver.fill_data(current_address_textbox, "Current Address")
my_page_driver.fill_data(permanent_address_textbox, "Permanent Address")
my_page_driver.explicit_wait_for_element(submit_button, seconds=5)
my_page_driver.wait_for_element_clickable(submit_button)
my_page_driver.scroll_to_element(submit_button)
my_page_driver.click_on_element(submit_button)
my_page_driver.explicit_wait_for_element(output_box)

print(my_page_driver.get_text_of_element(output_box))

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()
