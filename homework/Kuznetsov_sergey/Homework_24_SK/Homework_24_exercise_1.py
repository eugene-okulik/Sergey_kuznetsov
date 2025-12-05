from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
input_text = "Hello"
wait = WebDriverWait(driver, timeout=10)
driver.get("https://www.qa-practice.com/elements/input/simple")
search_input1 = driver.find_element(By.NAME, 'text_string')
search_input1.send_keys(input_text)
search_input1.send_keys(Keys.ENTER)
result = wait.until(EC.visibility_of_element_located((By.ID, 'result-text')))
print(result.text)
assert result.text == input_text
