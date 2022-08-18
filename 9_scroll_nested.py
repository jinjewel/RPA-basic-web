from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains # ActionChain 를 사용하기 위해 선언

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/html/')
browser.maximize_window()

time.sleep(3)

# 특정 영역 스크롤
elem = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[62]')

# 방법 1 : ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform() # .perform() : 수행한다

# 방법 2: 좌표정보 이용
xy = elem.location_once_scrolled_into_view # 함수가 아니니까 () 쓰지 않는다.
time.sleep(3)

elem.click() # 스크롤을 내려 해당 위치를 보이지 않아도 클릭은 가능하다.

time.sleep(3)
browser.quit()