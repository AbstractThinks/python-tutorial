#-*- coding:utf-8 -*-

'''
类的定义
'''
class Employee:

    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" %Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


'''
创建实例
'''

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)


'''
 属性的访问
'''
emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empCount

'''
 添加删除修改类的属性
'''
#添加一个属性
emp1.age = 7
#修改一个属性
emp2.age = 8
#删除一个属性
del emp1.age
#检查时候含有属性
hasattr(emp1, 'age')
#获取属性的值
getattr(emp1, 'age')
#添加属性
setattr(emp1, 'age', 8)
#删除属性
delattr(emp1, 'age')



