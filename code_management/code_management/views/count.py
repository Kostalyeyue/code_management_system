from flask import Flask,Blueprint,request,render_template,session,redirect
from ..itls.md5 import md5
from settings import Config
from ..itls import helper

count = Blueprint('count',__name__)

@count.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    pwd = md5(pwd)
    print(pwd)
    # import pymysql
    # conn = Config.POOL.connection()
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # #sql = "select * from userinfo where username='%s' and password = '%s'"%("as ' or 1=1 -- ",'76bb9bd144db9302865986f4d375b0ed')
    # #sql注入
    # cursor.execute("select id,nickname from userinfo where username= %s and password = %s",(user,pwd))
    # data = cursor.fetchone()
    # print(data)
    data = helper.select_one("select id,nickname from userinfo where username= %s and password = %s",(user,pwd))
    if not data:
        return render_template('login.html',error='用户名错误')

    session['user_info'] = {'id':data['id'],'nickname':data['nickname']}
    print(session['user_info'])

    return redirect('/home')

@count.route('/logout')
def logout():
    if 'user_info' in session:
        del session['user_info']

    return redirect('/login')