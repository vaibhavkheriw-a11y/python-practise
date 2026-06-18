import pytest

@pytest.fixture(scope="package")
def run_before_and_after():
    print("Hi.. package started")
    yield
    print("Bye.. package ended")

def test_student_name(run_before_and_after):
    print("Student name is Vaibhav")

def test_course_name(run_before_and_after):
    print("Course name is Selenium Python")