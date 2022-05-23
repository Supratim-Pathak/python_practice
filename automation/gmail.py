from selenium import webdriver
import time

# email = input("Enter Email");
# password = input("Enter Password");

email = "surajjana230@gmail.com";
password = "suraj123*";

targatePage = webdriver.Chrome("C:\chromedriver\chromedriver")
targatePage.get('https://mail.google.com/')

mailCred = targatePage.find_element_by_css_selector('input[type ="email"]')
mailCred.send_keys(email)

time.sleep(2)
nxtBtn = targatePage.find_element_by_class_name('VfPpkd-LgbsSe')
nxtBtn.click();

time.sleep(2)

passwordInput = targatePage.find_element_by_css_selector('input[type="password"]')
passwordInput.send_keys(password)

time.sleep(2)


# =========================================================


passwordButton = targatePage.find_element_by_class_name('VfPpkd-LgbsSe')
passwordButton.click()

time.sleep(2)

for i in range(0,10):

    time.sleep(2)

    composeEmail = targatePage.find_element_by_css_selector('.T-I.T-I-KE.L3')
    composeEmail.click()

    time.sleep(2)

    destination = targatePage.find_element_by_name('to')
    destination.send_keys("supratimpathak@gmail.com")
    # destination.send_keys("abhishekmukherjee.dits@gmail.com")


    time.sleep(2)

    subject = targatePage.find_element_by_name('subjectbox')
    subject.send_keys('This is  mail subject....')

    time.sleep(4)

    body = targatePage.find_element_by_css_selector('.Am.Al.editable.LW-avf.tS-tW')
    body.send_keys('This is  mail body....')

    time.sleep(4)
    send = targatePage.find_element_by_css_selector('.T-I.J-J5-Ji.aoO.v7.T-I-atl.L3')
    send.click()

    time.sleep(4)
















