from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,SelectField,FileField,TextAreaField,IntegerField

"""
登录表单:
1. 账号
2. 密码
3. 登录按钮
"""
from wtforms.validators import DataRequired, EqualTo, ValidationError
from film.models2 import User
class LoginForm(FlaskForm):
    account = StringField(
        label=u"账号",
        validators=[DataRequired(u"账号不能为空")],
        description=u"账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号!"
        }
    )
    pwd = PasswordField(
        label=u"密码",
        validators=[DataRequired(u"密码不能为空")],
        description=u"密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码!"
        }
    )
    submit = SubmitField(
        u"登录",
        render_kw={
            "class": "btn btn-primary"
        }
    )
    '''def validate_account(self, field):
        account = field.data
        user = User.query.filter_by(account=account).first()
        print(user)
        if not user:
            raise ValidationError(u"账号不存在")'''
    def validate_pwd(self, field):
        pwd = field.data
        #print(self.account)
        account = self.account.data
        user = User.query.filter_by(account=account).first()
        #print(user)
        if not user:
            raise ValidationError(u"账号或密码错误")
        user = User.query.filter_by(account=self.account.data).first()
        if not user.check_pwd(pwd):
            raise ValidationError(u"账号或密码错误")


from wtforms.validators import DataRequired, EqualTo, ValidationError
from film.models2 import User

class RegisterForm(FlaskForm):
    account = StringField(
        validators=[DataRequired(u"账号不能为空")],
        description=u"账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号"
        }
    )
    pwd = PasswordField(
        validators=[DataRequired(u"密码不能为空")],
        description=u"密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码"
        }
    )
    re_pwd = PasswordField(
        validators=[DataRequired(u"密码不能为空"),EqualTo('pwd',message=u'两次密码不一致')],
        description=u"确认密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请确认密码"
        }
    )

    captcha = StringField(
        validators=[],
        description=u"验证码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入验证码"
        }
    )
    submit = SubmitField(
        u"注册",
        render_kw={
            "class": "btn btn-primary"
        }
    )

    def validate_account(self, field):
        account = field.data
        user = User.query.filter_by(account=account).count()
        if user > 0:
            raise ValidationError(u"账号已存在")

    def validate_captcha(self, field):
        captcha = field.data
        from flask import session
        if not session["captcha"]:
            raise ValidationError(u"非法操作")
        if session["captcha"].lower() != captcha.lower():
            raise ValidationError(u"验证码不正确")
    '''原验证码校验，不清楚form_session的导包，替换为flask的导包session
        def validate_captcha(self, field):
            captcha = field.data
            if not form_session["captcha"]:
                raise ValidationError(u"非法操作")
            if form_session["captcha"].lower() != captcha.lower():
                raise ValidationError(u"验证码不正确")
    '''
class ArticleAddForm(FlaskForm):
    title = StringField(
        validators=[
            DataRequired(u"内容不能为空")
        ],
        description=u"标题",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入标题"
        }
    )
    # 强制类型为整型
    category = SelectField(
        validators=[
            DataRequired(u"分类不能为空")
        ],
        description=u"分类",
        choices=[(1, u"科技"), (2, u"搞笑"), (3, u"军事")],
        default=3,
        coerce=int,
        render_kw={
            "class": "form-control"
        }
    )
    logo = FileField(
        validators=[],
        description=u"封面",
        render_kw={
            "class": "form-control-file",
        }
    )
    content = TextAreaField(
        validators=[
            DataRequired(u"内容不能为空")
        ],
        description=u"内容",
        render_kw={
            "style": "height:300px;",
            "id": "content"
        }
    )
    submit = SubmitField(
        u"发布文章",
        render_kw={
            "class": "btn btn-primary"
        }
    )

class ArticleEditForm(FlaskForm):
    id = IntegerField(
        validators=[
            DataRequired(u"内容不能为空")
        ],

    )
    title = StringField(
        validators=[
            DataRequired(u"内容不能为空")
        ],
        description=u"标题",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入标题"
        }
    )
    # 强制类型为整型
    category = SelectField(
        validators=[
            DataRequired(u"分类不能为空")
        ],
        description=u"分类",
        choices=[(1, u"科技"), (2, u"搞笑"), (3, u"军事")],
        default=3,
        coerce=int,
        render_kw={
            "class": "form-control"
        }
    )
    logo = FileField(
        validators=[],
        description=u"封面",
        render_kw={
            "class": "form-control-file",
        }
    )
    content = TextAreaField(
        validators=[
            DataRequired(u"内容不能为空")
        ],
        description=u"内容",
        render_kw={
            "style": "height:300px;",
            "id": "content"
        }
    )
    submit = SubmitField(
        u"发布文章",
        render_kw={
            "class": "btn btn-primary"
        }
    )