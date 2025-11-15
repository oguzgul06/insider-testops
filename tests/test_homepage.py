""" from selenium import webdriver
from selenium.webdriver.common.by import By

def test_homepage_loads():
    driver = webdriver.Chrome()
    driver.get("https://useinsider.com/")
    assert "Insider" in driver.title
    driver.quit()
 """

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_homepage_loads():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://useinsider.com/")
    assert "Insider" in driver.title
    driver.quit()
