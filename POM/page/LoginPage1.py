from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        hc_username = (By.xpath, "//input[@name='username']")
        hc_password = (By.xpath, "//input[@name='password']")
        hc_login_button = (By.xpath, "//button[@type='submit']")
        hc_quit = (By.xpath, "//button[@type='button']")

        #告诉代码在做什么
        def do_login(self, username, password):
            self.sendkeys(self.hc_username, username)
            self.sendkeys(self.hc_password, password)
            self.click(self.hc_login_button)

        def quit_login(self):
            self.click(self.hc_quit)

        #本质是把重复的操作独立提取出去
        #页面操作 -- 都是固定的操作，只是参数不同，元素会变，操作不变
        #打开浏览器-关闭浏览器-输入文字-点击（可以把所有操作提取出去）
