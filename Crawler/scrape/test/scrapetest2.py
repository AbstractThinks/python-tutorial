from urllib.request import urlopen
from urllib.error import HTTPError

from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
        return title
    except AttributeError as e:
        return None

if __name__ == '__main__':
   # value = getTitle("http://www.pythonscraping.com/pages/page1.html")
    value = getTitle("http://www.baidu.com")
    if value == None:
        print("title colud not be found")
    else:
        print(value)
