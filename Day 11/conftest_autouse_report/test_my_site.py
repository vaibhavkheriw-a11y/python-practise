import pytest
driver = None

@pytest.mark.regression
def test_my_site():
    driver.get("https://vaibhavkheriwal.netlify.app/")
    print(driver.title)