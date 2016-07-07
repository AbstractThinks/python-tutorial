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
