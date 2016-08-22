# -*- coding: utf-8 -*-

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='abcd,1234.', charset='utf8')

# cur = conn.connect()
cur = conn.cursor()

#创建数据表
# cur.execute("CREATE DATABASE dataTest")
cur.execute("USE python_test")
# cur.execute("CREATE TABLE student(id INT, name VARCHAR(20), class VARCHAR(30), age VARCHAR(10)")
#=============================================================
# #纯sql语句操作
#
#
# #插入数据
# cur.execute("insert into student values('2', 'Jesse', '3 year 2 class', '9')")
#
# #============================================================
#
#
# #============================================================
# #开发写法
#
# #插入数据
#
# sqli = "insert into student values(%s, %s, %s, %s)"
# #插入一条数据
# cur.execute(sqli,('3','alvin', '3 year 1 class', '7'))
# #插入多条数据
# cur.executemany(sqli, [
#     ('4','fen', '1 year 1 class', '6'),
#     ('4', 'leslie', '1 year 1 class', '7')
# ])
#
#
# #============================================================
#
# #修改数据
# cur.excute("update student set class = '3 year 1 class' where name = 'Jesse'")
#
# #删除查询条件
# cur.execute("delete from student where age = '9'")
#
# #查询数据, 获取student表数据的总条数
aa = cur.execute("select * from user_test")
print(aa)
#
# # 遍历表中数据
info = cur.fetchmany(aa)
for ii in info:
    print(ii)















cur.close()
conn.commit()
conn.close()
