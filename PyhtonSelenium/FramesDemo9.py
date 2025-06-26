import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

ServiceObj = Service("D:\SOFT\WEBDRIVERS\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ServiceObj)


driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

# ____________________________________________________________________

driver.find_element(By.XPATH, "//div[@aria-label='Close']").click()     # used due to extra error about website policy

driver.switch_to.frame("mce_0_ifr")          # Switch TO frame

driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("In the frame")

driver.switch_to.default_content()      # Return to the main page

print(driver.find_element(By.TAG_NAME, "h3").text)

time.sleep(2)
driver.close()



