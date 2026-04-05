import json

from string import Template
import jsonpath

# 模拟接口返回的 JSON 数据（两种结构，验证 $. 和 $.. 的区别）
response_data1 = {
    "code": 0,
    "msg": "success",
    "token": "b029eafd5caf62251ab7b7a222bca573"  # token 在根节点
}

response_data2 = {
    "code": 0,
    "msg": "success",
    "data": {
        "user_info": {
            "token": "b029eafd5caf62251ab7b7a222bca573"  # token 嵌套在深层
        }
    }
}

# 测试用例配置
case_info = {
    "提取参数": "token"
}

# 1. 测试 $.token（单级查找）
print("=== 测试 $.token ===")
result1 = jsonpath.jsonpath(response_data1, "$.token")
print(f"在 response_data1 中提取结果: {result1}")  # 能成功

result2 = jsonpath.jsonpath(response_data2, "$.token")
print(f"在 response_data2 中提取结果: {result2}")  # 提取失败，返回 False

# 2. 测试 $..token（递归查找）
print("\n=== 测试 $..token ===")
result3 = jsonpath.jsonpath(response_data1, "$..token")
print(f"在 response_data1 中提取结果: {result3}")  # 能成功

result4 = jsonpath.jsonpath(response_data2, "$..token")
print(f"在 response_data2 中提取结果: {result4}")  # 也能成功！

# 3. 模拟框架中的参数提取和存储
print("\n=== 模拟框架参数提取 ===")
global_data = {}  # 公共容器

if case_info.get("提取参数"):
    # 使用 $.. 拼接表达式
    expr = f"$..{case_info['提取参数']}"
    extract_result = jsonpath.jsonpath(response_data2, expr)

    if extract_result:
        global_data[case_info["提取参数"]] = extract_result[0]
        print(f"提取并存储成功: {global_data}")
    else:
        print("提取失败，未找到目标字段")


ss={"token":"小明同学"}
str = "${token}大帅哥"
print("\n"+Template(str).substitute(ss))
