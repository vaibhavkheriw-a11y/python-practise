from selenium.webdriver.common.by import By

class HomePage:

    about_button = (By.XPATH, "//button[text()='About']")
    github_button = (By.XPATH, "//button[text()='GitHub']")

    def __init__(self, driver):
        self.driver = driver

    def click_about_button(self):
        self.driver.find_element(*self.about_button).click()

    def click_github_button(self):
        self.driver.find_element(*self.github_button).click()

    def click_on_project(self, name = ""):
        project_locator = (By.XPATH, f"//h3[contains(text(), '{name}')]")
        self.driver.find_element(*project_locator).click()
