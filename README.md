#课后作业：
### python实战作业一
- 1、搭建好python,pycharm, git 环境，在本地创建一个pythoncode，和README.MD, 上传到github上，将代码github链接地址贴到作业贴下即可
- 2、创建模块，模块里面创建方法，定义有参数，和无数，有返回值和无返回值 的情况，并说明 无返回值的默认返回值。
### python实战作业二
课后作业：自己写一个面向对象的例子
描述：
创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
- 复写父类的__init__方法，继承父类的属性，
- 添加一个新的属性，毛发=短毛，
- 添加一个新的方法， 会捉老鼠，
- 复写父类的‘【会叫】的方法，改成【喵喵叫】
创建子类【狗】，继承【动物类】，
- 复写父类的__init__方法，继承父类的属性，
- 添加一个新的属性，毛发=长毛，
- 添加一个新的方法， 会看家，
- 复写父类的【会叫】的方法，改成【汪汪叫】
创建一个猫猫实例
- 调用捉老鼠的方法
- 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
创建一个狗狗实例
- 调用【会看家】的方法
- 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
4、使用 yaml 来管理实例的属性
### pytest实战作业一
- 1、补全计算器（加减乘除）的测试用例
- 2、使用数据驱动完成测试用例的自动生成
- 3、conftest.py中创建fixture 完成setup和teardown
- 4、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
### pytest实战作业二
- 1、使用参数化数据驱动，完成加减乘除测试用例的自动生成
- 2、修改测试用例为check_开头，修改测试用例的执行规则，执行所有check_开头和test_开头的测试用例
- 3、控制测试用例顺序按照【加-减-乘-除】这个顺序执行,
- 4、减法依赖加法， 除法依赖乘法
- 5、注册一个命令行参数env,env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据。
### appium企业微信实战作业一
- 1、编写添加联系人测试用例
- 2、编写删除联系人测试用例
- 注意：
    - 注意setup_class,setup, teardown, teardown_class 灵活使用
    - 将测试数据保存在yaml文件里面读取出来
    - 添加联系人与删除联系人共有一份测试数据文件
### appium企业微信实战作业二
- 1、PO 模式封装添加联系人与删除联系人测试用例