from POM_AI辅助测试.base.BasePage import BasePage

class BaiduPage(BasePage):
    SEARCH_INPUT = ("id", "kw")
    SEARCH_BTN = ("id", "su")

    def search_keyword(self, text):
        # 使用智能输入，解决 ElementNotInteractableException
        self.smart_send_keys(self.SEARCH_INPUT, text, "百度搜索输入框")
        # 使用智能点击
        self.smart_click(self.SEARCH_BTN, "百度一下按钮")

    def check_result(self, text):
        # AI视觉验证
        self.ai_smart_assert(f"页面成功展示了关于'{text}'的搜索结果")
