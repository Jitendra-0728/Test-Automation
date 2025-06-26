import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PyhtonSelenium.UiControlsDemo5 import alert

ServiceObj = Service("D:\SOFT\WEBDRIVERS\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=ServiceObj)

driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/angularpractice/shop")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

# ____________________________________________________________________

products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    selectedProduct = product.find_element(By.XPATH, "div/h4/a").text
    if selectedProduct == "Blackberry":
        product.find_element(By.XPATH, "div[2]/button").click()

driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()

driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
successMessage = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(successMessage)

assert "Success" in successMessage




time.sleep(2)
driver.close()