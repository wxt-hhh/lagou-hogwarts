class Animal:
    def __init__(self, name, colour, age, sex):
        self.name = name
        self.colour = colour
        self.age = age
        self.sex = sex

    def call(self):
        print('会叫')

    def run(self):
        print('会跑')


class Cat(Animal):
    def __init__(self, name, colour, age, sex, hair='short hair'):
        self.name = name
        self.colour = colour
        self.age = age
        self.sex = sex
        self.hair = hair

    def catch_mice(self):
        print(f'猫猫的姓名{self.name}，颜色{self.colour}，年龄{self.age}，性别{self.sex}，毛发{self.hair}，捉到了老鼠')

    def call(self):
        print('miaow miaow miaow')


class Dog(Animal):
    def __init__(self, name, colour, age, sex, hair='long hair'):
        self.name = name
        self.colour = colour
        self.age = age
        self.sex = sex
        self.hair = hair

    def call(self):
        print('woof woof woof')

    def watch_house(self):
        print(f'狗狗的姓名P{self.name}，颜色{self.colour}，年龄{self.age}，性别{self.sex}，毛发{self.hair},可以看家')


if __name__ == '__main__':
    import yaml

    # with open('./animal.yml', 'w') as f:
    #     cat = [['cat', {'name': 'tom', 'colour': 'blue', 'age': 20, 'sex': 'boy'}],
    #            ['dog', {'name': 'tom', 'colour': 'yellow', 'age': 20, 'sex': 'boy'}]]
    # yaml.dump(cat, stream=f)
    # print(yaml.dump(cat))
    with open('./animal.yml', 'r') as f:
        animals = yaml.safe_load(f)
        # print(animals)
        for i in animals:
            if 'cat' in i:
                animal_cat = i[1]
            elif 'dog' in i:
                animal_dog = i[1]
    c_name = animal_cat.get('name')
    c_colour = animal_cat.get('colour')
    c_age = animal_cat.get('age')
    c_sex = animal_cat.get('sex')
    d_name = animal_dog.get('name')
    d_colour = animal_dog.get('colour')
    d_age = animal_dog.get('age')
    d_sex = animal_dog.get('sex')
    a = Cat(c_name, c_colour, c_age, c_sex)
    a.catch_mice()
    b = Dog(d_name, d_colour, d_age, d_sex)
    b.watch_house()
