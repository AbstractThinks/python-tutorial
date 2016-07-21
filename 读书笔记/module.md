##引入包
> import module 
> 调用：module.functionName
> 
> 
> from module import functionName 
> form module import a, b, c
> from module import *
> function和变量直接导入到本地空间去，可以直接使用。
> 块的所有公共对象(public objects)都被导入到当
> 前的名称空间，也就是任何只要不是以”_”开始的东西都会被导入
> 
> 程序中必须使用完整名称，即通过package.module使用，
> 如果只导入package而不导入module，那么只有package中定义的
> __init__.py模块中的内容可用（使用该模块中的内容需加上包名）
> 
> 
> 
> 
>



##一个.py文件就称之为一个模块（Module）


一个<font color= CornflowerBlue size=4>abc.py</font>的文件就是一个名字叫<font color= CornflowerBlue size=4>abc</font>的模块

![](../img/module2.png)

```python
abc.py模块的名字就变成了mycompany.abc
每一个包目录下面都会有一个__init__.py的文件，
这个文件是必须存在的，否则，Python就把这个目录当成普通目录，
而不是一个包。__init__.py可以是空文件，也可以有Python代码，
因为__init__.py本身就是一个模块，而它的模块名就是mycompany。
```

![](../img/module1.png)

```python
文件www.py的模块名就是mycompany.web.www，
两个文件utils.py的模块名分别是mycompany.utils和mycompany.web.utils。

自己创建模块时要注意命名，不能和Python自带的模块名称冲突。
```
