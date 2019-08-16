from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome("chromedriver.exe") # さっきDLしたchromedriver.exeを使う
driver.get("https://example.com/") #chrome起動して移動
uidBox = driver.find_element_by_id("uid") #ユーザーID入力ボックスのhtmlを探す
uidBox.send_keys("username")
passwordBox = driver.find_element_by_name("password") #パスワード入力ボックスのhtmlを探す
passwordBox.send_keys("toppan")
loginButton = driver.find_element_by_id("loginSubmit") #htmlからログインボタンを探す
loginButton.click() #ボタンをクリック

sleep(15)

driver.execute_script("window.open(arguments[0], 'newtab')", "https://example.com/example")
