from test_data.login_test_data import LoginTestData


def test_login_with_valid_user(login_page):
    login_page.login(LoginTestData.valid_username, LoginTestData.valid_password)

    assert "You logged into a secure area!" in login_page.get_flash_message()
    print("Valid login test passed")


def test_login_with_wrong_username(login_page):
    login_page.login(LoginTestData.wrong_username, LoginTestData.wrong_password)

    assert "Your username is invalid!" in login_page.get_flash_message()
    print("Wrong username test passed")


def test_login_with_wrong_password(login_page):
    login_page.login(LoginTestData.valid_username, LoginTestData.wrong_password)

    assert "Your password is invalid!" in login_page.get_flash_message()
    print("Wrong password test passed")


def test_login_with_empty_username(login_page):
    login_page.login("", LoginTestData.valid_password)

    assert "Your username is invalid!" in login_page.get_flash_message()
    print("Empty username test passed")


def test_login_with_empty_password(login_page):
    login_page.login(LoginTestData.valid_username, "")

    assert "Your password is invalid!" in login_page.get_flash_message()
    print("Empty password test passed")


def test_secure_page_after_login(login_logout):
    assert login_logout.get_secure_area_heading() == "Secure Area"
    assert login_logout.is_logout_button_displayed()
    print("Secure page after login test passed")


def test_logout_functionality(login_page):
    login_page.login(LoginTestData.valid_username, LoginTestData.valid_password)
    login_page.logout()

    assert "You logged out of the secure area!" in login_page.get_flash_message()
    assert login_page.is_login_button_displayed()
    print("Logout test passed")
