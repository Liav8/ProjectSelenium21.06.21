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
    time.sleep(1)
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

def isInBigCart(name, color, quantity, RPrice, driver):
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
                # print(td.text, name)
                if td.text == name:
                    isThere += 1

            if counter == 4:
                # print(td.find_element_by_tag_name('span').get_attribute("title"), color)
                if td.find_element_by_tag_name('span').get_attribute("title") == color:
                    isThere += 1

            if counter == 5:
                # print(td.text, quantity)
                if int(td.text) == quantity:
                    isThere += 1

            if counter == 6:
                price = td.find_element_by_tag_name('p').text
                currency = price[0]
                price = price.replace(",", "").replace("$", "")
                price = float(price)
                # print(price, RPrice)
                if price == RPrice:
                    isThere += 1
                counter = 0
        if isThere == 4:
            return True
        else:
            isThere = 0
    return False

def isInSmallCart(name, color, quantity, RPrice, driver):
    driver.find_element_by_id("shoppingCartLink").click()
    time.sleep(0.5)
    table = driver.find_element_by_xpath('//tool-tip-cart/div/table/tbody')
    rows = table.find_elements_by_tag_name('tr')
    isThere = 0
    for row in rows:
        tds = row.find_elements_by_tag_name('td')
        counter = 0
        for td in tds:
            counter += 1
            if counter == 2:
                firstIndex = td.text.find("\n")
                secondIndex = td.text.find("\n", firstIndex+1)
                if td.text[:firstIndex:] == name:
                    isThere += 1
                if int(td.text[firstIndex+1:secondIndex:].replace("QTY: ", "")) == int(quantity):
                    isThere += 1
                if td.text[secondIndex+8::] == color:
                    isThere += 1
            if counter == 3:
                if float(td.text.replace(",", "").replace("$", "")) == float(RPrice):
                     isThere += 1
                counter = 0
        if isThere == 4:
            return True
        isThere = 0
    return False

def getBigCartNames(driver):
    driver.find_element_by_id("shoppingCartLink").click()
    time.sleep(1)
    table = driver.find_element_by_xpath('//*[@id="shoppingCart"]/table/tbody')
    rows = table.find_elements_by_tag_name('tr')
    names = []
    for row in rows:
        tds = row.find_elements_by_tag_name('td')
        counter = 0
        for td in tds:
            counter += 1
            if counter == 2:
                names.append(td.text)
    return names

def getBigCartQuantity(driver):
    driver.find_element_by_id("shoppingCartLink").click()
    time.sleep(0.5)
    table = driver.find_element_by_xpath('//*[@id="shoppingCart"]/table/tbody')
    rows = table.find_elements_by_tag_name('tr')
    quantities = []
    for row in rows:
        tds = row.find_elements_by_tag_name('td')
        counter = 0
        for td in tds:
            counter += 1
            if counter == 5:
                quantities.append((td.text))
                counter = 3
    return quantities

def getBigCartPrice(driver):
    driver.find_element_by_id("shoppingCartLink").click()
    time.sleep(0.5)
    table = driver.find_element_by_xpath('//*[@id="shoppingCart"]/table/tbody')
    rows = table.find_elements_by_tag_name('tr')
    Prices = []
    for row in rows:
        tds = row.find_elements_by_tag_name('td')
        counter = 0
        for td in tds:
            counter += 1
            if counter == 6:
                price = td.find_element_by_tag_name('p').text
                price = price.replace(",", "").replace("$", "")
                price = float(price)
                Prices.append(price)
    return Prices

def updateItem(name, color, newColor, newQuan, driver):
    driver.find_element_by_id("shoppingCartLink").click()
    time.sleep(2)
    table = driver.find_element_by_xpath('//*[@id="shoppingCart"]/table/tbody')
    rows = table.find_elements_by_tag_name('tr')
    for row in rows:
        tds = row.find_elements_by_tag_name('td')
        counter = 0
        isThere = 0
        for td in tds:
            counter += 1
            if counter == 2:
                if td.text == name:
                    isThere += 1

            if counter == 4:
                if td.find_element_by_tag_name('span').get_attribute("title") == color:
                    isThere += 1

            if counter == 6 and isThere == 2:
                td.find_element_by_css_selector('[translate="EDIT"]').click()
                time.sleep(0.8)
                color = '[class=""] [title="' + newColor + '"]'
                driver.find_element_by_css_selector(color).click()
                driver.find_element_by_name("quantity").click()
                driver.find_element_by_name("quantity").send_keys(str(newQuan))
                driver.find_element_by_name("save_to_cart").click()

