from config.config import BASE_URL
from page.project_page import ProjectPage
from page.home_page import HomePage

def test_project(setup):
    driver = setup
    driver.get(BASE_URL)
    home_page = HomePage(driver)
    home_page.click_on_project("Racer")
    project_page = ProjectPage(driver)
    project_page.click_home_button()
