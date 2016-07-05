def now():
    print('2015-3-25')


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' %func.__name__)
        return func(*args, **kw)
    return wrapper

# 把@log放在函数定义处相当于执行了now1 = log(now1)
# now变量指向了新函数wrapper

@log
def now1():
    print('2015-3-25')

now1()




