from urllib.request import urlopen
from bs4 import BeautifulSoup #解析数据为dom结构对象


html = urlopen("http://www.baidu.com")
#html = urlopen("http://www.pythonscraping.com/pages/page1.html")

#print(html.read())
bsObj = BeautifulSoup(html.read(),"html.parser")
#print(bsObj.h1)
#print(html.read())
#print(bsObj.html.body.img)
