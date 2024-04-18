import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
selecttable=driver.find_element(By.ID,value="product")
rowSelect=driver.find_element(By.CSS_SELECTOR,value="#product > thead > tr:nth-child(3) > th:nth-child(3)")
print(rowSelect.text)
