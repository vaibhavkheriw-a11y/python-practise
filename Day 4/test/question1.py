#Get the title of page using python selenium

from page.seleniumHandlePage import SeleniumHandlePage

myPageWebDriver = SeleniumHandlePage()
myPageWebDriver.go("https://vaibhavkheriwal.netlify.app/")
myPageWebDriver.getTitle()
myPageWebDriver.exitWebDriver()