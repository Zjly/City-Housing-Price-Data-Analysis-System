# -*- coding: utf-8 -*-

import scrapy
from houseprice_crawler.items import LocationItem


class LocationSpider(scrapy.Spider):
    name = 'location'
    allowed_domains = ['jiwu.com']
    start_urls = ['http://www.jiwu.com/']


    def parse(self, response):
        dls = response.xpath("/html/body/div[4]/dl")
        provinces = []  # 全部省份
        cities = []  # 城市
        city_dic = {}
        for dl in dls:
            ds = dl.xpath("./dt/text()").extract()
            provinces.extend(ds)
            ds = dl.xpath("./dd")
            for d in ds:
                names = d.xpath("./a/text()").extract()
                cities.append(names)
                urls = d.xpath("./a/@href").extract()
                city_dic.update(zip(names, urls))
        item = LocationItem()
        item['cities'] = cities
        item['provinces'] = provinces
        item['city_dic'] = city_dic
        yield item
