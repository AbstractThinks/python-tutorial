import urllib.request

url = "http://www.baidu.com"
obj = urllib.request.urlopen(url)
type(obj)
url_data = obj.geturl()

info_data = obj.info()

code_data = obj.getcode()

read_data = obj.read().decode('UTF-8')


print(url_data)
print("/n")
print(info_data)
print("/n")
print(code_data)
print("/n")
print(read_data)
