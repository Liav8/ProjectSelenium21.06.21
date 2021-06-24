from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from SeleniumProject.usableFunctionalities import login
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from CleanCart import clearCart
import time
from openpyxl import *


def addProduct(name, color, quantity, driver):
    driver.find_element_by_id("menuSearch").click()
    driver.find_element_by_id("autoComplete").send_keys(name)
    time.sleep(1)
    driver.find_element_by_id("menuSearch").click()
    driver.find_element_by_css_selector('[class="imgProduct"]').click()
    time.sleep(1)
    color = '[ng-show="firstImageToShow"]>[title="' + color + '"]'
    driver.find_element_by_css_selector(color).click()
    driver.find_element_by_name("quantity").click()
    driver.find_element_by_name("quantity").send_keys(str(quantity))
    driver.find_element_by_name("save_to_cart").click()
    driver.find_element_by_css_selector('[class="logo"] [href="#/"]').click()
