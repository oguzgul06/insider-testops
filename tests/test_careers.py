""" from selenium import webdriver
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
 """


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_careers_page():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://useinsider.com/")

    company_link = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Company"))
    )
    driver.execute_script("arguments[0].click();", company_link)

    careers_link = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Careers"))
    )
    driver.execute_script("arguments[0].click();", careers_link)

    assert "Careers" in driver.title
    driver.quit()
