# -*- coding: utf-8 -*-

import pymssql

class DBHelper(object):

    def __init__(self, serverIp, port, dbName, user, pwd):
        if not dbName:
            raise (NameError, "没有设置数据库信息")
        self.connection = pymssql.connect(server=serverIp, port=port, user=user, password=pwd,
                                          database=dbName,
                                          charset="UTF-8")
        self.cursor = self.connection.cursor()
        if not self.cursor:
            raise (NameError, "连接数据库失败")

    def __del__(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None
            print(self.cursor, '__del__ cursor closed')
        if self.connection:
            self.connection.close()
            self.connection = None

    def destroy(self):
        if self.cursor:
            print(self.cursor, 'destroy cursor closed')
            self.cursor.close()
            self.cursor = None
        if self.connection:
            self.connection.close()
            self.connection = None

    # 获取全部查询结果
    def queryAll(self, qryStr):
        print(qryStr.decode('gbk'))
        self.cursor.execute(qryStr)
        return self.cursor.fetchall()

    # 获取前maxcnt条查询结果
    def querySome(self, qryStr, maxCount):
        self.cursor.execute(qryStr)
        return self.cursor.fetchmany(maxCount)

    # 获取分页查询结果
    def queryPage(self, qryStr, skipCnt, pageSize):
        self.cursor.execute(qryStr)
        self.cursor.skip(skipCnt)
        return self.cursor.fetchmany(pageSize)

    # 获取查询条数
    def count(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]

    # 执行语句，包括增删改，返回变更数据数量
    def execute(self, sql):
        print(sql)
        self.cursor.execute(sql)
        self.connection.commit()

    # 执行语句，包括增删改，返回变更数据数量
    def execute_many(self, sql, param):
        self.cursor.executemany(sql, param)
        self.connection.commit()
