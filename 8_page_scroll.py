from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://shopping.naver.com/home/p/index.naver")
browser.maximize_window()

# 검색어를 입력하는 방법 : .send_key(' -검색어- ')
time.sleep(2)
elem = browser.find_element(By.XPATH, '//*[@id="_verticalGnbModule"]/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div/input')
elem.send_keys('무선마우스')

# 검색 버튼 클릭
browser.find_element(By.XPATH, '//*[@id="_verticalGnbModule"]/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div/button[2]').click()
# 혹은 enter키 입력하기
# from selenium.webdriver.common.keys import Keys
# elem.send_keys(Keys.ENTER)

# # 스크롤
# # 지정한 위치로 스크롤 내리기
# # 모닡 높이인 1080 위치로 스크롤 내리기
# browser.execute_script('window,scrollTo(0,1080)') # 모니터 해상도에 맞게 길이를 설정한다.
# time.sleep(1)
# browser.execute_script('window,scrollTo(0,2080)')
# time.sleep(1)

# # 화면 가장 아래로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 동적 페이지에 대해서 마지막가지 스크롤 반복 수행
interval = 3 # 2초에 한번씩 스크롤 내리기

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

# 반복수행
while True:
    # 스크롤을 화면 가장 아래로 내림
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # 페이지 로딩
    time.sleep(interval) # 3초

    # 현재 문서 높이 가져와서 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height: # 직전 스크롤의 높이와 같으면(스크롤의 변화가 없으면)
        break # 반복문 탈출(스크롤 내리기를 중단)

    # 현재 스크롤 위치 저장
    prev_height = curr_height

# 맨 위로 올리기
browser.execute_script('window,scrollTo(0,0)')

time.sleep(5)

browser.quit()
