import yaml


# 读取yaml文件
def get_yaml(file):
    data = yaml.safe_load(open(file))
    return data
