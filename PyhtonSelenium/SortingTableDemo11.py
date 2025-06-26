import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

ServiceObj = Service("D:\SOFT\WEBDRIVERS\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=ServiceObj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

# ____________________________________________________________________
# empty list to append veggies while running for loop

browserVeggiesList = []

# ____________________________________________________________________
# Click on the table header to chceck wheather it is sorted or not

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
newVeggiesList = driver.find_elements(By.XPATH, "//tr/td[1]")

for veggis in newVeggiesList:
    browserVeggiesList.append(veggis.text)

newBrowserVeggiesList=browserVeggiesList.copy()             # browser list stored into new list for assertion/comparing using copy()
print("browser copy", browserVeggiesList)

# ____________________________________________________________________
# sort browser list
browserVeggiesList.sort()

# ____________________________________________________________________
# assert - compare
# assert browserVeggiesList == newBrowserVeggiesList            # Simple way
# print("compaired List",browserVeggiesList)

if browserVeggiesList == newBrowserVeggiesList:                 # Using if condition and print the message
    print("Browser list Sorted Succesfully")


# ____________________________________________________________________

time.sleep(2)
driver.close()
