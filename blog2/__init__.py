# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment

print("加载配置文件内容")
app = Flask(__name__)
app.config.from_object('blog2.setting')  # 模块下的setting文件名，不加.py
app.config.from_envvar('FLASKR_SETTINGS')  # 环境变量，指向配置文件setting的路径
# FLASKR_SETTINGS环境变量需要手动单独设置
# FLASKR_SETTINGS='D:\HelloWorld\practice\flask_blog\blog2\setting.py'

print("创建数据库对象")
db = SQLAlchemy(app)

print("只有在app对象之后声明，用于导入model否则无法创建表")
from blog2.model.User import User
from blog2.model.Category import Category

print("只有在app对象之后声明，用于导入view模块")
from blog2.controller import blog_message

moment = Moment(app)

login_manager = LoginManager()  # 声明login对象
login_manager.init_app(app)  # 初始化绑定到应用

# 声明默认视图函数为login，当我们@require_login时，如果没有登录会自动跳到该函数处理
login_manager.login_view = 'login'

# login_manager.session_protection = "strong"
# 可以设置None,'basic','strong'  以提供不同的安全等级,一般设置strong,如果发现异常会登出用户


# 当登陆成功后，该函数会自动从会话中存储的用户 ID 重新加载用户对象。它应该接受一个用户的 unicode ID 作为参数，并且返回相应的用户对象。
@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))
