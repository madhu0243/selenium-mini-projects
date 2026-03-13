from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

search = driver.find_element(By.NAME, "q")
search.send_keys("Selenium automation tutorial")
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()