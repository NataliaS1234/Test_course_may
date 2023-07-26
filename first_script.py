import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a Service object with the chromedriver path
service = Service('/opt/homebrew/bin/chromedriver')

# Start the chromedriver service
service.start()

# Initialize the webdriver with the service
driver = webdriver.Chrome(service=service)

# Implicitly wait for 10 seconds for elements to be available
driver.implicitly_wait(10)

# Open the website
driver.get("https://stepik.org/lesson/25969/step/12")
try:
    # Explicitly wait for the textarea element to be visible
    wait = WebDriverWait(driver, 20)
    textarea = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".textarea")))

    # Enter text in the textarea
    textarea.send_keys("get()")

    # Find and click the submit button
    submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
    submit_button.click()

    # Wait for the result message
    result_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    print(result_message.text)

finally:
    # Close the browser
    driver.quit()

    # Stop the chromedriver service
    service.stop()
