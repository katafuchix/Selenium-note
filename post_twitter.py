from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time

# seleniumを起動
options=Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver=webdriver.Chrome(chrome_options = options)

def login_twitter(account, password):
    # ログインページを開く
    driver.get('https://twitter.com/login/')
    time.sleep(2)

    # account入力
    element_account = driver.find_element_by_name("text")
    element_account.send_keys(account)
    time.sleep(2) 
    # 次へボタンのXPathがこれでしか取れなかった・・・
    # 次へボタンクリック
    element_login = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]')
    element_login.click()
    time.sleep(2) 

    # パスワード入力
    element_pass = driver.find_element_by_name("password")
    element_pass.send_keys(password)
    time.sleep(2) 
    # ログインボタンクリック
    element_login = driver.find_element_by_xpath('//*[@data-testid="LoginForm_Login_Button"]')
    element_login.click()
    time.sleep(2) 
    
 def send_tweet(text):
    # テキスト入力
    element_text = driver.find_element_by_class_name("notranslate")
    element_text.click()
    element_text.send_keys(text)
    # ツイートボタン
    tweet_button = driver.find_element_by_xpath('//*[@data-testid="tweetButtonInline"]')
    driver.execute_script("arguments[0].click();", tweet_button)
 
