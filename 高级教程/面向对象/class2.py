#-*- coding:utf-8 -*-

class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salray = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


#类的文档字符串
print "Employee.__doc__:", Employee.__doc__
#类名
print "Employee.__name__:", Employee.__name__
#类定义所在的模块
print "Employee.__module__:", Employee.__module__
#类的所有父类构成元素
print "Employee.__bases__:", Employee.__bases__
#类的属性
print "Employee.__dict__:", Employee.__dict__


'''
结果


Employee.__doc__: 所有员工的基类
Employee.__name__：Employee
Employee.__module__: __main__
Employee.__bases__: ()
Employee.__dict__:{....}
'''
