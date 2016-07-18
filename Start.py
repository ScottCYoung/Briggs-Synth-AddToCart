# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
import time

success = True
wd = WebDriver()
wd.implicitly_wait(15)

def wait_until_visible_then_click(element):
    element = WebDriverWait(wd,5,poll_frequency=.2).until(
        EC.visibility_of(element))
    element.click()

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    #wd.get("https://shop.briggsandstratton.com/us/en/repair-parts#/s/GEN//209617GS/1")
    wd.get("https://shop.briggsandstratton.com/us/en")
    wd.find_element_by_link_text("Shop Repair Parts Now »").click()
    wd.find_element_by_link_text("No, thanks").click()
    wd.find_element_by_id("aarisearch_brands_jl").click()
    wd.find_element_by_xpath("//ul[@class='ari-caused-spacer-expand']/li[3]").click()
    wd.find_element_by_id("arisearch_txtSearch").click()
    wd.find_element_by_id("arisearch_txtSearch").clear()
    wd.find_element_by_id("arisearch_txtSearch").send_keys("209617GS")
    wd.find_element_by_id("arisearch_btnLookup").click()
    #wd.find_element_by_id("aripartsSearch_btnCart0").click()
    time.sleep(5)

    wd.find_element_by_id('aripartsSearch_btnCart0').click()
    time.sleep(5)
    if not ("My Cart(1)" in wd.find_element_by_tag_name("html").text):
        success = False
        print("verifyTextPresent failed")
    wd.find_element_by_link_text("My Cart(1)").click()

    #Fill out form
    print("clicking checkout")
    wd.find_element_by_xpath("//a[@id='content_2_ButtonCheckout']//span[.='Checkout']").click()

    wd.find_element_by_id("content_2_TextBoxBTFirstName").click()
    wd.find_element_by_id("content_2_TextBoxBTFirstName").clear()
    wd.find_element_by_id("content_2_TextBoxBTFirstName").send_keys("User")
    wd.find_element_by_id("content_2_TextBoxBTLastName").click()
    wd.find_element_by_id("content_2_TextBoxBTLastName").clear()
    wd.find_element_by_id("content_2_TextBoxBTLastName").send_keys("Test")
    wd.find_element_by_id("content_2_TextBoxBTAddress1").click()
    wd.find_element_by_id("content_2_TextBoxBTAddress1").clear()
    wd.find_element_by_id("content_2_TextBoxBTAddress1").send_keys("1600 Pennsylvania Ave NW")
    wd.find_element_by_id("content_2_TextBoxBTCity").click()
    wd.find_element_by_id("content_2_TextBoxBTCity").clear()
    wd.find_element_by_id("content_2_TextBoxBTCity").send_keys("Washington")
    if not wd.find_element_by_xpath("//select[@id='content_2_DropDownListBTState']//option[8]").is_selected():
        wd.find_element_by_xpath("//select[@id='content_2_DropDownListBTState']//option[8]").click()
    wd.find_element_by_id("content_2_TextBoxBTZip").click()
    wd.find_element_by_id("content_2_TextBoxBTZip").clear()
    wd.find_element_by_id("content_2_TextBoxBTZip").send_keys("20500-0003")
    wd.find_element_by_id("content_2_TextBoxBTPhoneArea").click()
    wd.find_element_by_id("content_2_TextBoxBTPhoneArea").clear()
    wd.find_element_by_id("content_2_TextBoxBTPhoneArea").send_keys("123")
    wd.find_element_by_id("content_2_TextBoxBTPhone1").click()
    wd.find_element_by_id("content_2_TextBoxBTPhone1").clear()
    wd.find_element_by_id("content_2_TextBoxBTPhone1").send_keys("123")
    wd.find_element_by_id("content_2_TextBoxBTPhone2").click()
    wd.find_element_by_id("content_2_TextBoxBTPhone2").clear()
    wd.find_element_by_id("content_2_TextBoxBTPhone2").send_keys("1234")
    wd.find_element_by_id("content_2_txtEmail2").click()
    wd.find_element_by_id("content_2_txtEmail2").clear()
    wd.find_element_by_id("content_2_txtEmail2").send_keys("Test@basco.com")

    #time.sleep(15)
    wd.find_element_by_link_text("CONTINUE »").click()
    #time.sleep(15)
    #if not wd.find_element_by_id("content_2_CheckBoxUseSuggested").is_selected():
    #    wd.find_element_by_id("content_2_CheckBoxUseSuggested").click()
    #wd.find_element_by_link_text("CONTINUE »").click()
    if not ("GRAND TOTAL:" in wd.find_element_by_tag_name("html").text):
        success = False
        print("verifyTextPresent failed")

    #wd.find_element_by_id("aripartsSearch_btnCart0").click()


finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")