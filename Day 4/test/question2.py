#Select a value from drop down using python selenium

from page.seleniumHandlePage import SeleniumHandlePage

#locator
dropdownOptionOnMenu = "//a[@id='dropdowns']"
dropdown = "//select[@id='dropdown-menu']"

myPageWebDriver = SeleniumHandlePage()
myPageWebDriver.go("https://qa-practice.razvanvancea.ro/")
myPageWebDriver.waitForElementToBeVisible(dropdownOptionOnMenu)
myPageWebDriver.waitForElementToBeClickable(dropdownOptionOnMenu)
myPageWebDriver.clickOnElement(dropdownOptionOnMenu)
myPageWebDriver.waitForElementToBeVisible(dropdown)
myPageWebDriver.waitForElementToBeClickable(dropdown)
myPageWebDriver.selectDropdown(dropdown, "India")
myPageWebDriver.waitForSeconds(2)
myPageWebDriver.exitWebDriver()