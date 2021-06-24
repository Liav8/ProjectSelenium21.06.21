from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from SeleniumProject.login import login
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from CleanCart import clearCart
import time
from openpyxl import *



workbook = load_workbook(filename="DataTests.xlsx")
sheet = workbook.active
driver = webdriver.Chrome(executable_path=r"D:\QA Course\Selenium\chromedriver.exe")
wait = WebDriverWait(driver, 20)
action_chains = ActionChains(driver)
driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()
driver.implicitly_wait(25)
wait.until(EC.visibility_of_element_located((By.ID, "menuUser")))
time.sleep(5)
login(driver)

# for i in range(20):
#     action_chains.move_to_element(driver.find_element_by_id('menuCart')).perform()
#     time.sleep(2)

clearCart(driver)
action_chains.move_to_element(driver.find_element_by_id('menuCart')).perform()

time.sleep(2)
driver.find_element_by_id("see_offer_btn").click()
time.sleep(3)
plus = driver.find_element_by_class_name("plus")
plus.click()
plus.click()
driver.find_element_by_name("save_to_cart").click()
driver.find_element_by_xpath("/html/body/div[3]/nav/a[2]").click()
driver.find_element_by_id("5").click()
driver.find_element_by_name("save_to_cart").click()
driver.back()
driver.find_element_by_id("1").click()
driver.find_element_by_name("save_to_cart").click()
time.sleep(1)
total = int(driver.find_element_by_css_selector('[ng-show="welcome" ] [class="cart ng-binding"]').text)
time.sleep(1.5)
requiredTotal = 5#----------------------------------------------------------------------------------------------change this to get the requirment from the xl
if total == requiredTotal:
    driver.find_element_by_id("shoppingCartLink").click()
    # driver.find_element_by_id("checkOutButton").click()

# 2 2 2 2 2 2 2                                  vardi all of 2 is on build right now so ignore it

# table = driver.find_element_by_xpath('//*[@id="shoppingCart"]/table/tbody')
# rows = table.find_elements_by_tag_name('tr')
# # name = HP PAVILION 15T TOUCH LAPTOP#----------------------------------------------------------------------------------------------change this to get the requirment from the xl
# # color = GRAY#----------------------------------------------------------------------------------------------change this to get the requirment from the xl
# # quantity = 1#----------------------------------------------------------------------------------------------change this to get the requirment from the xl
# # reqPrice = 519.99#----------------------------------------------------------------------------------------------change this to get the requirment from the xl
# counter = 0
# for row in rows:
#     tds = row.find_elements_by_tag_name('td')
#     for td in tds:
#         counter += 1
#         if counter == 2:
#             name = "HP PAVILION 15T TOUCH LAPTOP"#-----change this to get the requirment from the xl
#             # return name == td.text
#
#         if counter == 4:
#             color = "GRAY"  # ----------------------------------------------------------------------------------------------change this to get the requirment from the xl
#             # return color == td.find_element_by_tag_name('span').get_attribute("title")
#             print(td.find_element_by_tag_name('span').get_attribute("title"))
#         if counter == 5:
#             quantity = 1#----------------------------------------------------------------------------------------------change this to get the requirment from the xl
#             # return quantity == int(td.text)
#         if counter == 6:
#             price = td.find_element_by_tag_name('p').text
#             currency = price[0]
#             price = price.replace(",", "").replace("$", "")
#             price = float(price)
#             reqPrice = 519.99  # ----------------------------------------------------------------------------------------------change this to get the requirment from the xl
#             # return reqPrice == price
#             counter = 0



# 5 5 5 5 5 5 5 5 5 5 5 5
table = driver.find_element_by_xpath('//*[@id="shoppingCart"]/table/tbody')
rows = table.find_elements_by_tag_name('tr')
# name = HP PAVILION 15T TOUCH LAPTOP#----------------------------------------------------------------------------------------------change this to get the requirment from the xl
# color = GRAY#----------------------------------------------------------------------------------------------change this to get the requirment from the xl
# quantity = 1#----------------------------------------------------------------------------------------------change this to get the requirment from the xl
# reqPrice = 519.99#----------------------------------------------------------------------------------------------change this to get the requirment from the xl
counter = 0
RowSheet = 2
CulSheet = 2
print(sheet.cell(row=RowSheet, column=CulSheet).value)
for row in rows:
    tds = row.find_elements_by_tag_name('td')
    for td in tds:
        counter += 1
        if counter == 2:
            if td.text == sheet.cell(row=RowSheet, column=CulSheet).value:
                print("True")
            else:
                print("False")
            # name = "HP PAVILION 15T TOUCH LAPTOP"#-----change this to get the requirment from the xl
            # return name == td.text
            CulSheet+=1

        if counter == 4:
            if td.find_element_by_tag_name('span').get_attribute("title") == sheet.cell(row=RowSheet, column=CulSheet).value:
                print("True")
            else:
                print("False")
            # color = "GRAY"  # ----------------------------------------------------------------------------------------------change this to get the requirment from the xl
            # return color == td.find_element_by_tag_name('span').get_attribute("title")
            # print(td.find_element_by_tag_name('span').get_attribute("title"))
            CulSheet+=1

        if counter == 5:
            if int(td.text) == sheet.cell(row=RowSheet, column=CulSheet).value:
                print("True")
            else:
                print("False")
            # quantity = 1#----------------------------------------------------------------------------------------------change this to get the requirment from the xl
            # return quantity == int(td.text)
            CulSheet+=1

        if counter == 6:

            price = td.find_element_by_tag_name('p').text
            currency = price[0]
            price = price.replace(",", "").replace("$", "")
            price = float(price)
            if price == sheet.cell(row=RowSheet, column=CulSheet).value:
                print("True")
            else:
                print("False")
            # reqPrice = 519.99  # ----------------------------------------------------------------------------------------------change this to get the requirment from the xl
            # return reqPrice == price
            counter = 0
            CulSheet = 2
            RowSheet += 1



# name = HP PAVILION 15T TOUCH LAPTOP#----------------------------------------------------------------------------------------------change this to get the requirment from the xl
# color#----------------------------------------------------------------------------------------------change this to get the requirment from the xl
# quantity#----------------------------------------------------------------------------------------------change this to get the requirment from the xl
# price#----------------------------------------------------------------------------------------------change this to get the requirment from the xl








time.sleep(8)
driver.close()




# class inCart:
#     def __init__(self, driver):
#         self.driver

