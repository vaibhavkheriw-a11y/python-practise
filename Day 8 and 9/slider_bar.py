from selenium_day_8 import SeleniumDay8
from selenium.webdriver.common.by import By


MY_URL = "https://jqueryui.com/slider/"

demo_frame = (By.CLASS_NAME, "demo-frame")
slider_handle = (By.XPATH, "//span[contains(@class, 'ui-slider-handle')]")

my_page_driver = SeleniumDay8()
my_page_driver.go(MY_URL)

my_page_driver.wait_for_frame_and_switch(demo_frame)
my_page_driver.explicit_wait_for_element(slider_handle)
my_page_driver.drag_slider_by_offset(slider_handle, 100, 0)

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()
