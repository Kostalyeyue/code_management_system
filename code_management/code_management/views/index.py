from flask import Flask,Blueprint,render_template,session,redirect,request
import os,uuid
from ..itls import helper

index = Blueprint('index',__name__)

@index.before_request
def process_request():
    if not session.get('user_info'):
        return redirect("/login")
    return None

@index.route('/home')
def home():
    return render_template('index.html')



@index.route('/user_list')
def user_list():
    # import pymysql
    # conn = pymysql.Connect(host='127.0.0.1', user='root', password='123456', database='flask_eg1', charset='utf8')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # # sql = "select * from userinfo where username='%s' and password = '%s'"%("as ' or 1=1 -- ",'76bb9bd144db9302865986f4d375b0ed')
    # # sql注入
    # cursor.execute("select id,username,nickname from userinfo")
    # users = cursor.fetchall()
    # cursor.close()
    # conn.close()
    # print(users)
    users = helper.select_all("select id,username,nickname from userinfo",[])
    return render_template('user_list.html',users=users)


@index.route('/detail/<int:nid>')
def detail(nid):
    # import pymysql
    # conn = pymysql.Connect(host='127.0.0.1', user='root', password='123456', database='flask_eg1', charset='utf8')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # cursor.execute("select user_id,line,ctime from record where user_id = %s",(nid,))
    # records = cursor.fetchall()
    # cursor.close()
    # conn.close()
    # print(records)
    records = helper.select_all("select user_id,line,ctime from record where user_id = %s",(nid,))
    return render_template('detail.html', records=records)


@index.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    file_obj = request.files.get('code')
    name_ext = file_obj.filename.rsplit('.',maxsplit=1)
    if len(name_ext) != 2:
        return '请上传zip压缩文件'
    if name_ext[1] != 'zip':
        return '请上传zip压缩文件'
    print(file_obj)
    print(file_obj.filename)
    import shutil
    target_path =  os.path.join('files',str(uuid.uuid4()))
    shutil._unpack_zipfile(file_obj.stream,target_path)

    total_num = 0
    for base_path,folder_list,file_list in os.walk(target_path):
        for file_name in file_list:
            file_path = os.path.join(base_path,file_name)
            file_ext = file_path.rsplit('.',maxsplit=1)
            if len(file_ext) != 2:
                continue
            if file_ext[1] != 'py':
                continue
            line_num = 0
            with open(file_path,'rb') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    if line.startswith(b'#'):
                        continue
                    line_num += 1
            total_num += line_num
            # print(file_path,line_num)
    import datetime
    ctime = datetime.date.today()
    print(ctime,total_num,session['user_info']['id'])
    # import pymysql
    # conn = pymysql.Connect(host='127.0.0.1', user='root', password='123456', database='flask_eg1', charset='utf8')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # cursor.execute("select id from record where user_id = %s and ctime=%s", (session['user_info']['id'],ctime))
    # data = cursor.fetchone()
    # cursor.close()
    # conn.close()
    data = helper.select_one("select id from record where user_id = %s and ctime=%s", (session['user_info']['id'],ctime))
    print(data)
    # if data:
    #     return '你今天已经上传了'

    # conn = pymysql.Connect(host='127.0.0.1', user='root', password='123456', database='flask_eg1', charset='utf8')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # cursor.execute("insert into record(user_id,line,ctime) values(%s,%s,%s)", (session['user_info']['id'],total_num,ctime))
    # conn.commit()
    # cursor.close()
    # conn.close()

    data = helper.insert("insert into record(user_id,line,ctime) values(%s,%s,%s)",(session['user_info']['id'],total_num,ctime))
    #上传几次
    print(data)

    return "上传成功"