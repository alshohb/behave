from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the website
driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Wait for the page to finish loading
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Measure the page load time
navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
loadTime = responseStart - navigationStart

# Assert that the load time is less than 3 seconds
assert loadTime < 3000, f"Page load time was {loadTime} ms, which is too slow"

# Close the browser
driver.quit()
