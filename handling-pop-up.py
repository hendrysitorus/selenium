from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://tees.co.id/")
print("success")

try : 
    webdriver(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, '/html/body/div[1]')))
    print("pop up berhasil tampil")
    driver.find_element_by_class_name("btn-modal-close").click()
    print("pop up ")

except TimeoutException :
    print("pop up muncul bro")
    pass





