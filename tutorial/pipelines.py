# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import log
from tutorial.dbHelper import DBHelper
from tutorial.items import CityLiveData


class TutorialPipeline(object):
    def __init__(self, dbhelper):
        self.dbhelper = dbhelper

    @classmethod
    def from_settings(cls, settings):
        host = settings['SQLSERVER_HOST14']
        db = settings['SQLSERVER_DBNAME14']
        user = settings['SQLSERVER_USER14']
        passwd = settings['SQLSERVER_PASSWD14']
        port = settings['SQLSERVER_PORT14']
        return cls(DBHelper(host, port, db, user, passwd))

    def process_item(self, item, spider):
        if isinstance(item, CityLiveData):

            if item:
                self.save_livedata(item)
        return item

    # 插入城市的数据到tbl_all_city中
    def save_city(self, item):
        # 插入数据库的sql语句
        sql = "insert into tbl_all_city(pinyin, name, link) values ('%s', '%s', '%s')" % (
        item["city_pinyin"], item["city_name"], item["home_link"])
        self.dbhelper.execute(sql)

    # 插入空气质量数据到tbl_all_city中
    def save_livedata(self, item):
        # 插入数据库的sql语句
        sql = 'INSERT INTO tbl_live_data VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        param = [(item['id'], item['pm2_5_1h'], item['no2_1h'], item['o3_1h'], item['so2_1h'], item['level'],
                  item['primary_pollutant'], item['pm10_1h'], item['city_name'], item['city_pinyin'], item['action'],
                  item['affect'], item['o3_8h'], item['data_unit'], item['aqi'], item['time_point'],
                  item['co_1h'])]
        self.dbhelper.execute_many(sql, param)
