import yaml


def get_yaml(file):
    with open(file) as f:
        files = yaml.safe_load(f)
        return files

# print(get_yaml('testData.yml'))
# # a = get_yaml('testData.yml')
# # name = a['add']['name']
# # print(name)