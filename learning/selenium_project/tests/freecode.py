from selenium import webdriver
import os


os.environ['PATH'] += r"C:\Users\Matthew\Documents\selenium_project\vendor"
driver = webdriver.Chrome()
driver.get("https://www.thecalculatorsite.com/")
driver.implicitly_wait(3)
my_element = driver.find_element_by_id('tcsSearch')
my_element.click()
