from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def login(driver):
    wait = WebDriverWait(driver, 3)
    # wait.until(EC.visibility_of_element_located((By.ID, "menuUser")))
    login_page = driver.find_element_by_id("menuUser")
    login_page.click()
    time.sleep(1.5)
    userName = driver.find_element_by_name("username")
    userName.click()
    userName.send_keys("Sa1234")
    password = driver.find_element_by_name("password")
    password.click()
    password.send_keys("Sa1234")
    loginButton = driver.find_element_by_id("sign_in_btnundefined")
    loginButton.click()



