from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep
#import os
class Browser_driver(object):
    def browser_init(self):
        try:
            #os.environ['WDM_CHROME_DOWNLOAD_URL'] = 'https://npmmirror.com/mirrors/chromedriver/'
            # 尝试自动下载驱动
            edgedriver_path = r"D:\Edge浏览器下载\edgedriver_win64\msedgedriver.exe"
            service = EdgeService(executable_path=edgedriver_path)
            driver = webdriver.Edge(service=service)
            return driver
        except Exception as e:
            print(f"自动下载驱动失败: {str(e)}")
            print("请确保网络连接正常，或手动指定本地驱动路径")
            # 这里可以添加使用本地驱动的代码作为备选方案
            raise
# 新增：实例化类并调用方法，这样才会执行下载逻辑
if __name__ == "__main__":
    browser = Browser_driver()
    driver = browser.browser_init()
    driver.get("https://www.baidu.com")
    sleep(2)
    driver.maximize_window()
    sleep(2)
    #driver.set_window_size(960, 540)
    #sleep(2)
    driver.quit()
"""
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.baidu.com")
from time import sleep
sleep(2)
#国内镜像需要翻墙，不然下载不了
"""
