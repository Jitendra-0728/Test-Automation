# implicit_wait()
# driver.implicit_wait(). So let's say if it's a 5 seconds, this is your global timeout to the script.
# Now, if any element is not shown on the page, it will wait a max of 5 seconds for that to show up.
# So 5 seconds is the max timeout.
# if that element is just displayed in 2 seconds, then immediately it identifies that and proceeds
# so it will save you the 3 seconds time. So,

# Exceptional case - implicit wait() on find_elements will not work so we manually need to give time.sleep,
# because find_elements return list and selenium consider empty list also a list, so selenium mark as condition matching and go forward and dont give time to load the products in the list

# ____________________________________________________________________

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


ServiceObj = Service("D:\SOFT\WEBDRIVERS\chromedriver-win64\chromedriver.exe")
driver =webdriver.Chrome(service=ServiceObj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

expectedList= ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList=[]

# ____________________________________________________________________
# Implicit Wait -- Use Globally
driver.implicitly_wait(5)       # if any element is not render so it will wait for max 5 sec

# ____________________________________________________________________

driver.find_element(By.XPATH, "//input[@class='search-keyword']").send_keys("ber")
print(driver.find_element(By.XPATH, "//input[@class='search-keyword']").get_attribute("value"))     # To get input value
time.sleep(2)
# we are using implicit wait still wee cant remove the above time.sleep method,
# because below statement returns list[] of web elements / Pural / multiple products

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")          # chaining    # List of product first
count = len(results)
print(count)

assert count > 0
for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

assert expectedList == actualList
print(actualList)

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# ____________________________________________________________________
total = driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum=0

for i in total:
    sum = sum+int(i.text)
print(sum)

totalAmmount=int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalAmmount

driver.find_element(By.CSS_SELECTOR, "input[class='promoCode']").send_keys("rahulshettyacademy")
print(driver.find_element(By.CSS_SELECTOR, "input[class='promoCode']").get_attribute("value"))      # To get inserted value

driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()

# ____________________________________________________________________
# Explicit Wait --
# use for specific element who takes longer time to render than 5 second
# so if any element takes longer time then its good to use explicit wait along with implicit wait globally

wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@class='promoCode']")))

print(driver.find_element(By.XPATH, "//span[@class='promoInfo']").text)

discountedAmmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(discountedAmmount)
assert totalAmmount > discountedAmmount, "TestCase Fail"

driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

# ____________________________________________________________________

dropdownCountries = Select(driver.find_element(By.XPATH,"//div[@class='wrapperTwo']//div//select"))
dropdownCountries.select_by_visible_text("India")


# Checkbox Validation

checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")       # Uncheck the checkbox
if checkbox.is_selected():
    checkbox.click()

driver.find_element(By.XPATH, "//button[text()='Proceed']").click()         # click to Proceed Button
time.sleep(2)

errorText = driver.find_element(By.XPATH, "//b")                       # Error Message validation
if errorText.is_displayed():
    print(errorText.text)
    assert errorText.text == "Please accept Terms & Conditions"              # Through an error

driver.find_element(By.XPATH, "//input[@type='checkbox']").click()     # Check the Checkbox

driver.find_element(By.XPATH, "//button[text()='Proceed']").click()

# ____________________________________________________________________

time.sleep(2)
driver.close()

# Thank you, your order has been placed successfully You'll be redirected to Home page shortly!!


