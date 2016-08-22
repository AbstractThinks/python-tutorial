# -*- coding:utf-8 -*-

a_string = "this is global variable"
a_string2 = "this is global varibale2"

def foo():
    a_string = "this variable is in function"
    print "foo: " + a_string
def foo2():
    print "foo2: " + a_string

def outer(some_func):
    def inner():
        print "before some_func"
        ret = some_func()
        return ret+1
    return inner

def fooOuter():
    return 1

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
    foo()
    foo2()
    
    decorated = outer(fooOuter)
    decorated()

    decoratedTester(5,6)
    decoratedTester2(9,{"name":"e"})
