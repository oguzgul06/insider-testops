from selenium import webdriver
from selenium.webdriver.common.by import By

def test_homepage_loads():
    driver = webdriver.Chrome()
    driver.get("https://useinsider.com/")
    assert "Insider" in driver.title
    driver.quit()
