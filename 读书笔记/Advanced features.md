|切片|迭代|列表生成式|生成器|迭代器|
|----|----|----------|------|------|
|取一个list或tuple的部分元素|如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。|创建list的生成式|在Python中，这种一边循环一边计算的机制，称为生成器：generator。|可以被next()函数调用并不断返回下一个值的对象称为迭代器|

###切片

|代码|解释|
|----|----|
|`L[0:3]`|从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。|
|`L[:3]`|如果第一个索引是0,可以省略|
|`L[-2:]`|  取倒数两个元素|
|`L[-2:-1]`| 取倒数第二个元素|
|`L[-1]`|    取倒数第一个元素|
|`L[:10:2]`| 前10个数，每两个取一个|
|`L[::5]`|   所有数，每5个取一个|
|`[:]`| 所有数|

###迭代

|默认迭代|迭代键值对|
|--------|----------|
|```for value in d.values()```|`for k, v in d.items()`| 

|判断是否可以迭代<br>isinstance(L, Iterable)|enumerate(L)|
|--------|----------|
|`isinstance('abc', Iterable)`|Python内置的enumerate函数可以把一个list变成索引-元素对<br>`for i, value in enumerate(['A', 'B', 'C'])`|


###列表生成式

```python
 list(range(1, 11))
 >>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
  L = []
  for x in range(1, 11):
    L.append(x * x)
  >>> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
  
   [x * x for x in range(1, 11)]
   >>> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
 
```

###生成器

```python
只要把一个列表生成式的[]改成()

g = (x * x for x in range(10))
 >>> <generator object <genexpr> at 0x1022ef630>
 
如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值

首选用for循环遍历生成器，可以避免StopIteration错误```python

g = (x * x for x in range(10))
for n in g:
     print(n)
     
```

###迭代器

```python
生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

把list、dict、str等Iterable变成Iterator可以使用iter()函数：

isinstance(iter('abc'), Iterator)

这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
```






     
