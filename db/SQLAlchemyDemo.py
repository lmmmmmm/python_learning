from sqlalchemy import column, String, INT, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import *

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = column(mysql.INTEGER, primary_key=True)
    username = column(String(32))
    password = column(String(64))


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test-shiro')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
session = DBSession()
# TODO 解决column() got an unexpected keyword argument 'primary_key'问题

new_user = User(username='Bob', password='123')
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
