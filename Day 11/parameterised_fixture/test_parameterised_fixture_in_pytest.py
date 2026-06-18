import pytest
from selenium import webdriver

@pytest.fixture(params=["edge", "chrome"])
def setup(request):
    if request.param == "edge":
        driver = webdriver.Edge()
    elif request.param == "chrome":
        driver = webdriver.Chrome()

    driver.maximize_window()
    yield driver
    driver.quit()


def test_my_site(setup):
    setup.get("https://vaibhavkheriwal.netlify.app/")
    print(setup.title)