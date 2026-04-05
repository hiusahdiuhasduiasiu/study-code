from selenium.webdriver.common.by import By
from POM.base.BasePage import BasePage


class LoginPage(BasePage):  #继承BasePage类

    hc_username = (By.ID, 'txtUName')
    hc_password = (By.ID, 'txtPassword')
    hc_login_button = (By.XPATH,'//*[@id="btnLogin"]')
    hc_quit = (By.XPATH, '//*[@id="headerUserInfo"]/span/a[2]')
    hc_search_input = (By.XPATH, '//*[@id="searchKey"]')

        #告诉代码在做什么
    def do_login(self, username, password):
        self.send_keys(self.hc_username, username)
        self.send_keys(self.hc_password, password)
        self.click(self.hc_login_button)

    def quit_login(self):
        self.click(self.hc_quit)
    #清空搜索框再输入
    def search_input(self):
        self.find_element(By.XPATH, '//*[@id="txtSearch"]').clear()
        self.click(self.hc_search_input)

if __name__ == '__main__':
    lp = LoginPage()
    lp.get_url("http://novel.hctestedu.com/user/login.html")
    from time import sleep
    sleep(3)
    #lp.do_login("15190718897", "241294")
    sleep(5)
    lp.quit_browser()


    #本质是把重复的操作独立提取出去
    #页面操作 -- 都是固定的操作，只是参数不同，元素会变，操作不变
    #打开浏览器-关闭浏览器-输入文字-点击（可以把所有操作提取出去）
