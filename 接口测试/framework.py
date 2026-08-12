import os
from string import Template
import dic
import jsonpath
import requests
import pandas as pd
import pytest
"""
封装框架
"""

#有一段代码 在读取出指定路径的 数据文件。 做到通过修改 数据文件，让它访问不同的接口 操作
"""
数据文件 -- 有格式区别，常用的：yml【pyyaml】,excel【pandas】, --数据库，redis..存放功能都可以
核心思路 -- 读数据 - 执行测试【发请求，收回答】 -- 断言 -- 生成报告 ⭐️⭐️⭐️
"""

#读取 excel 测试用例
file_path = r"..接口测试用例.xlsx"
def read_excel(file_path,sheet=1):
    df = pd.read_excel(file_path,sheet_name=sheet-1)
    return df.to_dict('records')
#读取用例文件
datas = read_excel(file_path,sheet=1)
#print(datas)

dic = {} #存放公共数据

# def excute(url,method,data,params):
@pytest.mark.parametrize('case_info', datas)
#⬆️@pytest.mark.parametrize装饰器 -- 把datas数组中的字典挨个传递给case_info，直到把datas字典执行完
# def test_case(case_info):
#     print(case_info)
def test_excute(case_info):
    url = case_info["url"]
    if '$' in url:
        url = Template(url).substitute(dic)
    应答 = requests.request(
        method=case_info["method"],
        url=url,
        params=eval(case_info["params"]),
        #eval()可以格式化内容，把文档中'{"":"","":""}'的单引号去掉，保证传输的是原本的字典
        data=case_info["json参数"])#发送请求 -- 参数化处理
    #显示应答数据
    print(应答.json())

    # token = jsonpath.jsonpath(应答.json(), '$..token')

    assert case_info["预期状态码"] == 应答.status_code #浏览器状态码是否和测试用例文档中一样

    """
    此时还差一个接口关联，如何再次测试其他接口，会报错，因为其他接口没有token。那我要做的是实现接口关联
    判断 是否要提取结果的值
    提取后放在公共容器中
    变量渲染：详解见变量渲染.py ----------
    """
    if case_info["提取参数"]:
        rlst = jsonpath.jsonpath(应答.json(), "$.."+case_info["提取参数"])
        dic[case_info["提取参数"]] = rlst[0]

#测试报告 -- allure 生成(纯命令) allure-command-line
#allure generate   本次测试结果的文件夹位置（e:/xxx）-0测试报告的路径（自动生成）--Clean


if __name__ == '__main__':
    pytest.main(["-vs",
                 "--capture=sys",#捕获输出
                 "test_framework.py",
                 "--clean-alluredir",#执行器清除上次的执行结果
                 "--alluredir=allure-results",#本次执行结果存放位置
                 ])#未安装 allure，运行不出来，到 Windows 尝试

    os.system("allure generate allure-result -o ./report_allure --clean")

"""
#使用@pytest.mark.parametrize取代for循环
for data in datas:
    excute(data)
    print(end='\n')
"""

"""
excute(url="http://shop-xo.hctestedu.com/index.php?s=/index/user/login.html",
       method="post",
       params={"application": "app", "application_client_type": "weixin"},  # 参数
       data={"accounts": "15190718897", "pwd": "241294", "type": "username"})

"""

#调用函数，执行登陆 -- jar包 war包 -- exe文件
#执行文件 与 数据文件分离




