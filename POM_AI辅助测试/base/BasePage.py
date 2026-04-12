import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM_AI辅助测试.AI_Vision_helper import AIVisionHelper


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        if not os.path.exists("logs"):
            os.makedirs("logs")

    def smart_click(self, locator, element_name):
        """带AI兜底的智能点击"""
        try:
            # 尝试正常点击
            el = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
            el.click()
        except Exception as e:
            print(f"⚠️ 无法点击 {element_name}，启动AI修复: {str(e)}")
            self._ai_coordinate_click(element_name)

    def smart_send_keys(self, locator, text, element_name):
        """带AI兜底的智能输入"""
        try:
            # 增加可见性判断，百度首页建议先点一下输入框激活它
            el = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
            el.click()  # 先点一下，激活输入状态
            el.clear()
            el.send_keys(text)
            print(f"✅ {element_name} 正常输入成功")
        except Exception as e:
            print(f"⚠️ 无法在 {element_name} 直接输入，启动AI辅助修复...")
            # 1. 调用AI物理点击坐标
            self._ai_coordinate_click(element_name)

            # 2. 点击完坐标后再次尝试输入，如果还不行，说明真的出问题了
            try:
                time.sleep(1)  # 给页面一点反应时间
                final_el = self.driver.find_element(*locator)
                final_el.send_keys(text)
                print(f"✅ 通过AI辅助，{element_name} 输入成功")
            except Exception as final_e:
                raise AssertionError(f"❌ 即使用了AI兜底，依然无法在 {element_name} 输入。原果: {final_e}")

    def _ai_coordinate_click(self, element_name):
        """内部方法：利用AI坐标进行物理点击"""
        img_path = os.path.abspath(f"logs/healing_{int(time.time())}.png")
        self.driver.save_screenshot(img_path)

        prompt = f"请找到页面中名为'{element_name}'的元素中心坐标"
        res = AIVisionHelper.call_qwen_vl(img_path, prompt)

        if res.get('location'):
            w = self.driver.get_window_size()['width']
            h = self.driver.get_window_size()['height']
            x = res['location'][0] * w
            y = res['location'][1] * h
            # 使用 ActionChains 进行物理坐标点击
            ActionChains(self.driver).move_to_location(x, y).click().perform()
            time.sleep(1)

    def ai_smart_assert(self, assert_desc):
        """AI视觉断言"""
        img_path = os.path.abspath(f"logs/assert_{int(time.time())}.png")
        self.driver.save_screenshot(img_path)
        res = AIVisionHelper.call_qwen_vl(img_path, f"断言任务：{assert_desc}")

        if res.get('status') == 'FAIL':
            raise AssertionError(f"❌ AI视觉断言失败: {res.get('reason')}")
        print(f"✅ AI断言通过: {res.get('reason')}")
