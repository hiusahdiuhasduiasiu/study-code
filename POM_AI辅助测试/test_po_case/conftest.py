from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import platform
import pytest
import os
driver = None
@pytest.fixture(scope="session")
def browser():
    print("登录")
    global driver
    if driver is None:
        system = platform.system()
        if system == "Windows":
            driver_path = r"driver/msedgedriver.exe" #在我自己的Windows运行
            service = EdgeService(executable_path=driver_path)
            driver = webdriver.Edge(service=service)
            edge_options = webdriver.EdgeOptions()
        elif system == "Darwin": #macos
            # driver_path = EdgeChromiumDriverManager().install()
            # service = EdgeService(driver_path)
            # driver = webdriver.Edge(service=service)
            # edge_options = webdriver.EdgeOptions()
            driver = webdriver.Edge()
            driver.maximize_window()
            driver.implicitly_wait(10)

        driver.maximize_window()


    # global driver
    # if driver is None:
    #     edge_driver_path = r"D:\Edge浏览器下载\edgedriver_win64\msedgedriver.exe"
    #     service = EdgeService(executable_path=edge_driver_path)
    #     driver = webdriver.Edge(service=service)
    #     edge_options = webdriver.EdgeOptions()
        """
        #使用远程浏览器并发协同进行自动测试，安装selenium grid
         driver=webdriver.Remote(
            command_executor='http://127.0.0.1:4444',
            options=edge_options
        )
        driver.set_window_size(1920, 1080)
        driver.set_window_position(0, 0)
        """

    yield driver
    driver.quit()
    print("退出登录")
