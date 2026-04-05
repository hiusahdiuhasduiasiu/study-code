# network_check.py
import requests
import socket


def check_network():
    """检测网络环境"""
    print("=" * 50)
    print("网络环境检测")
    print("=" * 50)

    # 检测的URL列表
    urls = [
        ("国内镜像", "https://npmmirror.com"),
        ("微软Edge驱动", "https://msedgedriver.azureedge.net"),
        ("GitHub", "https://github.com"),
        ("百度（测试连通性）", "https://www.baidu.com")
    ]

    for name, url in urls:
        try:
            response = requests.get(url, timeout=5)
            print(f"✅ {name}: 可访问 (状态码: {response.status_code})")
        except requests.exceptions.ConnectionError:
            print(f"❌ {name}: 无法连接")
        except requests.exceptions.Timeout:
            print(f"⏱️  {name}: 连接超时")
        except Exception as e:
            print(f"⚠️  {name}: 错误 - {str(e)}")

    print("\n建议：")
    print("- 如果能访问国内镜像，使用镜像源方案")
    print("- 如果能访问微软域名，可以直接自动下载")
    print("- 如果都不能访问，需要使用代理或手动下载")


if __name__ == "__main__":
    check_network()