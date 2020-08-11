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
    # 新房价
    areaPrice = scrapy.Field()
    # 二手房价
    esfareaPrice = scrapy.Field()
    # 月份
    compareDate = scrapy.Field()
    # 年份
    compareYear = scrapy.Field()
    # 最低价
    minPrice = scrapy.Field()
    # 最高价
    maxPrice = scrapy.Field()

    # 三年新房价
    threeAreaPrice = scrapy.Field()
    # 三年二手房价
    threeEsfareaPrice = scrapy.Field()
    # 三年月份
    threeCompareDate = scrapy.Field()
    # 三年年份
    threeCompareYear = scrapy.Field()
    # 三年最低价
    threeminPrice = scrapy.Field()
    # 三年最高价
    threemaxPrice = scrapy.Field()

    # 新房价格区间
    buildPriceNameList = scrapy.Field()
    # 新房区间数量
    buildPriceCount = scrapy.Field()
    # 二手房价格区间
    esfPriceNameList = scrapy.Field()
    # 二手房区间数量
    esfPriceCount = scrapy.Field()

    # 域名
    domain = scrapy.Field()

    # 新房平均价
    new_avg = scrapy.Field()
    # 二手房均价
    esf_avg = scrapy.Field()
    # 新房销售变化
    new_cgreen = scrapy.Field()
    # 二手房销售变化
    esf_cgreen = scrapy.Field()

    # 城市id
    cid = scrapy.Field()
    # 省份
    province = scrapy.Field()
    # 城市
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
