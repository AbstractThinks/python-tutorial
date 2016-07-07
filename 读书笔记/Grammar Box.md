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
