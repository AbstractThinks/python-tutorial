[wsgi理解参考](http://blog.csdn.net/sraing/article/details/8455242)

wsgi服务器主要实现
>
> 1.接受HTTP请求
> 2.解析HTTP请求
> 3.发送HTTP响应

WSGI server的工作仅仅是将从客户端收到的请求传递
给WSGI application，然后将WSGI application的返回值
作为响应传给客户端
