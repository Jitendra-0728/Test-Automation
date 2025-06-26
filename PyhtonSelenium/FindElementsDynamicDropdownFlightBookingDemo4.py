import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ServiceObj = Service("D:\SOFT\WEBDRIVERS\chromedriver-win64\chromedriver.exe")
driver =webdriver.Chrome(service=ServiceObj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

# ____________________________________________________________________
# Drop Down Operation

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)

# Get List of Elements
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")     # paraent to child --- /a
print("Count of Matching countries : ",len(countries))

for country in countries:
    if country.text=="India":
        country.click()
        break

# Check input value selected of not
#print(driver.find_element(By.ID, "autosuggest").text)      #.text --- is not work here because India is dynamically changed text. -- .text only applicable on static text
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))     # get_attribute("value") -- used to get dynamically changed value after the operations ---javascript DOM

# Assertion ways ---
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
assert "India" in driver.find_element(By.ID, "autosuggest").get_attribute("value")


time.sleep(2)
driver.close()
