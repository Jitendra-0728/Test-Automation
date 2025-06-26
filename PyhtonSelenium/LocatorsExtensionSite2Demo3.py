import time
import secrets
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ServiceObj=Service("D:\SOFT\WEBDRIVERS\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=ServiceObj)

# ____________________________________________________________________

FName = "Jitendra"
LName = "Kute"
email = "Jitendra" + secrets.token_hex(5) + "@gmail.com"
password = "Jiten@" + secrets.token_hex(4)

with open("LocatorsExtensionSite2Demo3credentials.txt", "a") as Writer:         # "a" - used to append multiple value(list of value) else using "w","r" it only sore single value
    Writer.write(f"Email: {email}\nPassword: {password}\n\n")

# ____________________________________________________________________
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Register here").click()
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys(FName)
driver.find_element(By.CSS_SELECTOR, '#lastName').send_keys(LName)
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys(email)
driver.find_element(By.XPATH, "//input[@id='userMobile']").send_keys("8485868888")
driver.find_element(By.XPATH, "//option[@value='2: Student']").click()
driver.find_element(By.XPATH, "//input[@value='Male']").click()
driver.find_element(By.CSS_SELECTOR, "#userPassword").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys(password)
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(2)

# ____________________________________________________________________
# Register Successfully Page ---
print(driver.current_url)
success = driver.find_element(By.CSS_SELECTOR, ".headcolor").text       # .text -- is used or return text when site is already loaded or only static text on page is get fetched
print(success)
assert "Successfully" in success

driver.find_element(By.XPATH, "//button[text() = 'Login']").click()

time.sleep(2)

# ____________________________________________________________________
# Forgot Password ---

driver.find_element(By.CSS_SELECTOR, ".forgot-password-link").click()
print(driver.current_url)
driver.find_element(By.XPATH, "//input[@formcontrolname='userEmail']").send_keys(email)
driver.find_element(By.XPATH, "//input[@id='userPassword']").send_keys(password)
driver.find_element(By.XPATH, "//input[@id='confirmPassword']").send_keys(password)
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()

time.sleep(2)

# ____________________________________________________________________
# Login Page ---
print(driver.current_url)
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys(email)
driver.find_element(By.XPATH, "//input[@id='userPassword']").send_keys(password)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(2)

# ____________________________________________________________________
# Automation Practice HomePage ---

url = driver.current_url
if url == "https://rahulshettyacademy.com/client/dashboard/dash":
    print("Automation Practice HomePage : ", url)

assert "https://rahulshettyacademy.com/client/dashboard/dash" in url, "Login Failed"

time.sleep(2)
driver.close()