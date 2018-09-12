# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Pm25CityItem(scrapy.Item):
    city_name = scrapy.Field() #城市的名称
    home_link = scrapy.Field() #对应数据的链接地址
    city_pinyin = scrapy.Field() #城市的拼音

class CityLiveData(scrapy.Item):
    id = scrapy.Field()
    pm2_5_1h = scrapy.Field()
    no2_1h = scrapy.Field()
    o3_1h = scrapy.Field()
    so2_1h = scrapy.Field()
    level = scrapy.Field()
    primary_pollutant = scrapy.Field()
    pm10_1h = scrapy.Field()
    city_name = scrapy.Field()
    city_pinyin = scrapy.Field()
    action = scrapy.Field()
    affect = scrapy.Field()
    o3_8h = scrapy.Field()
    data_unit = scrapy.Field()
    aqi = scrapy.Field()
    time_point = scrapy.Field()
    co_1h = scrapy.Field()
