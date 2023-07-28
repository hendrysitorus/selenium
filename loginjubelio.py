from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://app.jubelio.com/login")

element = driver.find_element(By.NAME, "email")
element.clear()
element.send_keys("qa.rakamin.jubelio@gmail.com")

element_pass = driver.find_element(By.NAME, "password")
element_pass.clear()
element_pass.send_keys("Jubelio123!")

# Use 'By.CSS_SELECTOR' with 'find_element' to click the element
driver.find_element(By.CSS_SELECTOR, "span.ladda-label").click()

# Wait for the login to complete
driver.implicitly_wait(10)

try:
    # Verify if the login is successful by checking for some element on the dashboard page
    driver.find_element(By.XPATH, "//span[contains(text(),'Dashboard')]")

    # If login is successful, print a success message and quit the WebDriver
    print("Login successful!")
    driver.quit()

except Exception as e:
    # If there is an exception, print an error message and quit the WebDriver
    print("Error during login:", str(e))
    driver.quit()
