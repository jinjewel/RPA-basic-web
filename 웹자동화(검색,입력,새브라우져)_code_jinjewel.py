from ntpath import join
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/')
browser.maximize_window()
time.sleep(2)

# LEARN HTML 클릭
browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[1]').click()
time.sleep(2)

# HOW TO 클릭
browser.find_element(By.XPATH, '//*[@id="topnav"]/div/div[1]/a[10]').click()
time.sleep(2)

# Contact Form 클릭
browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click()
time.sleep(2)

# 입력란에 각 텍스트 입력
First_Name = "jin"
Last_Name = "jewel"
Country = "Canada"
Subject = "입력을 완료 했습니다."

elem_fn = browser.find_element(By.XPATH, '//*[@id="fname"]').send_keys(First_Name)
elem_ln = browser.find_element(By.XPATH, '//*[@id="lname"]').send_keys(Last_Name)
elem_ct = browser.find_element(By.XPATH, '//*[@id="country"]/option[text()="{}"]'.format(Country)).click()
elem_sj = browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea').send_keys(Subject)

# Submit 클릭
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/a').click()

# 창 닫기
time.sleep(1)
browser.quit()