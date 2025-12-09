from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_recycle_bin(driver):
    driver.get("http://testshop.qa-practice.com/")
    wait = WebDriverWait(driver, 10)
    new_page = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Customizable Desk")))
    ActionChains(driver).key_down(Keys.COMMAND).click(new_page).key_up(Keys.COMMAND).perform()
    driver.switch_to.window(driver.window_handles[-1])
    wait.until(EC.element_to_be_clickable((By.ID, 'add_to_cart'))).click()
    pop_up = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="modal_5"]')))
    pop_up.find_element(By.XPATH, '//*[@class="btn btn-secondary"]').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@role="alert"]')))
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="eCommerce cart"]'))).click()
    driver.switch_to.window(driver.window_handles[-1])
    result = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Customizable Desk (Steel, White)')))
    assert result.text == 'Customizable Desk (Steel, White)'


def test_move_location(driver):
    driver.get('http://testshop.qa-practice.com/')
    wait = WebDriverWait(driver, 10)
    card = driver.find_element(By.XPATH, '//*[@alt="Customizable Desk"]')
    rec_bin = driver.find_element(By.XPATH, '//*[@class="btn btn-primary a-submit"]')
    ActionChains(driver).move_to_element(card).click(rec_bin).perform()
    pop_up = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="modal-content"]')))
    result = pop_up.find_element(By.XPATH, '//*[@class="product-name product_display_name"]')
    assert result.text == '[FURN_0096] Customizable Desk (Steel, White)'
