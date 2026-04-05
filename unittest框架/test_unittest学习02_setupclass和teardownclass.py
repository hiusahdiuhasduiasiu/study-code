import unittest

class Testlear02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("---打开浏览器---")

    # def setUp(self):
    #     print("---打开浏览器---")

    @classmethod
    def tearDownClass(cls):
        print("---关闭浏览器---")

    # def tearDown(self):
    #     print("---关闭浏览器---")

    def test_01(self):
        print("测试用例01")

    def test_02(self):
        print("测试用例02")

    def test_03(self):
        print("测试用例03")

if __name__ == '__main__':
    #使用unittest运行器
    unittest.main()