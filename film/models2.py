from film import db

"""
用户模型
0. id编号
1. 账号
2. 密码
3. 注册时间
"""

from sqlalchemy import MetaData
class User(db.Model):

    __bind_key__ = 'artcms'
    __tablename__ = "user"
    #metadata = MetaData()
    __table_args__ ={'schema': 'artcms'}
    # {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号id
    account = db.Column(db.String(20), nullable=False)  # 账号非空
    pwd = db.Column(db.String(100), nullable=False)  # 密码非空
    add_time = db.Column(db.DateTime, nullable=False)  # 注册时间

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)
    # 查询时的返回
    def __repr__(self):
        return "<User %r>" % self.account


"""
文章模型
0. id编号
1. 标题
2. 分类
3. 作者
4. 封面
5. 内容
6. 发布时间
"""


class Article(db.Model):
    __tablename__ = "article"
    __bind_key__ = 'artcms'
    id = db.Column(db.Integer, primary_key=True)  # 编号id
    title = db.Column(db.String(100), nullable=False)  # 标题非空
    category = db.Column(db.Integer, nullable=False)  # 编号id
    user_id = db.Column(db.Integer, nullable=False)  # 作者
    logo = db.Column(db.String(100), nullable=False)  # 封面
    content = db.Column(db.Text, nullable=False)  # 内容
    add_time = db.Column(db.DateTime, nullable=False)  # 发布时间

    # 查询时的返回
    def __repr__(self):
        return "<Article %r>" % self.title