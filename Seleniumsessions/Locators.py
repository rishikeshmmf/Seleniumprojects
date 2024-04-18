from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Find the search input field by ID and enter "Iphone"
search = driver.find_element(By.ID, "small-searchterms")
search.send_keys("Iphone")
print("It succesfully searched input")
# Find the search button by CSS selector and click it
# click_search = driver.find_element(By.CSS_SELECTOR, "input.button-1.search-box-button")
# click_search.click()


# Wait for the search button to be clickable
#click_search = WebDriverWait(driver, 10).until(
   # EC.element_to_be_clickable((By.CSS_SELECTOR, "input.button-1.search-box-button")))
#click_search.click()
#