from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class BasePage(object):
    def __init__(self, driver= None):#初始化浏览器
        if driver:
            self.driver = driver
        else:
            # 配置本地Edge驱动路径（重点修改这里！）
            edge_driver_path = r"D:\Edge浏览器下载\edgedriver_win64\msedgedriver.exe"
            # 创建驱动服务对象
            service = EdgeService(executable_path=edge_driver_path)
            # 初始化Edge浏览器
            self.driver = webdriver.Edge(service=service)
            # 最大化浏览器窗口
            self.driver.maximize_window()


        #self.driver.set_window_maximize()
        #self.driver.set_window_size(1500,1000)

    def get_url(self,url):
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()

    #输入文本
    def send_keys(self,locator,value):
        self.driver.find_element(*locator).send_keys(value)

    def click(self,locator):
        self.driver.find_element(*locator).click()

    def find_element(self,by,value):
        return self.driver.find_element(by,value)


