import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://34.141.58.52:8080/#/login'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.ID, "login")
    input1.send_keys("liza@12.com")
    time.sleep(3)

    input2 = browser.find_element(By.CSS_SELECTOR, "#password > input")
    input2.send_keys("Python#12")

    time.sleep(3)
    button = browser.find_element(By.CLASS_NAME, "p-button-label")
    button.submit()
    time.sleep(3)


    response = requests.get("http://34.141.58.52:8080/#/profile")
    r = response.status_code

    assert response.status_code == 200

    browser.save_screenshot('result2.png')

finally:
       browser.quit()

#pets = browser.find_elements(By.CSS_SELECTOR, "#password > input")

#ssert len(pets) == 3
