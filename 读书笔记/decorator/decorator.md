


```python
python解释器会先查找本地作用域是否含有变量a_string，当
本地作用域里面找不到，就会去上层的作用域里面查找

a_string = "this is global variable"

def foo():
    a_string = "this variable is in function"
    print "foo: " + a_string
def foo2():
    print "foo2: " + a_string
    
if __name__ == "__main__":
    foo()
    foo2()   
    
>>> this variable is in function
>>> this is global variable

```

```python
装饰器：
先将函数decoratedTester传入logger函数并执行
返回inner函数并复值给变量decoratedTester

def logger(func):
    def inner(*args, **kwargs):
        print "Arguments were: %s, %s" % (args, kwargs)
        return func(*args, **kwargs)
    return inner
    
@logger
def decoratedTester(x, y=1):
    print "the value is %s" % (x*y)
    return x*y

@logger
def decoratedTester2(x=1,y={}):
    print x
    
if __name__ == "__main__":
	decoratedTester(5,6)
   decoratedTester2(9,{"name":"e"})
   
 >>> Arguments were: (5, 6), {}
 >>> the value is 30
 >>> Arguments were: (9, {'name': 'e'}), {}
 >>> 9


```