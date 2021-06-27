from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def login(driver):
    wait = WebDriverWait(driver, 10)
    # wait.until(EC.element_to_be_clickable((By.ID, "menuUser")))
    login_page = driver.find_element_by_id("menuUser")
    login_page.click()
    # wait.until(EC.element_to_be_clickable((By.ID, "username")))
    time.sleep(1.5)
    driver.find_element_by_name("username").send_keys("Sa1234")
    driver.find_element_by_name("password").send_keys("Sa1234")
    driver.find_element_by_id("sign_in_btnundefined").click()

def clearCart(driver):
    driver.find_element_by_xpath('//*[@id="menuCart"]').click()
    remove = driver.find_elements_by_css_selector('[class="fixedTableEdgeCompatibility"] [translate="REMOVE"]')
    if remove != []:
        for i in range(len(remove)-1, -1, -1):
            remove[i].click()
            time.sleep(0.5)
    driver.find_element_by_css_selector('[class="logo"] [href="#/"]').click()

def getTotalSmallCart(driver):
    # total = driver.find_element_by_css_selector('[class="emptyCart"] [class="roboto-regular"]').text
    # total = total.replace(",", "").replace("$", "")
    return int((driver.find_element_by_css_selector('[class="emptyCart"] [class="roboto-regular"]').text).replace("(", "").replace(")", ""))



