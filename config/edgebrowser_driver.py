from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep
import os
class EdgeBrowser_driver(object):
    def edge_browser(self):
        try:
            # print("开始自动下载Edge驱动...")

            # 设置国内镜像源（关键步骤）
            # os.environ['WDM_EDGE_CHROMIUM_DRIVER_MIRROR_URL'] = 'https://npmmirror.com/mirrors/edgedriver/'

            # 或者使用备选镜像
            # os.environ['EDGE_CHROMIUM_DRIVER_URL'] = 'https://registry.npmmirror.com/-/binary/edgedriver/'

            driver_path = r"D:\Edge浏览器下载\edgedriver_win64\msedgedriver.exe"
            print(f"驱动下载成功，路径: {driver_path}")

            driver = webdriver.Edge(service=EdgeService(driver_path))
            print("Edge浏览器初始化成功")
            return driver
        except Exception as e:
            print(f"自动下载驱动失败: {str(e)}")
            print("请确保网络连接正常，或手动指定本地驱动路径")
            # 这里可以添加使用本地驱动的代码作为备选方案
            raise
"""
if __name__ == '__main__':
    edge_browser = EdgeBrowser_driver()
    driver = edge_browser.edge_browser()
    driver.get("https://www.baidu.com")
    sleep(2)
    driver.quit()

"""
