# -*- coding: utf-8 -*-
from flask_login import login_required, login_user, logout_user

from blog2.model.User import User
from blog2.model.Category import Category

from blog2 import app, db
from flask import request, render_template, flash, abort, url_for, redirect, session


@app.route('/')
def show_entries():
    categorys = Category.query.all()
    return render_template('show_entries.html', entries=categorys)


@app.route('/add', methods=['POST','GET'])
@login_required
def add_entry():
    # if not session.get('logged_in'):
    #     abort(401)
    if request.method == 'GET':
        return redirect(url_for('login'))
    title = request.form['title']
    content = request.form['text']
    categroy = Category(title, content)
    db.session.add(categroy)
    db.session.commit()
    flash('新文章发布成功')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        # passwd = User.query.filter_by(password=request.form['password']).first()
        #
        # if user is None:
        #     error = '用户名错误'
        # elif passwd is None:
        #     error = '密码错误'
        # else:
        #     session['logged_in'] = True
        login_user(user)
        flash('登录成功')
        return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    # session.pop('logged_in', None)
    logout_user()
    flash('已经注销')
    return redirect(url_for('show_entries'))
