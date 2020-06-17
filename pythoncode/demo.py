def func():
    print('无参数的方法')


def func1(name):
    print('有参数的方法' + name)


func()
func1('TOM')


def func2():
    '''
    无返回值,默认为None
    '''
    return


def func3(name='tom'):
    '''
    返回默认值tom
    '''
    return print(name)


print(func2())
func3()
