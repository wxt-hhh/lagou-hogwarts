import yaml


def get_yaml(file):
    with open(file) as f:
        files = yaml.safe_load(f)
        return files

# print(get_yaml('testData.yml'))
# data = get_yaml('../datas/devices.yml')
# for i in range(len(data)):
#     print(data[i])