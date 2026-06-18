import pytest

@pytest.fixture(scope="class")
def run_before_and_after():
    print("\nHi..")
    yield
    print("\nBye..")


class TestNames:

    def test_my_name(self, run_before_and_after):
        print("\nMy name is Vaibhav Kh...")

    def test_my_friend_name(self, run_before_and_after):
        print("\nRiya is my friend")

