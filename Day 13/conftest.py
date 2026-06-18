import os
import sys
import pytest

PROJECT_PATH = os.path.dirname(__file__)
sys.path.append(PROJECT_PATH)

from page.base_page import BasePage
from page.login_page import LoginPage
from test_data.login_test_data import LoginTestData

@pytest.fixture()
def base_page(request):
    my_page_driver = BasePage()
    my_page_driver.go(LoginTestData.base_url)

    try:
        yield my_page_driver
    except Exception:
        my_page_driver.take_screenshot(f"{request.node.name}.png")
        raise
    finally:
        my_page_driver.exit_webdriver()

@pytest.fixture()
def login_page(base_page):
    return LoginPage(base_page)

@pytest.fixture()
def login_logout(base_page):
    login_page_obj = LoginPage(base_page)
    login_page_obj.login(LoginTestData.valid_username, LoginTestData.valid_password)
    yield login_page_obj
    login_page_obj.logout()
