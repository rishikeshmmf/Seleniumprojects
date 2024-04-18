from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://mmfinfotech.co/intelar_web/")
dashboardbutton=driver.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div/div[1]/ul/a[1]")
#if dashboardbutton
