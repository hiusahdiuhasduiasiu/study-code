import os

import pytest

if __name__ == '__main__':
    pytest.main(["-vs",
                 "--capture=sys",#捕获输出
                 "test_framework.py",
                 "--clean-alluredir",#执行器清除上次的执行结果
                 "--alluredir=allure-results",#本次执行结果存放位置
                 ])#未安装 allure，运行不出来，到 Windows 尝试

    os.system("allure generate allure-result -o ./report_allure --clean")
