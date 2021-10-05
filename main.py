# Importing Necessary Libraries
import time
from selenium import webdriver

# Setting up Web Driver
driver = webdriver.Chrome(r"C:\Users\some_\chromedriver.exe")   # Address of the Driver Executable

driver.get("https://www.google.com/maps")
time.sleep(2)

# Search for Nearest Petrol Pump
def searchplace():
    Place = driver.find_element_by_class_name("tactile-searchbox-input")
    Place.send_keys("petrol pump near me")
    Submit = driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]')
    Submit.click()
  
searchplace()

# Get Direction and Routes
def directions():
    time.sleep(7)
    directions = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div[2]/button')
    directions.click()

directions()
