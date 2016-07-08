

<table>
  <tr>
    <th>
      __slots__
    </th>
    <th>
      @property
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
  </tr>
  <tr>
    <td>
      若只允许对Student实例添加name和age属性。<br>
      在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
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
