from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def clearCart(driver):
    driver.find_element_by_xpath('//*[@id="menuCart"]').click()
    remove = driver.find_elements_by_css_selector('[translate="REMOVE"]')
    for i in range(len(remove)-1, -1, -1):
        remove[i].click()
        time.sleep(0.5)
    driver.find_element_by_class_name("logo").click()
