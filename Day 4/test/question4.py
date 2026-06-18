#Click an element using python seleniun

from page.seleniumHandlePage import SeleniumHandlePage

#locator
qaPracticeLink = "//a[text()='QA Practice']"

myPageWebDriver = SeleniumHandlePage()
myPageWebDriver.go("https://qa-practice.razvanvancea.ro/")
myPageWebDriver.waitForElementToBeVisible(qaPracticeLink)
myPageWebDriver.waitForElementToBeClickable(qaPracticeLink)
myPageWebDriver.clickOnElement(qaPracticeLink)
myPageWebDriver.waitForSeconds(2)
myPageWebDriver.exitWebDriver()