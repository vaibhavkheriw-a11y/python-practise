from day_10 import Day10
from selenium.webdriver.common.by import By

URL = "https://vaibhavkheriwal.netlify.app/"

wd = Day10()
wd.go(URL)
wd.url_to_be(URL)