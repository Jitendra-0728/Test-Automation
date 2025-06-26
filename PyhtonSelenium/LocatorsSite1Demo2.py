import secrets
from select import select

from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

ServiceObj = Service("D:\SOFT\WEBDRIVERS\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=ServiceObj)

# Locators - ID, XPATH, CSSSelector, NAME, CLASS_NAME, LinkText
# XPATH --  //tagName[@attribute = "value"]
# CSSSelector --  tagName[attribute="value"]

FName = "Jitendra"
email = "Jitendra" + secrets.token_hex(5) + "@gmail.com"
password = "Jiten@" + secrets.token_hex(4)

with open("LocatorsSite1Demo2credentials.txt", "a") as Writer:         # "a" - used to append multiple value(list of value) else using "w","r" it only sore single value
    Writer.write(f"Email: {email}\nPassword: {password}\n\n")

# ____________________________________________________________________

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "name").send_keys(FName)
driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(password)

# CheckBox ---
driver.find_element(By.ID, "exampleCheck1").click()

# Static DropDown ---
dropDown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropDown.select_by_index(1)                 # Female
dropDown.select_by_visible_text("Male")

# Radio Button ---
driver.find_element(By.XPATH, "//input[@id='inlineRadio2']").click()

# Calender --- DOB
#driver.find_element(By.XPATH, "//input[@name='bday']").send_keys("12/02/1999")
time.sleep(2)
# Submit Button
driver.find_element(By.CLASS_NAME, "btn-success").click()

# Alert Message
messages = driver.find_element(By.CLASS_NAME, "alert").text
print(messages)
assert "Success" in messages

# ____________________________________________________________________

# Shopping Page
driver.find_element(By.LINK_TEXT, "ProtoCommerce").click()  # Logo Test
driver.find_element(By.LINK_TEXT, "Home").click()       # HomeButton Test
driver.find_element(By.LINK_TEXT, "Shop").click()       # ShopButton Test

time.sleep(5)
driver.close()
