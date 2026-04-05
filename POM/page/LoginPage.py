from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class Browser_driver(object):
    def browser_init(self):
        try:
            #os.environ['WDM_CHROME_DOWNLOAD_URL'] = 'https://npmmirror.com/mirrors/chromedriver/'
            # 尝试自动下载驱动
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            return driver
        except Exception as e:
            print(f"自动下载驱动失败: {str(e)}")
            print("请确保网络连接正常，或手动指定本地驱动路径")
            # 这里可以添加使用本地驱动的代码作为备选方案
            raise