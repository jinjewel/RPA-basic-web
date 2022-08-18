from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame("iframeResult") # iframe 전환

elem = browser.find_element(By.XPATH, '//*[@id="html"]')

elem.click()

browser.switch_to.default_content() # 상위로 빠져 나옴

time.sleep(5)

browser.quit()