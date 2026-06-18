import pytest
@pytest.fixture(scope='function')
def run_befor_and_after():
    print("\nHi..")
    yield
    print("\nBye..")

def test_my_name(run_befor_and_after):
    print("\nMy name is Vaibhav Kh...")

def test_my_friend_name(run_befor_and_after):
    print("\nRiya is my friend")