'''
Created on Feb 26, 2019

@author: Ahmad
'''

from selenium import webdriver

from lib2to3.tests.support import driver
from unittest.test import test_assertions


chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()

from selenium.webdriver.support.wait import WebDriverWait

from select import select
from selenium.webdriver.support.ui import Select


driver.get("https://stadium:goods2018!@stage.stadiumgoods.cloud")
driver.implicitly_wait(10)


#Close pop up
driver.find_element_by_xpath("//*[@version='1.1']").click()
driver.implicitly_wait(10)


#Select a category
driver.find_element_by_xpath("//div[@class='header-row-secondary']//div//a[@class='level0 has-children'][contains(text(),'Jordan')]").click()

#Select a shoe
driver.find_element_by_xpath("//a[@title='Air Jordan 1 4Lab1']//img[@itemprop='image']").click()

#Select a size
driver.find_element_by_xpath("//div[@class='product-sizes']//div[contains(@class,'product-sizes__selected')]//span[@class='product-sizes__detail']").click()
driver.implicitly_wait(10)


#Select shoe size from drop down
driver.find_element_by_xpath("//div[contains(@class,'product-sizes product-sizes-open')]//label[1]//span[1]//span[1]//span[1]").click()



#Add to cart
driver.find_element_by_xpath("//button[@title='Add to Cart']").click()


#Confirm Shopping cart
if driver.find_element_by_xpath("//div[@class='items-wrapper']//div[1]//div[2]//div[1]//span[1]//span[1]"):
    print("1 Air Jordan 1 4Lab1 Size 9.5 added")

#Click Checkout
driver.find_element_by_xpath("//button[@title='Checkout']").click()
driver.implicitly_wait(5)



#Guest checkout Radio button
driver.find_element_by_xpath("//input[@value='guest']").click()
driver.implicitly_wait(5)


#"Continue" as guest
driver.find_element_by_xpath("//button[@id='onepage-guest-register-button']").click()
driver.implicitly_wait(5)


# Shipping information
driver.find_element_by_xpath("//input[@id='shipping:email']").send_keys("Kam@kam.com")
driver.find_element_by_xpath("//input[@id='shipping:firstname']").send_keys("Kam")
driver.find_element_by_xpath("//input[@id='shipping:lastname']").send_keys("Ahmad")
driver.find_element_by_xpath("//input[@id='shipping:street1']").send_keys("1 times sq, ny")

driver.implicitly_wait(15)

driver.find_element_by_xpath("//input[@id='shipping:street2']").send_keys("5B")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//input[@id='shipping:city']").send_keys("New York")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//select[@id='shipping:region_id']").send_keys("New York")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//input[@id='shipping:postcode']").send_keys("11355")
driver.find_element_by_xpath("//input[@id='shipping:telephone']").send_keys("555-555-5555")
driver.find_element_by_xpath("//div[@id='shipping-buttons-container']//button[@title='Save and Continue']").click()
driver.implicitly_wait(5)



#Shipping options
driver.find_element_by_xpath("//div[@id='shipping-method-buttons-container']//button[@title='Save and Continue']").click()
driver.implicitly_wait(15)



#Payment Method
driver.find_element_by_id("p_method_creditcard").click()
driver.find_element_by_xpath("//input[@id='creditcard_cc_number']").send_keys("4242424242424242")
driver.find_element_by_xpath("//select[@id='creditcard_expiration']").click()

driver.implicitly_wait(15)

dropdown=Select(driver.find_element_by_xpath("//select[@id='creditcard_expiration']"))
dropdown.select_by_value("3")

driver.implicitly_wait(5)

driver.find_element_by_xpath("//select[@id='creditcard_expiration_yr']").click()

driver.implicitly_wait(15)

dropdown2=Select(driver.find_element_by_xpath("//select[@id='creditcard_expiration_yr']"))
dropdown2.select_by_value("2020")

driver.implicitly_wait(5)

driver.find_element_by_xpath("//input[@id='creditcard_cc_cid']").click()
driver.find_element_by_xpath("//input[@id='creditcard_cc_cid']").send_keys("321")

driver.implicitly_wait(5)

driver.find_element_by_xpath("//input[@placeholder='Billing Zip']").click()
driver.find_element_by_xpath("//input[@placeholder='Billing Zip']").send_keys("10011")

driver.find_element_by_xpath("//li[@class='section allow active']//button[@type='button']").click()
driver.implicitly_wait(20)

#Confirmation page
if driver.find_element_by_xpath("//p[@class='confirm-txt']"):
    print("Order Confirmed")





