# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
import time

success = True
wd = WebDriver()
wd.implicitly_wait(5)


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


try:
    wd.get("https://shop.briggsandstratton.com/us/en")
    wd.find_element_by_link_text("Shop Repair Parts Now »").click()
    wd.find_element_by_link_text("No, thanks").click()
    wd.find_element_by_id("aarisearch_brands_jl").click()
    wd.find_element_by_xpath("//ul[@class='ari-caused-spacer-expand']/li[3]").click()
    wd.find_element_by_id("arisearch_txtSearch").click()
    wd.find_element_by_id("arisearch_txtSearch").clear()
    wd.find_element_by_id("arisearch_txtSearch").send_keys("209617GS")
    wd.find_element_by_id("arisearch_btnLookup").click()

    # The following div classes get in the way of our user click as seen in errors
    # and we must wait for them to unload
    # <div class="blockUI blockOverlay" ... wait; position: absolute;"></div>

    print('Testing blockUI class')
    wait = WebDriverWait(wd,5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "blockUI")))
    print('Testing blockOverlay class')
    wait = WebDriverWait(wd,2).until(EC.invisibility_of_element_located((By.CLASS_NAME, "blockOverlay")))

    # Add item 209617GS to cart
    wd.find_element_by_id('aripartsSearch_btnCart0').click()

    # Click My Cart(1) to load Shopping cart page
    wd.find_element_by_link_text("My Cart(1)").click()

    # Fill out form with test data
    print("Filling out user data")
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

    # Continue to final page
    wd.find_element_by_link_text("CONTINUE »").click()

    #Verify part numbe ris on test page
    print('Looking for Part Number on page to complete test')
    #if not ("GRAND TOTAL:" in wd.find_element_by_tag_name("html").text):
    if not ("209617GS" in wd.find_element_by_tag_name("html").text):
        success = False
        print("verifyTextPresent failed")


finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
