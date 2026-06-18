from selenium_day_8 import SeleniumDay8
from selenium.webdriver.common.by import By


MY_URL = "https://the-internet.herokuapp.com/hovers"

first_image = (By.XPATH, "(//div[@class='figure'])[1]")
first_image_caption = (By.XPATH, "(//div[@class='figcaption']/h5)[1]")

my_page_driver = SeleniumDay8()
my_page_driver.go(MY_URL)

my_page_driver.explicit_wait_for_element(first_image)
my_page_driver.mouse_over(first_image)
my_page_driver.explicit_wait_for_element(first_image_caption)

print(my_page_driver.get_text_of_element(first_image_caption))

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()
