#测试pymysql连接数据库
'''import pymysql
conn = pymysql.connect('127.0.0.1','root','chis1chang',database='movie')
cursor = conn.cursor()
sql = "select * from role "
ret = cursor.execute(sql)
ret = cursor.fetchall()
print(ret)
'''

#测试sqlalchemy+pymysql是否正常
'''
from sqlalchemy import create_engine,Column,Integer,String,Integer
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:chis1chang@127.0.0.1:3306/movie?charset=utf8')

Base = declarative_base()
#sqlalchemy本身无法对已经建立的表进行修改，只存在新建，删除
#数据表类
class User(Base):
    __tablename__='users'
    id = Column(Integer,primary_key=True)
    username =Column(String(64),)
    pwd=Column(String(64),)

#新建数据表，如果当前表已经建立，则不会产生效果，
def create_all():
    engine = create_engine('mysql+pymysql://root:chis1chang@127.0.0.1:3306/movie?charset=utf8')
    Base.metadata.create_all(engine)
create_all()
'''

#测试flask_sqlalchemy 连接多个数据库的去写操作
'''
from film import db,create_app
app = create_app()
app_ctx = app.app_context() # app_ctx = film/g
with app_ctx:


    #from film.models import  User
    from film.models2 import User
    from datetime import datetime
    #db.session.add(User(account='zhang3',pwd='nihaoa',add_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),))
    #db.session.commit()
    ret = db.session.query(User).all()
    print(ret)
'''
from film import db,create_app
app = create_app()
app_ctx = app.app_context() # app_ctx = film/g
with app_ctx:


    #from film.models import  User
    from film.models2 import User
    from datetime import datetime

    user = User.query.filter_by(account='a').count()
    print(user)