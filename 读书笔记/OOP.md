

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
