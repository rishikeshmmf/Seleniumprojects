import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://zenfulnote.co/zenfulnote-admin/login")
driver.maximize_window()
email_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div[2]/form/div/div[1]/div/div/input")
password_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div[2]/form/div/div[2]/div/div/input")
email_input.send_keys("admin@zenfulnote.com")
password_input.send_keys("Zenful@Note##2023")
password_input.send_keys(Keys.RETURN)  # Press Enter key to submit the form
# Wait for a few seconds to ensure the login process is complete before performing further actions
time.sleep(5)

# Now, you can navigate to other pages or perform actions after login
# For example, you can click on a button using its XPath:
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div[1]/div[1]/div[1]/button").click()

# Don't forget to close the browser when you're done
driver.quit()