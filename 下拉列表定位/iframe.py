from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import Select
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait


def driver_init():
    try:
        driver_path = r"D:\Edge浏览器下载\edgedriver_win64\msedgedriver.exe"
        service = EdgeService(executable_path=driver_path)
        driver = webdriver.Edge(service=service)
        return driver
    except Exception as e:
        print("Edge浏览器驱动初始化失败", e)

if __name__ == '__main__':
    driver = driver_init()
    driver.get("http://shop-xo.hctestedu.com/")
    driver.maximize_window()
    sleep(2)
    #登录
    driver.find_element(By.XPATH, "/html/body/div[2]/div/ul[1]/div/div/a[1]").click()
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input").send_keys("15190718897")
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input").send_keys("241294")
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button").click()
    sleep(4)

    #找到地址填写
    # driver.find_element(By.XPATH, "/html/body/div[2]/div/ul[2]/div[1]/div/a/span").click()
    add_address = WebDriverWait(driver, 10 ,ignored_exceptions="no ele").until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/ul[2]/div[1]/div/a/span"))
    )
    add_address.click()

    driver.find_element(By.XPATH, '//*[@id="collapse-nav-base"]/li[2]/a').click()
    sleep(2)

    #driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div[1]/button").click()
    #driver.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/input").send_keys("15190718897")
    #上面方法行不通，需要使用切换到iframe

    driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div[1]/button").click()# 点击添加地址
    # 获取iframe的XPATH
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[@src= 'http://shop-xo.hctestedu.com/index.php?s=/index/useraddress/saveinfo.html']"))
    )
    # 切换到iframe
    driver.switch_to.frame(iframe)
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/input").send_keys("韩毅") #别名
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/input").send_keys("韩毅") #姓名
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[3]/input").send_keys("15190718897") #电话
    # select = Select(driver.find_element(By.XPATH, '//a[@class="chosen-single chosen-default"]'))
    # Select(select).select_by_visible_text("江苏省")
    # 这里是 a 标签，而不是select下拉标签，所以不能用select解决
    # ---选择省份---
    utl_click1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '(//a[@class="chosen-single chosen-default"])[1]'))
    )
    utl_click1.click()
    sleep(2)
    # driver.find_element(By.XPATH, '//div[@class="chosen-drop"]//li[text()="江苏省"]').click()
    add_address = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='chosen-drop']//li[text()='江苏省']"))# class是标签的属性，要加@，li是标签名,不叫@
    )
    add_address.click()
    sleep(5)
    # ---选择市---
    """
    utl_click2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '(//a[@class="chosen-single chosen-default"])[2]'))
    )
    utl_click2.click()
    sleep(5)
    #卡在选择市这一步，没有点击到市，待解决ing
    """


    driver.find_element(By.XPATH, '(//a[@class="chosen-single chosen-default"])[2]').click()
    add_address = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='chosen-drop']//li[text()='徐州市']"))
    )
    add_address.click()
    sleep(2)

    # ---选择区---
    utl_click3 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '(//a[@class="chosen-single chosen-default"])[3]'))
    )
    utl_click3.click()
    sleep(2)
    # driver.find_element(By.XPATH, '//div[@class="chosen-drop"]//li[text()="江苏省"]').click()
    add_address = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='chosen-drop']//li[text()='新沂市']"))
    )
    add_address.click()
    sleep(2)

    driver.find_element(By.XPATH, '//*[@id="form-address"]').send_keys("新安镇墨河街道") #国家
    driver.find_element(By.XPATH, '/html/body/div[1]/form/div[7]/button').clear()
    sleep(2)
    # driver.find_element(By.XPATH, "/html/body/div[1]/form/div[4]/input").send_keys("中国") #国家
    # driver.find_element(By.XPATH, "/html/body/div[1]/form/div[5]/input").send_keys("中国") #省份
    # driver.find_element(By.XPATH, "/html/body/div[1]/form/div[6]/input").send_keys("湖南省") #省份
    # driver.find_element(By.XPATH, "/html/body/div[1]/form/div[7]/input").send_keys("长沙市") #城市
    # driver.find_element(By.XPATH, "/html/body/div[1]/form/div[8]/input").send_keys("岳麓区") #区县

    sleep(2)
