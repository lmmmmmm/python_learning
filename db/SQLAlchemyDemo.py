from sqlalchemy import column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# 初始化数据库连接:
# echo 为True 会显示过程
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test-shiro', echo=True)


class User(Base):
    __tablename__ = 'user'

    id = column(Integer)
    username = column(String(32))
    password = column(String(64))


if __name__ == '__main__':
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
