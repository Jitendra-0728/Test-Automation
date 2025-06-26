import time

from selenium import webdriver
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
# 1 -- CheckBox Selection - Static
#driver.find_element(By.ID, "checkBoxOption2").click()

# 2 -- CheckBox Selection - Dynamically
checkbox = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print("count of check box : ", len(checkbox))

for check in checkbox:
    if check.get_attribute("value") == "option2":       #get_attribute("value") --- used to check attribute with multiple value
        check.click()
        assert check.is_selected(), "Not selected"      # assertion
        break
print(check.get_attribute("value"))                     # print the selected value

# ____________________________________________________________________
# 1 -- Radio Button Selection - Static
driver.find_element(By.XPATH, "//input[@value='radio1']").click()

# 2 -- Radio Button Selection - Static
radiov = driver.find_elements(By.XPATH, "//input[@type='radio']")
radiov[1].click()
assert radiov[1].is_selected(), "Radio 1 button Not selected"

# 3 -- Radio Button Selection - Dynamic
radio = driver.find_elements(By.XPATH, "//input[@type='radio']")
print("count of radio button : ", len(radio))

for radios in radio:
    if radios.get_attribute("value") == "radio3":
        radios.click()
        assert radios.is_selected(), "Radio button Not selected"
        break
print(radios.get_attribute("value"))

# ____________________________________________________________________
# Display Field / Hiding Mechanism
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "show-textbox").click()
assert driver.find_element(By.ID, "displayed-text").is_displayed()

# ____________________________________________________________________
# alert / Pop-up handling
driver.find_element(By.XPATH, "//input[@id='name']").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert =driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()

driver.find_element(By.ID, "confirmbtn").click()
alert=driver.switch_to.alert
time.sleep(1)
alert.dismiss()


time.sleep(2)
driver.close()
