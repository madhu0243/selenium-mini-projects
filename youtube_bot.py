from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com")

search = driver.find_element(By.NAME, "search_query")
search.send_keys("Python Selenium tutorial")
search.submit()

time.sleep(5)

driver.quit()