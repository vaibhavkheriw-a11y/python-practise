import pytest

@pytest.fixture(scope="session")
def run_before_and_after():
    print("Session started")
    yield
    print("Session ended")

def test_valid_login(run_before_and_after):
    print("Valid login test running")

def test_valid_logout(run_before_and_after):
    print("Valid logout test running")