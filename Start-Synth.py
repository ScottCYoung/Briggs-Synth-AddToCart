# -*- coding: utf-8 -*-
#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
import time

success = True
#driver = WebDriver()
#driver.implicitly_wait(40)


def is_alert_present(driver):
    try:
        driver.switch_to_alert().text
        return True
    except:
        return False


try:
    driver.set_window_size(1900, 1000)
    driver.get("https://shop.briggsandstratton.com/us/en")
    driver.find_element_by_link_text("Shop Repair Parts Now »").click()
    wait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, "No, thanks")))
    driver.find_element_by_link_text("No, thanks").click()
    driver.find_element_by_id("aarisearch_brands_jl").click()
    wait = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='ari-caused-spacer-expand']/li[3]")))
    print (wait)
    driver.find_element_by_xpath("//ul[@class='ari-caused-spacer-expand']/li[3]").click()
    driver.find_element_by_id("arisearch_txtSearch").click()
    driver.find_element_by_id("arisearch_txtSearch").clear()
    driver.find_element_by_id("arisearch_txtSearch").send_keys("209617GS")
    driver.find_element_by_id("arisearch_btnLookup").click()

    # The following div classes get in the way of our user click as seen in errors
    # and we must wait for them to unload
    # <div class="blockUI blockOverlay" ... wait; position: absolute;"></div>

    print('Testing blockUI class')
    wait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, "blockUI")))
    print('Testing blockOverlay class')
    wait = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME, "blockOverlay")))

    # Add item 209617GS to cart
    ActionChains(driver).move_to_element((By.ID,"aripartsSearch_btnCart0"))
    wait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"aripartsSearch_btnCart0")))
    print(wait)
    driver.find_element_by_id('aripartsSearch_btnCart0').click()

    # Click My Cart(1) to load Shopping cart page
    wait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"My Cart(1)")))
    ActionChains(driver).move_to_element((By.LINK_TEXT,"My Cart(1)"))
    driver.find_element_by_link_text("My Cart(1)").click()

    # Fill out form with test data
    print("Filling out user data")
    driver.find_element_by_xpath("//a[@id='content_2_ButtonCheckout']//span[.='Checkout']").click()

    driver.find_element_by_id("content_2_TextBoxBTFirstName").click()
    driver.find_element_by_id("content_2_TextBoxBTFirstName").clear()
    driver.find_element_by_id("content_2_TextBoxBTFirstName").send_keys("User")
    driver.find_element_by_id("content_2_TextBoxBTLastName").click()
    driver.find_element_by_id("content_2_TextBoxBTLastName").clear()
    driver.find_element_by_id("content_2_TextBoxBTLastName").send_keys("Test")
    driver.find_element_by_id("content_2_TextBoxBTAddress1").click()
    driver.find_element_by_id("content_2_TextBoxBTAddress1").clear()
    driver.find_element_by_id("content_2_TextBoxBTAddress1").send_keys("1600 Pennsylvania Ave NW")
    driver.find_element_by_id("content_2_TextBoxBTCity").click()
    driver.find_element_by_id("content_2_TextBoxBTCity").clear()
    driver.find_element_by_id("content_2_TextBoxBTCity").send_keys("Washington")
    if not driver.find_element_by_xpath("//select[@id='content_2_DropDownListBTState']//option[8]").is_selected():
        driver.find_element_by_xpath("//select[@id='content_2_DropDownListBTState']//option[8]").click()
    driver.find_element_by_id("content_2_TextBoxBTZip").click()
    driver.find_element_by_id("content_2_TextBoxBTZip").clear()
    driver.find_element_by_id("content_2_TextBoxBTZip").send_keys("20500-0003")
    driver.find_element_by_id("content_2_TextBoxBTPhoneArea").click()
    driver.find_element_by_id("content_2_TextBoxBTPhoneArea").clear()
    driver.find_element_by_id("content_2_TextBoxBTPhoneArea").send_keys("123")
    driver.find_element_by_id("content_2_TextBoxBTPhone1").click()
    driver.find_element_by_id("content_2_TextBoxBTPhone1").clear()
    driver.find_element_by_id("content_2_TextBoxBTPhone1").send_keys("123")
    driver.find_element_by_id("content_2_TextBoxBTPhone2").click()
    driver.find_element_by_id("content_2_TextBoxBTPhone2").clear()
    driver.find_element_by_id("content_2_TextBoxBTPhone2").send_keys("1234")
    driver.find_element_by_id("content_2_txtEmail2").click()
    driver.find_element_by_id("content_2_txtEmail2").clear()
    driver.find_element_by_id("content_2_txtEmail2").send_keys("Test@basco.com")

    # Continue to final page
    driver.find_element_by_link_text("CONTINUE »").click()

    #Verify part numbe ris on test page
    print('Looking for Part Number on page to complete test')
    #if not ("GRAND TOTAL:" in driver.find_element_by_tag_name("html").text):
    assert "209617GS" in driver.page_source
    #if not ("209617GS" in driver.find_element_by_tag_name("html").text):
    #    success = False
    #    print("verifyTextPresent failed")


finally:
    driver.quit()
    if not success:
        raise Exception("Test failed.")