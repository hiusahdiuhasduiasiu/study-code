import os
import dashscope
from dashscope import MultiModalConversation
import json
import re

class AIVisionHelper:
    # 建议在环境变量中设置 DASHSCOPE_API_KEY
    api_key = os.getenv("DASHSCOPE_API_KEY", "你的API_KEY_在这里")

    @staticmethod
    def call_qwen_vl(image_path, prompt):
        # 兜底：如果环境变量拿不到，请在这里检查你的 key
        dashscope.api_key = AIVisionHelper.api_key or "你的真实SK"

        messages = [{
            "role": "user",
            "content": [
                {"image": f"file://{image_path}"},
                {
                    "text": f"{prompt}\n请严格按JSON格式返回：{{\"status\": \"PASS/FAIL\", \"reason\": \"原因\", \"location\": [x_ratio, y_ratio]}}"}
            ]
        }]

        try:
            response = MultiModalConversation.call(model="qwen-vl-plus", messages=messages)
            if response.status_code == 200:
                content = response.output.choices[0].message.content[0]['text']
                # 增强正则解析，确保只拿 {} 里的内容
                import re
                match = re.search(r'\{.*\}', content, re.DOTALL)
                if match:
                    res_json = json.loads(match.group())
                    print(f"🤖 AI 分析结果: {res_json}")
                    return res_json
            print(f"❌ AI 响应异常: {response.code} - {response.message}")
            return {"status": "ERROR", "reason": "AI接口异常"}
        except Exception as e:
            print(f"❌ AI 调用代码崩溃: {str(e)}")
            return {"status": "ERROR", "reason": str(e)}
