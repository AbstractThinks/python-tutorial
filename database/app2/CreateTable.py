# -*- coding: utf-8 -*-

from sqlalchemy import Column, Table, String, Integer, MetaData, ForeignKey, create_engine
from sqlalchemy.orm import  sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql+pymysql://root:abcd,1234.@localhost:3306/test', echo=True)
metadata = MetaData(engine)

user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(20)),
             Column('fullname', String(40))
             )
metadata.create_all()



