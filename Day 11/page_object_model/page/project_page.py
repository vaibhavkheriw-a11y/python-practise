from selenium.webdriver.common.by import By

class ProjectPage:

    home_button = (By.XPATH, "//button[text()='Home']")

    def __init__(self, driver):
        self.driver = driver

    def click_home_button(self):
        self.driver.find_element(*self.home_button).click()
