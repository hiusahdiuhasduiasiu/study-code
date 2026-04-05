from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import Select
from time import sleep
"""
下拉列表显示
"""

def driver_init():
    try:
        driver_path = r"D:\Edge浏览器下载\edgedriver_win64\msedgedriver.exe"
        service = EdgeService(executable_path=driver_path)
        driver = webdriver.Edge(service=service)
        return driver
    except:
        print("Edge浏览器驱动初始化失败")

if __name__ == '__main__':
    driver = driver_init()
    driver.get("https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc")
    driver.maximize_window()
    sleep(2)


"""
#方法一：使用select类
# 第一步，先找到父元素 -- select
select = driver.find_element(By.ID, "cc_start_time")
#第二步 通过父类找到对应的子元素 -- index/value/visible_text
# Select(父元素).select()
Select(select).select_by_index(1)
from time import sleep
sleep(2)
Select(select).select_by_value("06001200")
sleep(2)
Select(select).select_by_visible_text("12:00--18:00")
sleep(2)
driver.refresh()
sleep(2)
"""


#方法二：使用之前学过的方法
#先使用找到父元素 -- select
select = driver.find_element(By.ID, "cc_start_time")
sleep(2)
#再找到父元素对应的子类（xpath）
#//*[@id="cc_start_time"]/option[1] --直接复制的
#//*[@value=00000600]
select.find_element(By.XPATH, '//*[@value="00000600"]').click()
sleep(2)