from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, timeout=10)

driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')

start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
start_button.click()

hw_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4")))

assert hw_text.text == "Hello World!"
