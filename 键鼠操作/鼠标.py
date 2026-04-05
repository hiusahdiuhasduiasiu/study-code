from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium import webdriver


def driver_init():
    try:
        driver_path = r"D:\Edge浏览器下载\edgedriver_win64\msedgedriver.exe"
        service = EdgeService(executable_path=driver_path)
        driver = webdriver.Edge(service=service)
        return driver
    except Exception as e:
        print("Edge浏览器驱动初始化失败", e)


def yd_action(driver):
    #  先使用XPATH定位到设置按钮
    wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="s-usersetting-top"]')))
    ActionChains(driver).move_to_element(wait).pause(0.5).perform()
    #  再使用LINK_TEXT定位到高级搜索按钮
    wait = driver.find_element(By.LINK_TEXT, "高级搜索")#
    ActionChains(driver).click(wait).pause(0.5).perform()

def hd_action(driver):
    # 点击同意并继续按钮
    wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/a[2]'))
    )
    wait.click()

    # 拖动 (元素ele , X轴 , Y轴)
    ele = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '滑块XPATH'))
    )
    ele_width = ele.size['width']

    # 更灵活的写法，自动获取滑动的距离（方框宽度）
    # ActionChains(driver).drag_and_drop_by_offset(ele, 100, 0).pause(0.5).perform()
    ActionChains(driver).drag_and_drop_by_offset(ele, ele_width, 0).pause(0.5).perform()



if __name__ == '__main__':
    driver = driver_init()
    #driver.get("https://www.baidu.com/")
    driver.get("https://passport.ctrip.com/user/reg/home")
    driver.maximize_window()
    #yd_action(driver)
