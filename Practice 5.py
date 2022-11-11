import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

time.sleep(5)

search_box = driver.find_element(By.TAG_NAME, "input")
search_box.send_keys('Swagger')
search_box.submit()

time.sleep(5)

driver.save_screenshot('result.png')

driver.quit()

#  button2 = browser.find_element(By.NAME, 'id_gender')
#     button2.click()