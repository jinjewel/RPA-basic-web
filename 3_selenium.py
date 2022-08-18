from webbrowser import Chrome
from selenium import webdriver

brower = webdriver.Chrome("./chromedriver.exe") # 다운로드를 실행 파일안에서 했으므로 ()안을 비워도 실행된다.

brower.get("http:/naver.net")