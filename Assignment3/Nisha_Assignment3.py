from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the github.com homepage
driver.get("https://github.com/")
time.sleep(5)

Input_button = driver.find_element("xpath","/html/body/div[1]/div[1]/header/div/div[2]/div/div/qbsearch-input/div[1]/button")
Input_button.click()
time.sleep(3)

search_bar = driver.find_element("id","query-builder-test")
search_bar.send_keys("Nishaben_8913052")

search_bar.send_keys(Keys.RETURN)
time.sleep(3)

Repo_link = driver.find_element("xpath","/html/body/div[1]/div[4]/main/react-app/div/div/div[1]/div/div/main/div[2]/div/div[1]/div[4]/div/div/div/div/div[1]/h3/div/div[2]/a")
Repo_link.click()
time.sleep(5)

# Closing the webdriver
driver.close()