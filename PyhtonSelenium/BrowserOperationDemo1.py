from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("D:\SOFT\WEBDRIVERS\chromedriver-win64\chromedriver.exe")     # firefox -- \Firefox Webdriver\geckodriver.exe
driver = webdriver.Chrome(service=service_obj)                                      # edge   -- \Edge Webdriver\msedgedriver.exe

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print(driver.title)
print(driver.current_url)
driver.minimize_window()
driver.back()
driver.forward()
driver.refresh()


driver.close()