import functools


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#1.先执行log('execute'),返回decorator函数
#2.执行decorator函数,返回wrapper函数

@log('execute')
def now():
    print('2015-06-23')

now()


def log1(func):
#由于返回的wrapper函数的名字就是'wrapper'
#所以需要把原始函数的__name__等属性复制到wrapper
#python内置函数库functools.wraps
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' %func.__name__)
        return func(*args, **kw)
    return wrapper


