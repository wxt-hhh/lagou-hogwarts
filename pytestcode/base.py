import yaml


# 读取yaml文件
def get_yaml(file):
    with open(file) as f:
        datas = yaml.safe_load(f)
    return datas
