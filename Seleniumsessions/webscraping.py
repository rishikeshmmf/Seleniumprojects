import pandas as pd
from selenium import webdriver # allow launching browser
from selenium.webdriver.common.by import By # allow search with parameters
from selenium.webdriver.support.ui import WebDriverWait # allow waiting for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situation

driver_option = webdriver.ChromeOptions()
browser=webdriver.Chrome()
#browser = create_webdriver()
browser.get("https://github.com/collections/machine-learning")
projects = browser.find_elements(By.XPATH,value="//h1[@class='h3 lh-condensed']")
project_list = {}
for proj in projects:
 proj_name = proj.text # Project name
 proj_urls = proj.find_elements(By.XPATH, "(//a)[1]")  # Finding all matching elements
 proj_url = proj_urls[0].get_attribute('href')  # Getting the href attribute of th# Project URL
 project_list[proj_name] = proj_url
 #print(proj_url)
 project_df = pd.DataFrame.from_dict(project_list, orient='index')
 #print(project_df)
 project_df['project_name'] = project_df.index
 project_df.columns = ['project_url', 'project_name']
 project_df = project_df.reset_index(drop=True)
 project_df.to_csv('project_list.csv')
browser.get("url_of_your_page")

# Find and click the download link
download_link = browser.find_element(By.XPATH, "//a[contains(@href,'project_list.csv')]")
download_link.click()
