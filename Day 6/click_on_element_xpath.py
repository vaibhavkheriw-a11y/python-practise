from selenium_day_6 import SeleniumDay6
from selenium.webdriver.common.by import By

MY_URL = "https://demoqa.com/upload-download"

elements_dropdown = (By.XPATH, "//div[text()='Elements']")
upload_and_download_dropdown_element = (By.XPATH, "//span[text()='Upload and Download']")

my_page_driver = SeleniumDay6()
my_page_driver.go(MY_URL)
my_page_driver.wait_for_element(elements_dropdown)
my_page_driver.wait_for_element_clickable(elements_dropdown)
my_page_driver.click_on_element(elements_dropdown)
my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()