from selenium import webdriver
# BY: 也就是依照條件尋找元素中XPATH、CLASS NAME、ID、CSS選擇器等都會用到的Library
from selenium.webdriver.common.by import By
# keys: 鍵盤相關的Library
from selenium.webdriver.common.keys import Keys
# Select: 下拉選單相關支援，但前端框架UI工具不適用(ex: Quasar、ElementUI、Bootstrap)
from selenium.webdriver.support.ui import Select
# WebDriverWait: 等待頁面加載完成的顯性等待機制Library
from selenium.webdriver.support.ui import WebDriverWait
# ActionChains: 滑鼠事件相關
from selenium.webdriver.common.action_chains import ActionChains
# expected_conditions: 條件相關
from selenium.webdriver.support import expected_conditions as EC
# Chrome WebDriver 需要DRIVER Manager的支援
from webdriver_manager.chrome import ChromeDriverManager
# 延遲時間相關
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("detach", True)

# 關閉自動記住密碼的提示彈窗
options.add_experimental_option("prefs", {
    "profile.password_manager_enabled": False,
    "credentials_enable_service": False})

driver = webdriver.Chrome(options)
driver.get('https://24h.pchome.com.tw/prod/DCAN8M-A9009U21M?fq=/S/DSARAS')

driver.find_element(By.XPATH,'//*[@id="ProdBriefing"]/div/div/div/div[2]/div[5]/div/div[2]/div[2]/button/span/span').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/header/nav/div/div/div[2]/div/div/div[1]/div/div[2]/a').click()

# 帳號密碼的登入
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginAcc"]'))).send_keys("0972791355")
driver.find_element(By.XPATH,'//*[@id="btnKeep"]/span').click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginPwd"]'))).send_keys("Yoyo0525")
driver.find_element(By.XPATH,'//*[@id="btnLogin"]/span').click()

# 選擇付款方式
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="a_cod"]'))).click()
# driver.find_element(By.XPATH,'//*[@id="a_cod"]').click()
