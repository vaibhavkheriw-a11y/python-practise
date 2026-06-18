from locators.login_locators import LoginLocators

class LoginPage:

    def __init__(self, my_page_driver):
        self.my_page_driver = my_page_driver

    def enter_username(self, username):
        self.my_page_driver.fill_data(LoginLocators.username_textbox, username)

    def enter_password(self, password):
        self.my_page_driver.fill_data(LoginLocators.password_textbox, password)

    def click_login_button(self):
        self.my_page_driver.click_on_element(LoginLocators.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_login_page_heading(self):
        return self.my_page_driver.get_text_of_element(LoginLocators.login_page_heading)

    def get_flash_message(self):
        return self.my_page_driver.get_text_of_element(LoginLocators.flash_message)

    def get_secure_area_heading(self):
        return self.my_page_driver.get_text_of_element(LoginLocators.secure_area_heading)

    def logout(self):
        self.my_page_driver.click_on_element(LoginLocators.logout_button)

    def is_login_button_displayed(self):
        return self.my_page_driver.find_element(LoginLocators.login_button).is_displayed()

    def is_logout_button_displayed(self):
        return self.my_page_driver.find_element(LoginLocators.logout_button).is_displayed()
