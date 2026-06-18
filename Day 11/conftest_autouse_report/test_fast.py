import pytest
driver = None

@pytest.mark.sanity
def test_fast():
    driver.get("https://fast.com/")
    print(driver.title)