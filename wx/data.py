## -*- coding: utf-8 -*-
import pymysql
import sys
import traceback

'''
封装数据库操作不用Djanggo 集成
pymysql使用指南 
host = '127.0.0.1'  回送地址，指本地机 
port = 3306  MySQL的默认端口 
user 用户名 
passwd 密码 
db 数据库 
charset 字符类型
'''


class DBMysqlHelp:
    # 构造函数
    def __init__(self, host='120.27.118.193', user='root', pwd='admin', db='ccars'):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.conn = None
        self.cur = None

    # 连接数据库
    def connectDatabase(self):
        try:
            self.conn = pymysql.connect(self.host, self.user,
                                        self.pwd, self.db, charset='utf8')

            self.cur = self.conn.cursor()
            return True
        except:
            # print("连接异常")
            traceback.print_exc()
            return False

    # 关闭数据库
    def close(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    # 执行数据库的sq语句,主要用来做插入操作
    def execute(self, sql, params=None):
        # 连接数据库
        self.connectDatabase()
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                self.cur.execute(sql, params)
                self.conn.commit()
                return True
        except:
            self.close()
            return False

    # 用来查询表数据
    def fetchall(self, sql, params=None):
        is_false = self.execute(sql, params)
        if is_false:
            info = self.cur.fetchall()
            self.cur.close()
            self.conn.close()
            return info
        else:
            return False

    # 新增数据
    def insert(self, sql):
        self.execute(sql)
        return self.cur.rowcount

    # 修改数据
    def update(self, sql):
        self.execute(sql)
        return self.cur.rowcount

    # 删除数据
    def delete(self, sql):
        self.execute(sql)
        return self.cur.rowcount


if __name__ == '__main__':
    model = DBMysqlHelp()
    info = model.fetchall("select c_oid,c_name,c_start from c_org limit 0,3")
    print(info);
