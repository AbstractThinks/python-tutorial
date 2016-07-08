##debug

####错误处理

```python

# try...except...finally...

# 例：

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')



```

####assert和logging

```python

def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('0')

main()

##凡是用print来辅助查看的地阿芳都可以用断言(assert)来代替

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

##若断言为false会抛出AssertionError

 ##python3 -O err.py关闭断言功能


import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)


输出
>>>$ python3 err.py
>>>INFO:root:n = 0
>>>Traceback (most recent call last):
>>>  File "err.py", line 8, in <module>
>>>    print(10 / n)
>>>ZeroDivisionError: division by zero


##logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
##当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
##这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
```


