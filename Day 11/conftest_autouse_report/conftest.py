import pytest
from selenium import webdriver


@pytest.fixture(params=["edge", "chrome"], autouse=True)
def setup(request):
    if request.param == "edge":
        driver = webdriver.Edge()
    elif request.param == "chrome":
        driver = webdriver.Chrome()

    driver.maximize_window()
    request.module.driver = driver

    yield

    driver.quit()