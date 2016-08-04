##数据类型和变量

|常规类型|布尔运算符|空值|常量|
|---|---|---|---|
|整形<br>浮点型<br>字符串<br>布尔值（True，False）|and<br>or<br>not<br>|None|全大写字母为`约定`常量|

|list|tuple|
|----|----|
|定义：使用中括号`[]`定义数组<br>例：['1','hello']|定义：使用小括号`()`定义元祖<br>例：（1,2,3）<br>不可变的数组|

|dict|set|
|---|---|
|字典类型：dict = {'key':value}|管理一个不可重复元素的列表|
|dict.get(key)|联合(\\)<br>交(&)<br>差(-)<br>对称差集(^)|


##循环

```python
#代码段落需要严格缩进
if condition :
    block
elif condition :
    block
else :
    block
    
#可以生成从0到number-1的list
range(number)

#for循环
for item in list ：
    block
    
#while循环
while condition :
    block
```

##函数

```python
1.空函数： pass
2.类型检查：python是类型不安全的，所以可以通过isinstance(var,(type1, type2))来检查类型
3.返回多个值，使用tuple。不可以省略括号
4.默认值：def method(arg = 'arg')
5.可变参数:def method(*var_arg), 其中var_arg是一个tuple,可以使用for...in..来遍历
6.关键字参数：def method(**key), 关键字参数不限制传入的参数个数和类型，会在函数内部组合成一个dict
7.参数组合：

 def test(x,y=5,*a,**b):
     print x,y,a,b
 #test(1,2) ===> 1 2 () {}
 #test(x=1,y=1,a=1)   ===> 1 1 () {'a':1}
 #test(1,2,3,4,k=1,t=2,o=3) ===> 1 2 (3,4) {'k':1,'t':2,'o':3}
 
8.递归函数
```

##高级特性
|切片|迭代|列表生成器|生成器|
|---|---|---|---|
|arr[0:3]:表示从第0个元素开始，取3个|迭代即使用:for item in arr, arr可以是数组，字典或者字符串|列表生成使用range(start,end)函数。[]|如果你需要一组序列，但是太大，占用内存过多。那么可以使用生成器，它是实时计算的列表。|
|arr[-3:-1]:表示取倒数第三，第二个元素,-1表示最后一个|判断是否可以迭代isinstance(object, Iterable)|混合生成使用简写for...in...迭代|将列表生成表达式的[]变为()即可|
|arr[::5]:每5个取一个元素|迭代dict: for key in dict遍历key。for value in dict.itervalues()遍历value；for k, v in dict.iteritems()遍历key和value||可以将一个函数变成一个生成器，只需要添加yield item语句即可，生成器会在遇到yield的时候返回对应结果，下次next从上次yield之后开始执行。|
|字符串也可以切片||||
 

##with

```python
//传统写法
try:
    f = open('xxx')
except:
    print 'fail to open'
    exit(-1)
try:
    do something
except:
    do something
finally:
    f.close()


//with语句写法

try:
    with open( "a.txt" ) as f :
        do something
except xxxError:
    do something about exception


//with语句说明
class A:  
    def __enter__(self):  
        print 'in enter'  
    def __exit__(self, e_t, e_v, t_b):  
        print 'in exit'  
  
with A() as a:  
    print 'in with'  
  
>>> in enter  
>>> in with  
>>> in exit  

```
