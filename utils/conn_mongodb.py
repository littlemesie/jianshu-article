# -*- coding:utf-8 -*-
from pymongo import MongoClient
"""
@summary:mongodb连接
"""
class MongodbUtil(object):

    @staticmethod
    def get_conn():
        client = MongoClient('mongodb://101.132.191.134:8010/')
        return client

    def insert_one(self,db_name,col_name,values):
        """
        @summary: 插入一条数据
        :param db_name: 数据库名
        :param col_name: 集合名
        :param values: 文本内容
        :return:
        """
        client = self.get_conn()
        db = client[db_name]
        col = db[col_name]
        result = col.insert_one(values)
        return result.inserted_id

    def insert_more(self,db_name,col_name,values):
        """
        @summary: 插入多条数据
        :param db_name: 数据库名
        :param col_name: 集合名
        :param values: 文本内容
        :return:
        """
        client = self.get_conn()
        db = client[db_name]
        col = db[col_name]
        result = col.insert_many(values)
        return result.inserted_ids

    def get_one(self, db_name,col_name,param=None):
        """
        @summary:查询一条数据
        :param db_name:
        :param col_name:
        :param param: 字典类型
        :return:
        """
        client = self.get_conn()
        db = client[db_name]
        col = db[col_name]
        if param is None:
            result = col.find_one()
        else:
            result = col.find_one(param)
        return result

    def get_more(self, db_name,col_name,param=None):
        """
        @summary:查询多条数据
        :param db_name:
        :param col_name:
        :param param: 字典类型
        :return:
        """
        client = self.get_conn()
        db = client[db_name]
        col = db[col_name]
        if param is None:
            result = col.find()
        else:
            result = col.find(param)
        return result

    def update_one(self,db_name,col_name,old_values,new_values):
        """
        @summary:更新一条数据
        :param db_name:
        :param col_name:
        :param old_values: 字典类型
        :param new_values: 字典类型
        :return:
        """
        client = self.get_conn()
        db = client[db_name]
        col = db[col_name]
        result = col.update_one(old_values,new_values)
        return result.inserted_id

    def delete_one(self,db_name,col_name,values):
        """
        @summary:删除一条数据
        :param db_name:
        :param col_name:
        :param values: 字典类型
        :return:
        """
        client = self.get_conn()
        db = client[db_name]
        col = db[col_name]
        result = col.update_one(values)
        return result.inserted_id

    def delete_more(self,db_name,col_name,values):
        """
        @summary:删除多条数据
        :param db_name:
        :param col_name:
        :param values: 字典类型
        :return:
        """
        client = self.get_conn()
        db = client[db_name]
        col = db[col_name]
        result = col.update_many(values)
        return result.inserted_ids

    def sort(self,db_name,col_name,name,param=1):
        """
        @summary:排序
        :param db_name:
        :param col_name:
        :param name: 排序字段
        :param param: 1 升序 -1 降序
        :return:
        """
        client = self.get_conn()
        db = client[db_name]
        col = db[col_name]
        if param is 1:
            result = col.find().sort(name)
        else:
            result = col.find().sort(name,-1)
        return result

    def test(self):
        client = self.get_conn()
        db = client["test"]
        col = db['sites']
        mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
        id = self.insert_one('test','sites',mydict)
        print(id)

if __name__ == '__main__':
    mongodbUtil = MongodbUtil()
    mongodbUtil.test()