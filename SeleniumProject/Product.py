from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from SeleniumProject.usableFunctionalities import login
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from CleanCart import *
import time
from openpyxl import *


def addProduct(name, color, quantity, driver):
    time.sleep(1)
    driver.find_element_by_id("menuSearch").click()
    driver.find_element_by_id("autoComplete").send_keys(name)
    time.sleep(1)
    driver.find_element_by_id("menuSearch").click()
    time.sleep(1)
    driver.find_element_by_css_selector('[class="imgProduct"]').click()
    color = '[class=""] [title="' + color + '"]'#[id="productProperties"] [title="GRAY"]        [class=""] [title="GRAY"]
    driver.find_element_by_css_selector(color).click()
    # print(type(colors), colors)
    # for i in colors:
    #     print(i)
    #     i.click()
    driver.find_element_by_name("quantity").click()
    driver.find_element_by_name("quantity").send_keys(str(quantity))
    driver.find_element_by_name("save_to_cart").click()
    driver.find_element_by_css_selector('[class="logo"] [href="#/"]').click()

def isInCart(name, color, quantity, RPrice, driver):
    driver.find_element_by_id("shoppingCartLink").click()
    time.sleep(2)
    table = driver.find_element_by_xpath('//*[@id="shoppingCart"]/table/tbody')
    rows = table.find_elements_by_tag_name('tr')
    counter = 0
    isThere = 0
    for row in rows:
        tds = row.find_elements_by_tag_name('td')
        counter = 0
        for td in tds:
            counter += 1
            if counter == 2:
                print(td.text, name)
                if td.text == name:
                    isThere += 1

            if counter == 4:
                print(td.find_element_by_tag_name('span').get_attribute("title"), color)
                if td.find_element_by_tag_name('span').get_attribute("title") == color:
                    isThere += 1

            if counter == 5:
                print(td.text, quantity)
                if int(td.text) == quantity:
                    isThere += 1

            if counter == 6:
                price = td.find_element_by_tag_name('p').text
                currency = price[0]
                price = price.replace(",", "").replace("$", "")
                price = float(price)
                print(price, RPrice)
                if price == RPrice:
                    isThere += 1
                counter = 0
        if isThere == 4:
            return True
        else:
            isThere = 0
    return False
