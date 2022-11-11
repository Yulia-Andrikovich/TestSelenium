
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://34.141.58.52:8080/#/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, "//div[@id='pv_id_2']/div/span").click()
    time.sleep(1)
    browser.find_element(By.ID, "pv_id_2_0").click()
    time.sleep(1)

    browser.save_screenshot('result_drop.png')

finally:

    browser.quit()

