import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ServiceObj = Service("D:\SOFT\WEBDRIVERS\chromedriver-win64\chromedriver.exe")
driver =webdriver.Chrome(service=ServiceObj)

name = "jiten"

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

# ____________________________________________________________________

# parent to child and viceVersa

driver.find_element(By.LINK_TEXT, "Click Here").click()

windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
time.sleep(2)
driver.close()

driver.switch_to.window(windowsOpened[0])
assert "Opening a new window" == driver.find_element(By.XPATH, "//h3").text

time.sleep(2)
driver.close()


# ____________________________________________________________________
