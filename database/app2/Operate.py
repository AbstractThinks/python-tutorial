# -*- coding: utf-8 -*-

from sqlalchemy import Column, Table, String, Integer, MetaData, ForeignKey, create_engine
from sqlalchemy.orm import  sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import random

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    fullname = Column(String(40))

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:abcd,1234.@localhost:3306/test', echo=True)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 获取session对象
session = DBSession()
# 创建新user对象
new_user = User(id=5, name='jesse', fullname='jessezhuang')
# 添加到session
# session.add(new_user)

# 插入多条数据
# session.execute(User.__table__.insert(), [{'id': i, 'name':'jesse{0}'.format(i), 'fullname':''} for i in range(200, 300)]);

# 创建Query查询,filter是where条件,最后调用one()返回唯一行,如果调用all()则返回所有行
# printuser = session.query(User).filter(User.id == 5).one()
# print(printuser.name)

# # 遍历查询返回结果
# printuserall = session.query(User)
# for user in printuserall:
#     print(user.name)



# 修改数据
# updateuser = session.query(User).filter(User.name == 'jesse200').update({User.name : 'Alvin'})

# 删除数据
# deleteuser1 = session.query(User).filter(User.name == 'jesse201').one()
# session.delete(deleteuser1)
# session.query(User).filter(User.name == 'jesse202').delete()


# 提交保存到数据库
session.commit()
# 关闭session
session.close()