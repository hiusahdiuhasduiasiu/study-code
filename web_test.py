from config.edgebrowser_driver import EdgeBrowser_driver
from selenium.webdriver.common.by import By
from time import sleep


"""
#一个简单的自动化测试脚本
driver = EdgeBrowser_driver().edge_browser()
driver.get('https://www.baidu.com')
driver.find_element(By.ID, 'chat-textarea').send_keys('python')
driver.find_element(By.ID, 'chat-submit-button').click()
driver.quit()
"""
driver = EdgeBrowser_driver().edge_browser()
driver.get('https://mail.qq.com/')
#===点击QQ登录===
driver.find_element(By.XPATH, '//*[@id="qqLoginTab"]/span[2]').click()
#iframe = driver.find_element(By.id, 'bottom_qlogin')

#===点击密码登录===
driver.find_element(By.ID, 'switcher_plogin').click()
#===输入账号密码===
driver.find_element(By.XPATH, '//*[@id="u"]').send_keys('2098241294')
driver.find_element(By.XPATH, '//*[@id="p"]').send_keys('********')
#===点击登录===
driver.find_element(By.XPATH, '//*[@id="login_button"]').click()
driver.quit()

