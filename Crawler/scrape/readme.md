#安装scrapy

```python
#安装scrapy
sudo pip install scrapy --ignore-installed six

sudo pip uninstall six
sudo easy_install six


#检查是否安装成功
scrapy --version
```


#创建scrapy项目

```python
scrapy startproject 项目名称
```

启动scrapy项目

```python

scrapy crawl 模块

或

scrapy crawl 别名
(参考wikiSpider/wikiSpider/spiders/articleSpider.py模块中ArticleSpider中name属性)
```



# xpath规则

|表达式|描述|例子|
|---|---|---|
|nodename|选取此节点的所有子节点。||
| / |从根节点选取| /html/head/title: 选择HTML文档<head>元素下面的<title> 标签。<br> /html/head/title/text(): 选择前面提到的<title> 元素下面的文本内容|
| // |从匹配选择的当前节点选择文档中的节点,而不考虑他们的位置|选择所有 <td> 元素|
| . |选取当前节点||
| .. |选取当前节点的父节点||
| @ |选取属性| //div[@class="mine"]: 选择所有包含 class="mine" 属性的div 标签元素|


