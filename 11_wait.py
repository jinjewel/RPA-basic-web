from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://flight.naver.com/')
# browser.maximize_window()

# 가는 날 클릭
time.sleep(10)
browser.find_element(By.LINK_TEXT, '"가는 날"').click()

time.sleep(5)
browser.quit()