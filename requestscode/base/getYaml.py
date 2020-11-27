import yaml


def getYml(file):
    with open(file) as f:
        newFile = yaml.safe_load(f)
    return newFile


# print(getYml('../data/add_tag.yml'))