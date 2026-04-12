import pytest
from selenium import webdriver

from POM_AI辅助测试.page.baiduPage import BaiduPage


@pytest.fixture
def driver():
    options = webdriver.EdgeOptions()
    # options.add_argument("--start-maximized") # 某些系统有效
    driver = webdriver.Edge(options=options)
    driver.maximize_window()  # 强制最大化
    yield driver
    driver.quit()


def test_baidu_ai_search(driver):
    baidu = BaiduPage(driver)
    driver.get("https://www.baidu.com")

    baidu.search_keyword("AI 自动化测试")
    baidu.check_result("AI 自动化测试")
