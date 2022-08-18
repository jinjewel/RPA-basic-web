from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option")

browser.switch_to.frame("iframeResult")

time.sleep(1)

# 순서를 이용한 옵션 선택
# # car 에 해당하는 element를 찾고 드롭다운 내부에 있는 3번째 옵션을 선택
# elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[3]')
# elem.click()

# 완전히 일치하는 텍스트를 이용한 옵션 선택
# # 옵션 중에서 텍스트가 opel인 항목을 선택
# elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[text()="Opel"]')
# elem.click()

# 텍스트 값이 부분 일치하는 항목 선택하는 방법
# 옵션 중에서 텍스트 중 AU 가 있는 항목을 선택
elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[contains(text(), "Au")]')
elem.click()



time.sleep(3)

browser.quit()













