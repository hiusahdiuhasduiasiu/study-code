import unittest

from unittest框架.test_unittest学习01_setup和teardown import Testlear01
from unittest框架.test_unittest学习02_setupclass和teardownclass import Testlear02



def runner_case():
    #定义一个测试集合————盒子
    suit = unittest.TestSuite()

    #给盒子添加数据
    #suite.addTest(类名("用例名"))
    suit.addTest(Testlear01("test_01"))
    suit.addTest(Testlear01("test_02"))
    suit.addTest(Testlear02("test_03"))

    # 执行对应的对象
    runner = unittest.TextTestRunner()
    runner.run(suit)

def runner_cases():
    suit = unittest.TestSuite()

    suit_list = [Testlear01("test_01"),Testlear01("test_02"),Testlear02("test_03")]
    suit.addTests(suit_list)

    runner = unittest.TextTestRunner()
    runner.run(suit)

def runner_classcase():
    suit = unittest.TestSuite()

    classcase1 = unittest.TestLoader().loadTestsFromTestCase(Testlear01)
    classcase2 = unittest.TestLoader().loadTestsFromTestCase(Testlear02)
    suit.addTests([classcase1,classcase2])

    runner = unittest.TextTestRunner()
    runner.run(suit)

def runner_all():
    # url = r"D:\PycharmProjects\pythonProject1\unittest框架"
    url = r"..\unittest框架"

    allcase = unittest.defaultTestLoader.discover(url)

    runner = unittest.TextTestRunner()
    runner.run(allcase)

if __name__ == '__main__':
    # runner_case()
    # runner_cases()
    # runner_classcase()
     runner_all()
