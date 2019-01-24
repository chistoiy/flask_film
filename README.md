# flask_film
a website for film developed by flask

# [阶段版本一](https://github.com/chistoiy/flask_film/tree/3d25a5608ced63ad7af61ee4ff78c8826ff87a49)

主要内容为:
1. 新建两个model,同时使用了flask_sqlalchemy连接两个数据库(使用主连接和关联方式)时的读写操作，在项目初始化时，先执行create_db.py,用于初始化数据库，配置放置于film/__init__.py；对于这两个model，只使用model2(用户及文章表)
2. 使用两个蓝图：admin/home，其中本阶段只是用到了home：
> *   主要路由：  
/ 根目录，项目测试阶段使用  
/login 用户登录    
/logout 用户登出  
/register 注册  
/captcha/ 注册时验证码访问地址  
/art/list/1 文章列表  
/art/add 新建文章  
/upload/ 文章写作时使用的富文本编辑器ueditor，该插件需要后台传递参数  
/art/edit/[id] 编辑文章  
/art/del/[id] 删除文章  


涉及到的知识点：
> bootstrap语法  
flask视图 路由 模板 静态文件创建  
jinja2模板语法  
使用sqlachemy操作msyql  
使用wtforms定义表单  

项目引用自[天涯明月笙 ](https://www.jianshu.com/p/9e44acf19513) ,此处主要针对该项目各章内容进行github维护内容，主要为完善各阶段的知识，内容，感谢原博主。
