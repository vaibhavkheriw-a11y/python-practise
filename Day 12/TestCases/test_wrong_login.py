from Base.base_driver import BaseDriver
from Pages.login_page import LoginPage
from Utilities.read_config import ReadConfig
from Utilities.read_test_data import ReadTestData


my_page_driver = BaseDriver()

try:
    url = ReadConfig.get_config_value("app", "base_url")

    my_page_driver.go(url)
    login_page = LoginPage(my_page_driver)
    login_page.login("this is", "wrong")

except Exception:
    my_page_driver.take_screenshot("login_test_failed.png")
    raise

finally:
    my_page_driver.wait_for_seconds(2)
    my_page_driver.exit_webdriver()
