from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/alerts")

driver.find_element_by_id("promtButton").click()
driver.switch_to.alert.send_keys("saya sedang makan")
driver.switch_to.alert.accept()