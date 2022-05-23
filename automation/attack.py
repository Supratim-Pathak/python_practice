from selenium import webdriver
import time

browser = webdriver.Chrome('C:\chromedriver\chromedriver')
browser.get("https://www.innovaindia.com/contactus.php")

m = browser.find_elements_by_xpath("span[@class='hm_requires_star']")

for i in m:

    print(m)