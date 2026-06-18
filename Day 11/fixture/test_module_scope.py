import pytest


@pytest.fixture(scope="module")
def run_before_and_after():
    print("Hi..")
    yield
    print("Bye..")


def test_my_name(run_before_and_after):
    print("My name is Vaibhav Kh...")


def test_my_friend_name(run_before_and_after):
    print("Riya is my friend")


class TestMoreNames:

    def test_city_name(self, run_before_and_after):
        print("My city is Chandigarh")

    def test_country_name(self, run_before_and_after):
        print("My country is India")