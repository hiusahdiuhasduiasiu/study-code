import pandas as pd

def read_cases(file_path):
    #读取Excel文件
    df = pd.read_excel(file_path)
    #将每一行转化为字典列表，方便pytest调用

def write_results(file_path, results):
    #这里实现将执行结果写回Excel的逻辑
    pass