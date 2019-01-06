import pymysql
from settings import Config


def connect():
    conn = Config.POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    return conn, cursor


def connect_close(conn, cursor):
    cursor.close()
    conn.close()


def select_one(sql, args):
    conn, cursor = connect()
    cursor.execute(sql, args)
    data = cursor.fetchone()
    connect_close(conn, cursor)
    return data


def select_all(sql, args):
    conn, cursor = connect()
    cursor.execute(sql, args)
    data = cursor.fetchall()
    connect_close(conn, cursor)

    return data


def insert(sql, args):
    conn, cursor = connect()
    row = cursor.execute(sql, args)
    conn.commit()
    connect_close(conn, cursor)
    return row