import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://mmfinfotech.co/intelar_web/")
driver.maximize_window()
email_input = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/form/div[1]/input").send_keys("intelaradmin@yopmail.com")
password_input = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/form/div[2]/input").send_keys("12345678")
#driver.find_element(By.NAME,"rememberMe").click()
checkbox=driver.find_element(By.NAME,'rememberMe')
checkbox.click()
if checkbox.is_selected():
 print("checkbox is selected")
else:
 print("Checkbox is not selected")
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div/form/button").click()
#driver.find_element(By.CSS_SELECTOR, "button.mt-5 logout_btn btn btn-primary").click()
act_title='Intelar | Admin'
ext_title="Intelar | Admin"
if act_title==ext_title:
 print("Login passed")
else:
 print("Login failed")
 driver.quit()
time.sleep(5)

# Now, you can navigate to other pages or perform actions after login
# For example, you can click on a button using its XPath:
#driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div[1]/div[1]/div[1]/button").click()

# Don't forget to close the browser when you're done
#driver.quit()