import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
selectTable=driver.find_element(By.CLASS_NAME,value="table-display")
rowSelect=driver.find_element(By.CSS_SELECTOR,value="#product > tbody > tr:nth-child(1) > th:nth-child(1)")
print(rowSelect.text)
rowSelect1=driver.find_element(By.CSS_SELECTOR,value="#product > tbody > tr:nth-child(3) > td:nth-child(1)")
print(rowSelect1.text)