from . import home
from flask import render_template,redirect,url_for,request

@home.route("/")
def index():
    return "<h1 style='color:red'>this is home</h1>"
from functools import wraps
def user_login_req(f):
    @wraps(f)
    def login_req(*args,**kwargs):
        if "user" not in session:
            return redirect(url_for('home.login', next=request.url ))
        return f(*args,**kwargs)
    return login_req


from .forms import LoginForm
@home.route("/login/",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        session["user"] = data["account"]
        flash("登录成功", "ok")
        return redirect("/art/list/1/")
    return render_template('login.html',title='登录',form=form)

@home.route("/logout/",methods=["GET"])
@user_login_req
def logout():
    session.pop("user", None)
    return redirect("/login/",)



from .forms import RegisterForm
from film.models2 import User
from werkzeug.security import generate_password_hash
from datetime import datetime
from film import db
from flask import flash
@home.route("/register/",methods=["GET","POST"])
def register():
    #print('你好')
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        print(data)
        user = User(
            account=data["account"],
            # 对于pwd进行加密
            pwd=generate_password_hash(data["pwd"]),
            add_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
        db.session.add(user)
        db.session.commit()
        flash("注册成功！","ok")
        return redirect('/art/list/')

    return render_template("register.html", title="注册", form=form,session=session)



from .forms import ArticleAddForm
from werkzeug.utils import secure_filename

from film.models2 import Article
@home.route("/art/add/",methods=["GET","POST"])
@user_login_req
def art_add():
    form = ArticleAddForm()
    if form.validate_on_submit():
        data = form.data
        #print('aaa',data)
        from flask import current_app
        # print(current_app.static_folder)
        file = secure_filename(form.logo.data.filename)
        logo = change_name(file)
        #print('logo type',type(logo),logo)
        if not os.path.exists(current_app.config["uploads"]):
            os.makedirs(current_app.config["uploads"])
        #print('pahtht:::::',type(current_app.config["uploads"]))
        # 保存文件
        pa = os.path.join(current_app.config["uploads"], logo)
        print('pahtht:::::',pa)
        form.logo.data.save(pa)
        # 获取用户ID
        user = User.query.filter_by(account=session["user"]).first()
        user_id = user.id
        # 保存数据，Article
        article = Article(
            title=data["title"],
            category=data["category"],
            user_id=user_id,
            logo=logo,
            content=data["content"],
            add_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
        db.session.add(article)
        db.session.commit()
        flash(u"发布文章成功", "ok")
    return render_template("art_add.html",title="发布文章",form=form)
from .forms import ArticleEditForm
@home.route("/art/edit/<int:id>/",methods=["GET","POST"])
@user_login_req
def art_edit(id):
    form = ArticleEditForm()
    article = Article.query.get_or_404(int(id))
    #print(article.id)
    if request.method == "GET":
        form.content.data = article.content
        form.category.data = article.category
        # 莫名其妙赋初值:不赋初值表单提交时会提示封面为空
        # 放在这里修复显示请选择封面的错误
    #form.logo.data = article.logo
    #print('data>>>>>',form.data,'logo>>>',)
    if form.validate_on_submit():
        data = form.data
        # 上传logo
        print('sss',form.logo.data,type(form.logo.data))
        if form.logo.data:

            file = secure_filename(form.logo.data.filename)
            #print('llll')
            logo = change_name(file)

            from flask import current_app
            if not os.path.exists(current_app.config["uploads"]):
                os.makedirs(current_app.config["uploads"])

            # 保存文件
            pa = os.path.join(current_app.config["uploads"], logo)
            #print('pahtht:::::', pa)
            form.logo.data.save(pa)
            article.logo = logo

        article.title = data['title']
        article.content = data['content']
        article.category = data['category']
        db.session.add(article)
        db.session.commit()
        flash(u"编辑文章成功", "ok")
        return redirect('art/list/1')
    return render_template("art_edit.html", form=form, title="编辑文章", article=article)

@home.route("/art/list/<int:page>/",methods=["GET"])
def art_list(page):
    if page is None:
        page = 1
        # 只展示当前用户才能看到的内容
    user = User.query.filter_by(account=session["user"]).first()
    user_id = user.id
    page_data = Article.query.filter_by(
        user_id=user_id
    ).order_by(
        Article.add_time.desc()
    ).paginate(page=page, per_page=1)

    category = [(1, u"科技"), (2, u"搞笑"), (3, u"军事")]
    return render_template("art_list.html", title="文章列表", page_data=page_data, category=category)
    #return render_template("art_list.html", title="文章列表", page_data=page_data)


@home.route("/art/del/<int:id>",methods=["GET"])
@user_login_req
def art_del(id):
    article = Article.query.get_or_404(int(id))
    db.session.delete(article)
    db.session.commit()
    flash("删除《%s》成功!" % article.title, "ok")
    return redirect("/art/list/1")


# 验证码
from flask import session, Response
@home.route("/captcha/", methods=["GET"])
def captcha():
    from film.util.catpcha  import Captcha
    import os
    c = Captcha()
    info = c.create_captcha()
    '''
    原设计catpcha()生成验证码并保存成jpeg格式文件，现在修改为该函数传递过来二进制图片流
    image = os.path.join('film/util/', "static/captcha") + "/" + info["image_name"]
    with open(image, 'rb') as f:
        image = f.read()
    return Response(image, mimetype="jpeg")
    '''
    session['captcha'] = info["captcha"]
    return Response(info['image_2'])


from werkzeug.utils import secure_filename
import os ,uuid
# 设置上传封面图路径
# 修改文件名称
def change_name(name):
    info = os.path.splitext(name)
    # 文件名: 时间格式字符串+唯一字符串+后缀名
    name = datetime.now().strftime("%Y%m%d%H%M%S")+str(uuid.uuid4().hex)+info[-1]
    return name
import json,re

@home.route('/upload/', methods=['GET', 'POST'])
def upload():
    from flask import current_app
    #print(current_app.static_folder)
    action = request.args.get('action')
    with open(os.path.join(current_app.static_folder, 'ue', 'php','config.json')) as fp:
        try:
            # 删除 `/**/` 之间的注释
            CONFIG = json.loads(re.sub(r'\/\*.*\*\/', '', fp.read()))
        except:
            CONFIG = {}

    if action == 'config':
        # 初始化时，返回配置文件给客户端
        result = CONFIG

    return json.dumps(result)

