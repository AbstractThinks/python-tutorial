# -*- coding: utf-8 -*-
# 子类里访问父类的同名属性,而又不想直接引用父类的名字,使用super

class OrdinaryParent(object):
    def __init__(self):
        self.parent="I am the parent"
        print("Parent")

    def bar(self, message):
        print(message, "from Parent")

class OrdinaryChild(OrdinaryParent):
    def __init__(self):
        OrdinaryParent.__init__(self)
        print("Child")

    def bar(self, message):
        OrdinaryParent.bar(self, message)
        print("Child bar function")
        print(self.parent)

class SuperParent(object):
    def __init__(self):
        self.parent = 'I am the parent'
        print ("Parent")
    def bar(self, message):
        print (message)

class SuperChild(SuperParent):
    def __init__(self):
        super(SuperChild, self).__init__()
        print("child")
    def bar(self, message):
        super(SuperChild, self).bar("child"+message)

'''
#python3写法
class SuperChild(SuperParent):
    def __init__(self):
        super(SuperChild, self).__init__()
        print("Child")

    def bar(self, message):
        super(SuperChild, self).bar(message)
        print ("Child bar function")
        print(self.parent)
'''

if __name__ == '__main__':
   # ordinary = OrdinaryChild()
   # ordinary.bar("Hello World")

    superobject = SuperChild()
    #superobject.bar("super")
