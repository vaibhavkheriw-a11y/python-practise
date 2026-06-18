from selenium_day_8 import SeleniumDay8
from selenium.webdriver.common.by import By


MY_URL = "https://jqueryui.com/droppable/"

demo_frame = (By.CLASS_NAME, "demo-frame")
drag_element = (By.ID, "draggable")
drop_element = (By.ID, "droppable")

my_page_driver = SeleniumDay8()
my_page_driver.go(MY_URL)

my_page_driver.wait_for_frame_and_switch(demo_frame)
my_page_driver.explicit_wait_for_element(drag_element)
my_page_driver.explicit_wait_for_element(drop_element)
my_page_driver.drag_and_drop(drag_element, drop_element)

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()
