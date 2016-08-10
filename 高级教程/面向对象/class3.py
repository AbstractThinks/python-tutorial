#-*- coding:utf-8 -*-

'''
继承

class a:
    pass

class b(a):
    pass

b继承a

多重继承

class a:
    pass

class c:
    pass

class b(a, c):
    pass


issbclass(sub, sup)-判断一个类是另一个类的子类或者子孙类
isinstance(obj, Class)-判断obj是Class类的实例对象或者是一个Class子类的实例对象
'''


class Parent:
    parentAttr = 100
    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print('调用父类方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性 :", Parent.parentAttr)

    def rewrite(self):
        print('调用父类方法')

class Child(Parent):
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print("调用子类方法")

    def rewrite(self):
        print('调用子类方法')

#实例化子类
c = Child()
#调用子类的方法
c.childMethod()
#调用父类方法
c.parentMethod()
#再次调用父类的方法
c.setAttr(200)
#再次调用父类的方法
c.getAttr()
print(dir(c))
print(c.parentAttr)
#子类重写父类方法
c.rewrite()
print(c.__module__)
print(c.__doc__)
print(c.__class__)


'''
结果

调用子类构造方法
调用子类方法 child method
调用父类方法
父类属性: 200
调用子类方法

'''




















