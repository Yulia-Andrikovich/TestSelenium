import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://automationpractice.com/index.php'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
    button.click()
    input1 = browser.find_element(By.XPATH, '//*[@id="email_create"]')
    input1.send_keys("qwert@123.com")
    button1 = browser.find_element(By.XPATH, '//*[@id="SubmitCreate"]')
    button1.submit()

    time.sleep(5)


    browser.save_screenshot('result1.png')

finally:
       browser.quit()
