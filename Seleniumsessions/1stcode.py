import time
from selenium import webdriver
driver=webdriver.Chrome()
print(selenium.__version__)

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
namesearch=driver.find_element("id", "name")
namesearch.send_keys("Rishikesh verma")

# Optional: Close the browser window after a delay
time.sleep(10)
driver.quit ()