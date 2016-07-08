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
