from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

class SeleniumHandlePage:
    def __init__(self):
        self.myWebDriver = webdriver.Chrome()

    def go(self, url=""):
        self.myWebDriver.get(url)

    def getTitle(self):
        return print(f"Page title: {self.myWebDriver.title}")
    
    def clickOnElement(self, clickXpath):
        clickOn = self.myWebDriver.find_element(By.XPATH, clickXpath)
        clickOn.click()
    
    def selectDropdown(self, dropdownXpath, selectValueString):
        selectDropdown = self.myWebDriver.find_element(By.XPATH, dropdownXpath)
        selectValue = Select(selectDropdown)
        selectValue.select_by_value(selectValueString)

    def waitForElementToBeClickable(self, elementXpath):
        WebDriverWait(self.myWebDriver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, elementXpath)))
        
    def waitForElementToBeVisible(self, elementXpath):
        WebDriverWait(self.myWebDriver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, elementXpath)))

    def waitForSeconds(self, seconds):
        time.sleep(seconds)

    def findElements(self, elementsXpath):
        allElement = self.myWebDriver.find_elements(By.XPATH, elementsXpath)
        allElementName = []
        for element in allElement:
            if element.accessible_name:
                allElementName.append(element.accessible_name)
        return print(f"{allElementName}")

    def exitWebDriver(self):
        self.myWebDriver.close()