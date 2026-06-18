#Find no of elements on page using python selenium

from page.seleniumHandlePage import SeleniumHandlePage

#locator
locatorOfAllElement = "//*"

myPageWebDriver = SeleniumHandlePage()
myPageWebDriver.go("https://vaibhavkheriwal.netlify.app/")
myPageWebDriver.findElements(locatorOfAllElement)
myPageWebDriver.exitWebDriver()