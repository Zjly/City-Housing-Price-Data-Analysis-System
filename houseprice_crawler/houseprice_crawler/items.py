# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LocationItem(scrapy.Item):
    # 所有省份
    provinces = scrapy.Field()
    # 城市
    cities = scrapy.Field()
    # urls
    city_dic = scrapy.Field()


class InfoItem(scrapy.Item):
    areaPrice = scrapy.Field()
    esfareaPrice = scrapy.Field()
    compareDate = scrapy.Field()
    compareYear = scrapy.Field()
    minPrice = scrapy.Field()
    maxPrice = scrapy.Field()

    threeAreaPrice = scrapy.Field()
    threeEsfareaPrice = scrapy.Field()
    threeCompareDate = scrapy.Field()
    threeCompareYear = scrapy.Field()
    threeminPrice = scrapy.Field()
    threemaxPrice = scrapy.Field()

    buildPriceNameList = scrapy.Field()
    buildPriceCount = scrapy.Field()
    esfPriceNameList = scrapy.Field()
    esfPriceCount = scrapy.Field()

    domain = scrapy.Field()

    new_avg = scrapy.Field()
    esf_avg = scrapy.Field()
    new_cgreen = scrapy.Field()
    esf_cgreen = scrapy.Field()

    cid = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()


class NewHouseItem(scrapy.Item):
    # 省份
    province = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 小区的名字
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 几居
    rooms = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 行政区
    district = scrapy.Field()
    # 是否在售
    sale = scrapy.Field()
    # 详情页面url
    origin_url = scrapy.Field()


class ESFHouseItem(scrapy.Item):
    # 省份
    province = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 小区的名字
    name = scrapy.Field()
    # 几室几厅
    rooms = scrapy.Field()
    # 层
    floor = scrapy.Field()
    # 朝向
    toward = scrapy.Field()
    # 年代
    year = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 建筑面积
    area = scrapy.Field()
    # 总价
    price = scrapy.Field()
    # 单价
    unit = scrapy.Field()
    # 原始url
    origin_url = scrapy.Field()
