# -*- coding:utf-8 -*-
#
#将序列分解为单独的变量

p = (4, 5)

x, y = p

print x
print y

data = ['name', 50, 91.1, (2019, 12, 21)]
name, share, price, date = data
name1, share1, price1, (year, month, day) = data

print "name: "+name
print "share: "+str(share)
print "price: "+str(price)
print "date: "+str(date)

print "name1: "+name1
print "share1: "+str(share1)
print "price1: "+str(price1)
print "year: "+str(year)
print "month: "+str(month)
print "day "+str(day)


#如果元素的数量不匹配，将得到一个错误提示

#m, n = data
#print m
#print n

#可以通过'_'代替变量取值
_, m, n, _ = data
print m
print n

