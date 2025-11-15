from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_careers_page():
    driver = webdriver.Chrome()
    driver.get("https://useinsider.com/")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Company"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Careers"))
    ).click()

    assert "Careers" in driver.title
    driver.quit()
