## -*- coding: utf-8 -*-
import pymysql


class DBHelper:
    # 构造函数
    def __init__(self, host='localhost', user='root',
                 pwd='', db='ccars'):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.conn = None
        self.cur = None

    # 连接数据库
    def connectDatabase(self):
        try:
            self.conn = pymysql.connect(host='127.0.0.1',
                                     port=3306,
                                     user='root',
                                     passwd='zx123456',
                                     db='ccars',
                                     charset='utf8'
                                     )
        except:
            return False
        self.cur = self.conn.cursor()
        return True

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
        except:
            self.close()
            return False
        return True

    # 用来查询表数据
    def all_data(self, sql, params=None):
        self.execute(sql, params)
        return self.cur.fetchone()


if __name__ == '__main__':
    dbhelper = DBHelper()
    sql = "select * from c_org"
    result = dbhelper.all_data(sql, None)
    if result:
        print(result)
    else:
        print("maoyan　table创建失败")

