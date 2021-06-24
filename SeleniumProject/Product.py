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
    SName = driver.find_element_by_name("search icon").click()
    driver
    SName.send_keys(name)
    #press enter
    #get to the product
    #press the selected color buttin
    #add quantities as requierd
    #pres
    driver.find_element_by_name("save_to_cart").click()
    driver.back()