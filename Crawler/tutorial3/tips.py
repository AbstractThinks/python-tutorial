#python2.7

import urllib2
import urllib

#get
url = "http://www.baidu.com"
resp = urllib2.urlopen(url)
data = resp.read()
print(data)


#post

url_post = "http://www.baidu.com"
form = {'name':'abc','psd':'1234'}
form_data = urllib.urlencode(form)
req = urllib2.Request(url, form_data)
rep = urllib2.urlopen(req)
data_post = rep.read()
print(data_post)
