from config.config import BASE_URL
from page.home_page import HomePage


def test_about(setup):
    driver = setup
    driver.get(BASE_URL)

    home_page = HomePage(driver)
    home_page.click_about_button()
    print(driver.title)
