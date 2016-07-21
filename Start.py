# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


success = True
driver = WebDriver()

try:
    driver.set_window_size(1900, 1000)
    driver.get("https://shop.briggsandstratton.com/us/en")
    driver.find_element_by_link_text("Shop Repair Parts Now »").click()

    # This try statement is used to detect the Foresee overlay that pops up at this point in FF
    # Without this, Chrome will not continue to next step as it will error out while waiting
    try:
        wait = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.LINK_TEXT, "No, thanks")))
        driver.find_element_by_link_text("No, thanks").click()
    except Exception, e:
        print("Foresee not seen here")

    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located((By.ID, "fsrOverlay")))

    driver.find_element_by_id("aarisearch_brands_jl").click()
    wait = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='ari-caused-spacer-expand']/li[3]")))
    driver.find_element_by_xpath("//ul[@class='ari-caused-spacer-expand']/li[3]").click()
    driver.find_element_by_id("arisearch_txtSearch").click()
    driver.find_element_by_id("arisearch_txtSearch").clear()
    driver.find_element_by_id("arisearch_txtSearch").send_keys("209617GS")
    driver.find_element_by_id("arisearch_btnLookup").click()

    # The following div classes get in the way of our user click as seen in errors
    # and we must change the css with javascript to allow the button click without a sleep statement
    # <div class="blockUI blockOverlay" ... wait; position: absolute;"></div>

    try:
        hideElement = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, "blockUI")))
    except Exception, e:
        print("BlockUI not found")
    try:
        driver.execute_script("document.getElementsByClassName('blockUI blockOverlay')[0].style.height = '1px';")
    except Exception, e:
        print('blocking class not there')

    # The curtain <div> also prevents us from click so that is handled by a wait statement
    check = WebDriverWait(driver, 10).until_not(EC.presence_of_element_located((By.ID, "curtain")))

    # Add item 209617GS to cart
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.ariPartListAddToCart.ariImageOverride")))
    element = driver.find_element_by_xpath("//input[@id='aripartsSearch_btnCart0']")
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located((By.ID, "curtain")))
    driver.find_element_by_id('aripartsSearch_btnCart0').click()

    # Click My Cart(1) to load Shopping cart page
    wait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"My Cart(1)")))

    # This try statement is used to detect the Foresee overlay that pops up at this point in FF
    # Without this, Chrome will not continue to next step as it will error out while waiting
    try:
        wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "No, thanks")))
        driver.find_element_by_link_text("No, thanks").click()
    except Exception, e:
        print("Foresee not seen here")

    #View the cart contents
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

    # Continue to Checkout confirmation
    driver.find_element_by_link_text("CONTINUE »").click()

    #Verify part number is on test page
    print('Looking for Part Number on page to complete test')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"span.cart_mn")))
    assert "209617GS" in driver.page_source

finally:
    driver.quit()
    if not success:
        raise Exception("Test failed.")
