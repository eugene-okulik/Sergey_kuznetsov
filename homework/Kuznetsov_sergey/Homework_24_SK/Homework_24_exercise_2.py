from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--window-size=400,1080')
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, timeout=5)
driver.get("https://demoqa.com/automation-practice-form")

first_name_element = driver.find_element(By.XPATH, '//input[@id="firstName"]')
first_name_element.send_keys("Sergey")

second_name_element = driver.find_element(By.XPATH, '//input[@id="lastName"]')
second_name_element.send_keys("Kuznetsov")

email_element = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
email_element.send_keys("test@testov.com")

male_gender_radio_button = driver.find_element(By.XPATH, '//*[@for="gender-radio-1"]')
male_gender_radio_button.click()

mobile_element = driver.find_element(By.XPATH, '//input[@id="userNumber"]')
mobile_element.send_keys("8005553535")

wait.until(EC.element_to_be_clickable((By.ID, "dateOfBirthInput"))).click()

wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "react-datepicker")))

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".react-datepicker__month-select"))).click()

wait.until(EC.element_to_be_clickable((By.XPATH, '//option[@value="7"]'))).click()

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.react-datepicker__year-select'))).click()

wait.until(EC.element_to_be_clickable((By.XPATH, '//option[@value="1999"]'))).click()

wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//div[contains(@class, "react-datepicker__day") and text()="31"]'))).click()

sub_element = driver.find_element(By.ID, "subjectsInput")
sub_element.send_keys("Biology")
sub_element.send_keys(Keys.ENTER)

wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='hobbies-checkbox-1']"))).click()

curr_address_element = driver.find_element(By.ID, "currentAddress")
curr_address_element.send_keys("Hello world for all")

curr_address_element = driver.find_element(By.ID, "state")
curr_address_element.click()
select_state_element = driver.find_element(By.ID, "react-select-3-option-0")
select_state_element.click()

curr_city_element = driver.find_element(By.ID, "city")
curr_city_element.click()
select_city_element = driver.find_element(By.ID, "react-select-4-option-0")
select_city_element.click()

submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

result = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-content")))
rows = result.find_elements(By.CSS_SELECTOR, 'table tbody tr')

result_data = {}

for row in rows:
    key = row.find_element(By.TAG_NAME, "td").text
    value = row.find_elements(By.TAG_NAME, "td")[1].text
    result_data[key] = value

for k, v in result_data.items():
    print(f"{k}: {v}")
