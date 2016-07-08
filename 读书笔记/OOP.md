

<table>
  <tr>
    <th>
      __slots__
    </th>
    <th>
      @property
    </th>
    <th>
      多重继承
    </th>
    <th>
      定制类
    </th>
    <th>
      枚举类
    </th>
    <th>
      元类
    </th>
  </tr>
  <tr>
    <td>
      动态绑定允许我们在程序运行的过程中动态给class加上功能
    </td>
    <td>
    把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    </td>
    <td>
      <pre>
class Mammal(Animal):
    pass
    
class Runnable(object):
    def run(self):
        print('Running...')
        
class Dog(Mammal, Runnable):
    pass
        
      </pre>
    </td>
    <td>
    </td>
    <td>
    </td>
    <td>
      metaclass
      type
    </td>
  </tr>
  <tr>
    <td>
      若只允许对Student实例添加name和age属性。<br>
      在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
      __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    </td>
    <td>
    <pre>
    
    class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
        
    </pre>
    </td>
  </tr>
  <tr>
    <td>
<div class="highlight highlight-source-python">
<pre>

class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

>>> s = Student() # 创建新的实例
>>> s.name = 'Michael' # 绑定属性'name'
>>> s.age = 25 # 绑定属性'age'
>>> s.score = 99 # 绑定属性'score'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'

</pre>
</div>

    </td>
  </tr>
</table>


##元类

#####type(类名, 父类的元组（可以为空）, 属性的字典)
```python

一切皆是对象
一切皆是对象
一切皆是对象

Class C(object):
  pass
c = C()
print c.__class__
print C.__class__

>>> <class '__main__.C'>
>>> <class 'type'>

type(类名, 父类的元组（可以为空）, 属性的字典)

def  printInfo(self):
    print "%s is %d years old" %(self.name, self.age)

S = type("Student", (object, ), {"name": "Wilber", "age": 28, "printStudentInfo": printInfo})

print type(S)             >>> <type 'type'>
s = S()
print type(s)             >>> <class '__main__.Student'>
s.printStudentInfo()      >>> Wilber is 28 years old

```
#####__metaclass__

___元类就是用来创建类的"模板",元类就是类的类___

1. `Python解释器会在当前类中查找"__metaclass__"属性对于的代码，然后创建一个类对象`
2. `如果没有找到"__metaclass__"属性，会继续在父类中寻找"__metaclass__属性"，并尝试前面同样的操作`
3. `如果在任何父类中都找不到"__metaclass__"，就会用内置的type来创建这个类对象`

```python

def queueMeta(name, bases, attrs):
    attrs['InQueue'] = lambda self, value: self.append(value)
        
    def deQueue(self):
        if len(self) > 0:
            return self.pop(0)
    attrs['DeQueue'] = deQueue
    
    # 直接调用type内建函数
    return type(name, bases, attrs)


# 元类从`type`类型派生
class QueueMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['InQueue'] = lambda self, value: self.append(value)
        
        def deQueue(self):
            if len(self) > 0:
                return self.pop(0)
        attrs['DeQueue'] = deQueue
        
        # 直接调用type内建函数
        # return type(name, bases, attrs)
        
        # 通过父类的__new__方法
        return type.__new__(cls, name, bases, attrs)

class MyQueue(list):
    # 设置metaclass属性，可以使用一个函数，也可以使用一个类，只要是可以创建类的代码
    #__metaclass__ = queueMeta
    __metaclass__ = QueueMetaclass
    pass
    

q = MyQueue("hello World")
print q
q.InQueue("!")
print q
q.DeQueue()
print q

1. 拦截类的创建
2. 根据"__metaclass__"对应的代码修改类
3. 返回修改之后的类

```

```python

class MyMetaclass(type):
    def __new__(meta, name, bases, attrs):
        print '-----------------------------------'
        print "Allocating memory for class", name
        print meta
        print bases
        print attrs
        return super(MyMetaclass, meta).__new__(meta, name, bases, attrs)
    
    def __init__(cls, name, bases, attrs):
        print '-----------------------------------'
        print "Initializing class", name
        print cls
        print bases
        print attrs
        super(MyMetaclass, cls).__init__(name, bases, attrs)

class MyClass(object):
    __metaclass__ = MyMetaclass

    def foo(self, param):
        pass

barattr = 2   

```

"__call__"是另外一个经常在实现元类时被重写的方法，与"__init__"和"__new__"不同的是，当调用"__call__"的时候，类已经被创建出来了，"__call__"是作用在类创建的实例过程。

```python

class MyMetaclass(type):
    def __call__(cls, *args, **kwds):
        print '__call__ of ', str(cls)
        print '__call__ *args=', str(args)
        return type.__call__(cls, *args, **kwds)

class MyClass(object):
    __metaclass__ = MyMetaclass

    def __init__(self, a, b):
        print 'MyClass object with a=%s, b=%s' % (a, b)

print 'gonna create foo now...'
foo = MyClass(1, 2) 

```
  

