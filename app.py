
#!/usr/local/bin/python3
# coding: utf-8
 
from flask import Flask, redirect, url_for, session
from flask import render_template, request, flash

import os, json, datetime
import bbslogin
import data
from models import models

from flask_sqlalchemy import SQLAlchemy

 
app = Flask(__name__)
app.secret_key = 'secret_key'

app.config.from_object('config')

db = SQLAlchemy(app)


@app.route('/')
def index():
    if not bbslogin.is_login():
        return redirect('\login')

    return render_template('index.html',
        user=bbslogin.get_user(),
        data=data.load_data(),
    )

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/try_login', methods=['POST'])
def try_login():
    user = request.form.get('user', '')
    pw = request.form.get('pw', '')

    if bbslogin.try_login(user, pw):
        return redirect('/')
    return show_msg('失敗！！！')

@app.route('/logout')
def logout():
    bbslogin.try_logout()
    return show_msg('ログアウトしました')

@app.route('/write', methods=['POST'])
def write():
    if not bbslogin.is_login():
        return redirect('/login')
    
    ta = request.form.get('ta', '')
    if ta == '':
        return show_msg('書き込んでね')

    data.save_data_append(
        user=bbslogin.get_user(),
        text = ta)
    return redirect('/')

def show_msg(msg):
    return render_template('msg.html', msg=msg)


@app.route('/test')
def test():
    a = request.args.get('a')
    b = request.args.get('b')
    if a is None and b is None:
        return "残念"
    elif a is None and b is not None:
        return b
    elif a is not None and b is None:
        return a
    else:
        return str(int(a) * int(b))

@app.route('/kyokin')
def input_page():
    filter_date = datetime.date.today()
    print(filter_date)
    #entries = models.MascleData.query.order_by(models.MascleData.id.desc()).all()
    entries = models.MascleData.query.filter(models.MascleData.done_at>datetime.date.today()).order_by(models.MascleData.id.desc()).all()
    return render_template('kyokin.html',entries=entries)
    
@app.route('/add', methods=['POST'])
def add_entry():
    try:

        mascle_data = models.MascleData(
                kind_of_mascle=request.form['kind_of_mascle'],
                reps=float(request.form['reps']),
                weight= float(request.form['weight']),
                done_at= datetime.date.today(),
                )
        db.session.add(mascle_data)
        db.session.commit()
        flash('New entry was successfully posted')
        return redirect(url_for('input_page'))
    except ValueError:
        return render_template(url_for('input_page'), massage="必要な値を入力してください")


    



if __name__ == '__main__':
    app.run(debug=True)
 