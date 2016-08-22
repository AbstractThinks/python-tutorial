# -*- coding: utf-8 -*-
import os

#激活跨站点请求伪造保护
CSRF_ENABLED = True
SECRET_KEY = 'jesse'

basedir = os.path.abspath(os.path.dirname(__file__))

#Flask-SQLAlchemy扩展需要,储存数据库文件的路径
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

#文件夹,SQLAlchemy-migrate数据文件存储的位置
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')