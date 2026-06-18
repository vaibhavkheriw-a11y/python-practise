from selenium_day_6 import SeleniumDay6
from selenium.webdriver.common.by import By
import os

MY_URL = "https://demoqa.com/upload-download"
UPLOAD_FILE_PATH = os.path.abspath("a.txt")

upload_and_download_dropdown_element = (By.XPATH, "//span[text()='Upload and Download']")
upload_file = (By.ID, "uploadFile")

my_page_driver = SeleniumDay6()
my_page_driver.go(MY_URL)
my_page_driver.wait_for_element(upload_and_download_dropdown_element)
my_page_driver.wait_for_element_clickable(upload_and_download_dropdown_element)
my_page_driver.click_on_element(upload_and_download_dropdown_element)

my_page_driver.wait_for_element(upload_file)
my_page_driver.wait_for_element_clickable(upload_file)
my_page_driver.fill_data(upload_file, UPLOAD_FILE_PATH)

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()