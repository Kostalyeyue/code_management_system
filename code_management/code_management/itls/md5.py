import hashlib
from settings import Config

def md5(arg):
    hash = hashlib.md5(Config.SALT)
    hash.update(bytes(arg,encoding='utf-8'))
    return hash.hexdigest()

# import pymysql
# conn = pymysql.Connect(host='127.0.0.1',user='root',password='123456',database='flask_eg1',charset='utf8')
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# #sql = "select * from userinfo where username='%s' and password = '%s'"%("as ' or 1=1 -- ",'76bb9bd144db9302865986f4d375b0ed')
# #sql注入
# cursor.execute("select * from userinfo where username= %s and password = %s",("wudi",'76bb9bd144db9302865986f4d375b0ed'))
# data = cursor.fetchone()
#
# cursor.close()
# conn.close()
# print(data)

