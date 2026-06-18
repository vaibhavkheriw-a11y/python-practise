from selenium.webdriver.common.by import By

class LoginLocators:

    login_page_heading = (By.XPATH, "//h2[text()='Login Page']")
    username_textbox = (By.ID, "username")
    password_textbox = (By.ID, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    flash_message = (By.ID, "flash")
    secure_area_heading = (By.XPATH, "//h2[contains(text(), 'Secure Area')]")
    logout_button = (By.XPATH, "//a[contains(@href, '/logout')]")
