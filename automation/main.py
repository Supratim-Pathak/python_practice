from selenium import webdriver
import time

google = input("Enter Keyword");

targatePage = webdriver.Chrome("C:\chromedriver\chromedriver")
targatePage.get('https://www.google.com/')

time.sleep(2)

searchInput = targatePage.find_element_by_name('q')
searchInput.send_keys(google)

time.sleep(2)

subButton = targatePage.find_element_by_css_selector('input[type="submit"]')
subButton.click()
