# -*- coding:utf-8 -*-

from collections import OrderedDict
import json
d = OrderedDict()

d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
print(d['foo'])
for key in d:
    print(key, d[key])


b = json.dumps(d) 
print(b)
print(type(b))
