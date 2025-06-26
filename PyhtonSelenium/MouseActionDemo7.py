import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ServiceObj = Service("D:\SOFT\WEBDRIVERS\chromedriver-win64\chromedriver.exe")
driver =webdriver.Chrome(service=ServiceObj)

name = "jiten"

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

# ____________________________________________________________________

action = ActionChains(driver)

action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

time.sleep(2)
driver.close()

# ____________________________________________________________________