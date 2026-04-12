import os
import dashscope
from dashscope import MultiModalConversation

# 配置你的API Key
dashscope.api_key = "sk-05d09a1c4dcd475494b8a1ff0ce7254e"
dashscope.base_http_api_url = "https://dashscope.aliyuncs.com/api/v1"


def ai_visual_assert(screenshot_path, assert_desc):
    """
    AI视觉断言核心函数：让千问VL看图做断言
    :param screenshot_path: 页面截图路径
    :param assert_desc: 自然语言描述的断言预期（比如"页面显示搜索结果列表"）
    :return: (断言结果bool, AI分析原因str)
    """
    # 1. 处理截图路径
    if not os.path.exists(screenshot_path):
        return False, f"截图文件不存在：{screenshot_path}"

    abs_path = os.path.abspath(screenshot_path)
    image_path = f"file://{abs_path}"

    # 2. 构造Prompt（让AI返回标准化结果）
    messages = [
        {
            "role": "user",
            "content": [
                {"image": image_path},
                {
                    "text": f"""
                    你是自动化测试断言专家，严格按以下要求执行：
                    1. 分析截图内容，判断是否符合断言要求：{assert_desc}
                    2. 先返回断言结果（仅能是"符合"或"不符合"），再换行说明具体原因
                    3. 原因要具体，比如"页面显示了搜索结果列表，包含关键词'AI辅助测试'"或"页面无搜索结果，仅显示空白"
                    """
                }
            ]
        }
    ]

    # 3. 调用千问VL
    try:
        response = MultiModalConversation.call(
            model="qwen-vl-plus",
            messages=messages,
            temperature=0.0,
            result_format="message"
        )

        # 4. 解析AI返回结果
        if response.status_code != 200:
            return False, f"AI调用失败：{response.code} - {response.message}"

        ai_result = response.output.choices[0].message.content
        if isinstance(ai_result, list):
            ai_result = ai_result[0].get("text", "").strip()

        # 拆分结果和原因
        if "符合" in ai_result:
            return True, ai_result.split("\n", 1)[1].strip() if "\n" in ai_result else ai_result
        elif "不符合" in ai_result:
            return False, ai_result.split("\n", 1)[1].strip() if "\n" in ai_result else ai_result
        else:
            return False, f"AI返回格式异常：{ai_result}"
    except Exception as e:
        return False, f"AI断言执行异常：{str(e)}"