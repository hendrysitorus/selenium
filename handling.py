from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com/alerts")
time.sleep(2)

driver.find_element_by_id("confirmButton").click()
time.sleep(2)
driver.switch_to.alert.dismiss()