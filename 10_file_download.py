from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':r'C:\ohcoding'})

browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')
# browser.maximize_window()

browser.switch_to.frame('iframeResult')

elem = browser.find_element(By.XPATH, '/html/body/p[2]/a')
elem.click()

time.sleep(3)
browser.quit()
