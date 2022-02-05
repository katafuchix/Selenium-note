import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
import chromedriver_binary, time

driver = webdriver.Chrome()

driver.get(" スレのURL ")
driver.get_cookies()

comment = '書き込み内容'
driver.find_element_by_name("MESSAGE").send_keys(comment)
driver.find_element_by_name("submit").click() # 書き込み画面送信

time.sleep(1)
driver.find_element_by_name("submit").click() # 確認画面送信

driver.close()
driver.quit()
