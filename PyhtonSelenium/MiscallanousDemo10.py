import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# ____________________________________________________________________

chromeOptions = webdriver.ChromeOptions()

# Execution Without Browser UI - headless
chromeOptions.add_argument("--headless")

# Ignore SSL Certificate
chromeOptions.add_argument("--ignore-certificate-errors")

# ____________________________________________________________________

ServiceObj = Service("D:\SOFT\WEBDRIVERS\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=ServiceObj, options=chromeOptions)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
print(driver.current_url)

# ____________________________________________________________________
# Scrolling
#driver.execute_script("window.scrollBy(0, 1000")                                # for Specific area
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")        # for direct to bottom of the page

# ____________________________________________________________________
# ScreenShot

driver.get_screenshot_as_file("Screenshot1.png")


time.sleep(2)
driver.close()