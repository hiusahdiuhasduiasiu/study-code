from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.page.LoginPage2 import LoginPage
from time import sleep
import allure

class TestNovel:
    @allure.story("登录功能")
    @allure.title("成功登录测试")
    def test_01(self,browser):
        with allure.step("打开登录页面"):
            hy = LoginPage(browser)
            hy.get_url("http://novel.hctestedu.com/user/login.html")
        with allure.step("输入用户名和密码"):
            hy.do_login("15190718897", "241294")
            sleep(3)
    @allure.story("占位测试")
    def test_02(self,browser):
        pass

    # @allure.story("搜索与阅读功能")
    # @allure.title("搜索《剑来》并点击阅读")
    # def test_03(self,browser):#搜索小说，并点击阅读
    #     hy = LoginPage(browser)
    #     with allure.step("点击搜索 《剑来》"):
    #         hy.find_element(By.XPATH, '//*[@id="searchKey"]').click()
    #         hy.find_element(By.XPATH, '//*[@id="searchKey"]').send_keys('剑来')
    #         hy.find_element(By.XPATH, '//*[@id="btnSearch"]/i').click()
    #         sleep(2)
    #     with allure.step("点击搜到的 剑来，并点击阅读"):
    #         hy.find_element(By.XPATH, '//*[@id="bookList"]/tr/td[3]/a').click()
    #         #点击阅读
    #         # hy.find_element(By.XPATH, '//*[@id="chapterList"]/tr/td[2]/a').click()
    #         hy.find_element(By.XPATH, '//*[@id="optBtn"]/a').click()
    #         #点击收藏
    #         utl_click_collect = WebDriverWait(browser, 10).until(
    #             EC.presence_of_element_located((By.XPATH, '//*[@id="cFavs"]/a/b'))
    #         )
    #         # 若已经收藏，则收藏按钮不可点击
    #         sleep(3)
    #     with allure.step("跳转到书架页面"):
    #         hy.find_element(By.XPATH, '//*[@id="headerUserInfo"]/a').click()
    #         sleep(2)
    #     with allure.step("断言：书架中有书"):
    #         # 简单的校验，确保页面包含章节内容
    #
    #         assert "剑来" in browser.page_source
    # #进阶，添加收藏，并判断是否成功收藏
    @allure.story("搜索与收藏功能 -- DDT")
    @allure.title("搜索：{book_name}")
    @pytest.mark.parametrize("book_name",["剑来","雪中悍刀行","斗罗大陆"])
    #DDT核心数据
    def test_03(self, browser, book_name):#搜索小说，并点击阅读
        hy = LoginPage(browser)
        with allure.step(f"点击搜索 {book_name}"):
            #一定要清空搜索栏，不然会造成没搜索到雪中悍刀行，又输入斗罗大陆，最终搜索栏会显示雪中悍刀行斗罗大陆
            search_input = hy.find_element(By.XPATH, '//*[@id="searchKey"]')
            search_input.clear()
            search_input.click()
            hy.find_element(By.XPATH, '//*[@id="searchKey"]').send_keys(book_name)
            hy.find_element(By.XPATH, '//*[@id="btnSearch"]/i').click()
            sleep(2)
        with allure.step(f"点击搜到的 {book_name}，并点击阅读"):
            hy.find_element(By.XPATH, '//*[@id="bookList"]/tr/td[3]/a').click()
            #点击阅读
            # hy.find_element(By.XPATH, '//*[@id="chapterList"]/tr/td[2]/a').click()
            hy.find_element(By.XPATH, '//*[@id="optBtn"]/a').click()
            #点击收藏
            utl_click_collect = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="cFavs"]/a/b'))
            )
            # 若已经收藏，则收藏按钮不可点击
            sleep(3)
        with allure.step("跳转到书架页面"):
            hy.find_element(By.XPATH, '//*[@id="headerUserInfo"]/a').click()
            sleep(2)
        with allure.step("断言：书架中有书"):
            # 简单的校验，确保页面包含章节内容

            assert book_name in browser.page_source,f"未找到 {book_name} 在书架中"
    #进阶，添加收藏，并判断是否成功收藏




if __name__ == '__main__':
#    pytest.main("-v","-s",__file__)
    # 运行会自动生成 report 数据到本地文件夹
    pytest.main(["-s", "-v", "--alluredir=./reports", __file__])

"""
from selenium.webdriver.common.by import By
import pytest
import allure
from time import sleep
from POM.page.LoginPage2 import LoginPage # 确保路径与你本地一致

@allure.feature("小说网站自动化测试项目")
class TestNovel:

    @allure.story("登录功能")
    @allure.title("成功登录测试")
    def test_01(self, browser):
       #对应你原有的 test_01
        with allure.step("打开登录页面并执行登录"):
            hy = LoginPage(browser)
            hy.get_url("http://novel.hctestedu.com/user/login.html")
            hy.do_login("15190718897", "241294")
            sleep(3)
        with allure.step("校验：是否跳转到首页"):
            assert "index.html" in browser.current_url or "novel" in browser.current_url

    @allure.story("占位测试")
    def test_02(self, browser):
        #对应你原有的 test_02
        pass

    @allure.story("搜索与阅读功能")
    @allure.title("搜索《剑来》并点击阅读")
    def test_03(self, browser):
        #对应你原有的 test_03
        hy = LoginPage(browser)
        
        with allure.step("搜索小说：剑来"):
            # 这里沿用你原有的 find_element 逻辑
            hy.find_element(By.XPATH, '//*[@id="searchKey"]').click()
            hy.find_element(By.XPATH, '//*[@id="searchKey"]').send_keys('剑来')
            hy.find_element(By.XPATH, '//*[@id="btnSearch"]/i').click()
            sleep(2)
            
        with allure.step("从搜索结果点击书籍并阅读"):
            # 点击搜到的 剑来
            hy.find_element(By.XPATH, '//*[@id="bookList"]/tr/td[3]/a').click()
            # 点击阅读按钮
            hy.find_element(By.XPATH, '//*[@id="optBtn"]/a').click()
            sleep(3)
        
        with allure.step("断言：验证是否进入阅读页面"):
            # 简单的校验，确保页面包含章节内容
            assert "book" in browser.current_url

# 如果你想保留 DDT（数据驱动）测试，可以在下面接着写：
# login_data = [("15190718897", "241294", "成功"), ("user2", "pwd2", "失败")]
# @pytest.mark.parametrize("u,p,t", login_data)
# def test_login_ddt(self, browser, u, p, t):
#     ... 逻辑同上 ...

if __name__ == '__main__':
    # 这样运行会自动生成 report 数据到本地文件夹
    pytest.main(["-s", "-v", "--alluredir=./reports", __file__])

"""