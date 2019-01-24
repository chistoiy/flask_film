from film import db,create_app
app = create_app()
app_ctx = app.app_context() # app_ctx = film/g
with app_ctx: # __enter__,通过LocalStack放入Local中
    #db.create_all(bind=None)
    #db.create_all(bind=['movie'])
    #db.drop_all(bind=['movie'])
    #db.create_all(bind=['artcms'])
    #db.drop_all(bind=None)
    db.create_all()
    #db.drop_all()
    """
        测试后，如果多个连接，可以分为这两个属性配置
        app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:chis1chang@127.0.0.1:3306/movie?charset=utf8"
        app.config['SQLALCHEMY_BINDS'] = {
        'artcms': 'mysql+pymysql://root:chis1chang@127.0.0.1:3306/artcms?charset=utf8',
        #'movie':"mysql+pymysql://root:chis1chang@127.0.0.1:3306/movie?charset=utf8",
    }
    SQLALCHEMY_DATABASE_URI为主连接，可以不设置，但是不设置时，会导致create_all出错，需要指定bind对象
    SQLALCHEMY_BINDS 为关联连接方式，
        其关联的表需要表内添加一个__bind_key__ = 'artcms'属性，即关联对象为artcms，不一定是数据库artcms，artcms为关联字典的key
    
    情景一：
        一个主连接，多个关联，此时：
            create_all不指定内容，则为全部创建，指定bind=['artcms']，则只创建artcms连接的数据表，对主连接而言
                则设置bind=none
                drop_all一样
    情景二：
        不设置主连接，
            测试，create_all必须指定bind对象，否则连接池出错
            drop_all一样
    
    问题：
        如果多个数据库需要创建的模型表重名如何解决？
        最好的解决办法就是，在重复的模型表上添加属性，指定其绑定的数据库名
        __table_args__ ={'schema': 'artcms'}
    """