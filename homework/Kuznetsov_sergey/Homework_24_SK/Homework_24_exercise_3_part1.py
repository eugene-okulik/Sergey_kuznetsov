from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, timeout=5)

driver.get('https://www.qa-practice.com/elements/select/single_select')

select_language = driver.find_element(By.XPATH, '//*[@value="1"]')
select_language.click()

submit_click = driver.find_element(By.ID, 'submit-id-submit')
submit_click.click()

result_submit = wait.until(EC.visibility_of_element_located((By.ID, 'result-text')))

assert result_submit.text == "Python"
