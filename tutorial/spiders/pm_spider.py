import scrapy
from tutorial.items import Pm25CityItem, CityLiveData
import uuid


class Pm25Spider(scrapy.Spider):
    name = "pm25"
    allowed_domains = ["pm25.in"]
    start_urls = [
        'http://www.pm25.in',
    ]

    def parse(self, response):
        sel = scrapy.Selector(response)
        citys = sel.xpath("//div[@class='all']/div[@class='bottom']/ul[@class='unstyled']/div[2]/li")
        city_items = []
        for city in citys:
            city_item = Pm25CityItem()
            href = ''.join(city.xpath('a/@href').extract()).strip()
            city_item['city_name'] = ''.join(city.xpath('a/text()').extract()).strip()
            city_item['home_link'] = 'http://www.pm25.in' + href
            city_item['city_pinyin'] = href.split('/')[1]
            # city_items.append(city_item)

            meta = {'city_name': city_item['city_name'], 'city_pinyin': city_item['city_pinyin'],
                    'proxy' : 'http://192.168.1.7:81'}
            yield scrapy.Request(city_item['home_link'], callback=self.get_livedata, meta=meta)

    def get_livedata(self, response):
        liveData = CityLiveData()

        id = uuid.uuid1()

        liveData['id'] = id
        liveData['city_name'] = response.meta['city_name']
        liveData['city_pinyin'] = response.meta['city_pinyin']

        sel = scrapy.Selector(response)

        level = ''.join(sel.xpath("//div[@class='level']/h4/text()").extract()).strip()
        live_data_time = ''.join(sel.xpath("//div[@class='live_data_time']/p/text()").extract()).strip()
        live_data_unit = ''.join(sel.xpath("//div[@class='live_data_unit']/text()").extract()).strip()

        live_data_time = live_data_time[live_data_time.find("：") + 1:]
        live_data_unit = live_data_unit[live_data_unit.find("：") + 1:]

        aqi = ''.join(sel.xpath(
            "//div[@class='caption' and contains(text(), 'AQI')]/parent::div/div[@class='value']/text()").extract()).strip()
        pm2_5_1h = ''.join(sel.xpath(
            "//div[@class='caption' and contains(text(), 'PM2.5/1h')]/parent::div/div[@class='value']/text()").extract()).strip()
        no2_1h = ''.join(sel.xpath(
            "//div[@class='caption' and contains(text(), 'NO2/1h')]/parent::div/div[@class='value']/text()").extract()).strip()
        o3_1h = ''.join(sel.xpath(
            "//div[@class='caption' and contains(text(), 'O3/1h')]/parent::div/div[@class='value']/text()").extract()).strip()
        so2_1h = ''.join(sel.xpath(
            "//div[@class='caption' and contains(text(), 'SO2/1h')]/parent::div/div[@class='value']/text()").extract()).strip()
        pm10_1h = ''.join(sel.xpath(
            "//div[@class='caption' and contains(text(), 'PM10/1h')]/parent::div/div[@class='value']/text()").extract()).strip()
        o3_8h = ''.join(sel.xpath(
            "//div[@class='caption' and contains(text(), 'O3/8h')]/parent::div/div[@class='value']/text()").extract()).strip()
        co_1h = ''.join(sel.xpath(
            "//div[@class='caption' and contains(text(), 'CO/1h')]/parent::div/div[@class='value']/text()").extract()).strip()

        primary_pollutant = ''.join(sel.xpath(
            "//div[@class='primary_pollutant']/p/text()").extract()).strip()
        action = ''.join(sel.xpath(
            "//div[@class='action']/p/text()").extract()).strip()
        affect = ''.join(sel.xpath(
            "//div[@class='affect']/p/text()").extract()).strip()
        liveData['level'] = level
        liveData['time_point'] = live_data_time
        liveData['data_unit'] = live_data_unit
        liveData['aqi'] = aqi
        liveData['pm2_5_1h'] = pm2_5_1h
        liveData['no2_1h'] = no2_1h
        liveData['o3_1h'] = o3_1h
        liveData['so2_1h'] = so2_1h
        liveData['pm10_1h'] = pm10_1h
        liveData['o3_8h'] = o3_8h
        liveData['co_1h'] = co_1h
        liveData['primary_pollutant'] = primary_pollutant
        liveData['action'] = action
        liveData['affect'] = affect
        return liveData




