from selenium_day_6 import SeleniumDay6
from selenium.webdriver.common.by import By
import os

MY_URL = "https://demoqa.com/upload-download"

upload_and_download_dropdown_element = (By.XPATH, "//span[text()='Upload and Download']")
download_button = (By.XPATH, "//a[text()='Download']")

my_page_driver = SeleniumDay6()
my_page_driver.go(MY_URL)
my_page_driver.wait_for_element(upload_and_download_dropdown_element)
my_page_driver.wait_for_element_clickable(upload_and_download_dropdown_element)
my_page_driver.click_on_element(upload_and_download_dropdown_element)

list_of_files_befor_download = os.listdir(os.path.join(os.path.expanduser("~"), "Downloads"))

my_page_driver.wait_for_element(download_button)
my_page_driver.wait_for_element_clickable(download_button)
my_page_driver.click_on_element(download_button)
my_page_driver.wait_for_seconds(5)
 
list_of_files_after_download = os.listdir(os.path.join(os.path.expanduser("~"), "Downloads"))
new_file = set(list_of_files_after_download) - set(list_of_files_befor_download)

if new_file: print("Download Success: ", new_file)
else: assert False, f"Download failed"

my_page_driver.exit_webdriver()