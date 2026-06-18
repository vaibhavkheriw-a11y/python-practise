from Base.base_driver import BaseDriver
from Pages.login_page import LoginPage
from Utilities.read_config import ReadConfig
from Utilities.read_test_data import ReadTestData


my_page_driver = BaseDriver()


url = ReadConfig.get_config_value("app", "base_url")
login_data = ReadTestData.get_login_data()

my_page_driver.go(url)

login_page = LoginPage(my_page_driver)
login_page.login(login_data["username"], login_data["password"])

assert login_page.get_app_logo_text() == "Swag Labs"
print("Login test passed")

my_page_driver.wait_for_seconds(2)
my_page_driver.exit_webdriver()
