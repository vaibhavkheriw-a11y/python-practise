import pytest

driver = None

@pytest.mark.regression
@pytest.mark.skip
def test_google():
    driver.get("https://www.google.com/")
    print(driver.title)