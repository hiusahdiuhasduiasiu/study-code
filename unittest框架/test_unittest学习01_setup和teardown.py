import unittest

class Testlear01(unittest.TestCase):


    def setUp(self):
        print("---打开浏览器---")

    def tearDown(self):
        print("---关闭浏览器---")

    def test_01(self):
        print("测试用例01")

    def test_02(self):
        print("测试用例02")

    def test_03(self):
        print("测试用例03")

    def test_04(self):
        print("测试用例04")

    def test_05(self):
        print("测试用例05")

if __name__ == '__main__':
    #使用unittest运行器
    unittest.main()