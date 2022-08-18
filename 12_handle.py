from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')
browser.maximize_window()

curr_handle = browser.current_window_handle
print(curr_handle) # 현재 위도우 핸들 정보

browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles # 모든 핸들 정보
for handle in handles:
    print(handle) # 각 핸들 정보 출력
    print()
    browser.switch_to.window(handle) # 각 핸들로 이동해서
    print(browser.title)
    print()

# 새로 이동된 브라우져에서 뭔가 자동화 작업을 수행...
time.sleep(3)

# 그 브라우져를 종료
print("현재 핸들 닫기")
browser.close()

# 이전 핸들로 돌아오기
print("처음 핸들로 돌아오기")
browser.switch_to.window(curr_handle)

print(browser.title)

# 브라우져 컨드롤이 가능한지 확인
time.sleep(5)
browser.get("http://daum.net")

time.sleep(3)
browser.quit()








