import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
showbtn = driver.find_element(By.ID, value="show-textbox")
driver.execute_script("arguments[0].scrollIntoView();", showbtn)
showbtn.click()  # Clicking the button to show the textbox
textbox = driver.find_element(By.ID, value="displayed-text")
textbox.send_keys("test")  # Entering "test" into the textbox
time.sleep(2)  # Wait for demonstration purpose
driver.quit()
