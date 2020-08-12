# -*- coding: utf-8 -*-

import scrapy
from houseprice_crawler.items import InfoItem
from houseprice_crawler.pipelines import HousepriceCrawlerPipeline

cities = HousepriceCrawlerPipeline().select_all_cities()


class InfoSpider(scrapy.Spider):
    name = 'info'

    start_urls = ['http://qingdao.jiwu.com/fangjia/']

    def parse(self, response):
        for i in cities:
            yield scrapy.Request("http://" + i[3] + "/fangjia/", callback=self.parse_detail, meta={
                'cid': i[0],
                'province': i[1],
                'city': i[2]
            })

    def parse_detail(self, response):
        item = InfoItem()
        meta = response.meta
        item['cid'] = meta['cid']
        item['province'] = meta['province']
        item['city'] = meta['city']

        item['areaPrice'] = response.xpath('//*[@id="areaPrice"]/@value').get()  # 新房
        item['esfareaPrice'] = response.xpath(
            '//*[@id="esfareaPrice"]/@value').get()  # 二手房
        item['compareDate'] = response.xpath(
            '//*[@id="compareDate"]/@value').get()  # 近一年月份
        item['compareYear'] = response.xpath(
            '//*[@id="compareYear"]/@value').get()  # 近一年年份
        item['minPrice'] = response.xpath('//*[@id="minPrice"]/@value').get()  # 近一年最小值
        item['maxPrice'] = response.xpath('//*[@id="maxPrice"]/@value').get()  # 近一年最大值

        item['threeAreaPrice'] = response.xpath(
            '//*[@id="threeAreaPrice"]/@value').get()  # 新房
        item['threeEsfareaPrice'] = response.xpath(
            '//*[@id="threeEsfareaPrice"]/@value').get()  # 二手房
        item['threeCompareDate'] = response.xpath(
            '//*[@id="threeCompareDate"]/@value').get()  # 近三年月份
        item['threeCompareYear'] = response.xpath(
            '//*[@id="threeCompareYear"]/@value').get()  # 近三年年份
        item['threeminPrice'] = response.xpath(
            '//*[@id="threeminPrice"]/@value').get()  # 近三年最小值
        item['threemaxPrice'] = response.xpath(
            '//*[@id="threemaxPrice"]/@value').get()  # 近三年最大值

        item['buildPriceNameList'] = response.xpath(
            '//*[@id="buildPriceNameList"]/@value').get()  # 近三年最大值
        item['buildPriceCount'] = response.xpath(
            '//*[@id="buildPriceCount"]/@value').get()  # 近三年最大值
        item['esfPriceNameList'] = response.xpath(
            '//*[@id="esfPriceNameList"]/@value').get()  # 近三年最大值
        item['esfPriceCount'] = response.xpath(
            '//*[@id="esfPriceCount"]/@value').get()  # 近三年最大值

        item['domain'] = response.xpath('//*[@id="domain"]/@value').get()  # 近三年最大值

        item['new_avg'] = response.xpath(
            '//*[@class="maincon"]/div[1]/div[1]/div[2]/span[1]/text()').get()

        item['esf_avg'] = response.xpath(
            '//*[@class="maincon"]/div[1]/div[2]/div[2]/span[1]/text()').get()

        item['new_cgreen'] = response.xpath(
            '//*[@class="maincon"]/div[1]/div[1]/div[2]/span[2]/text()').get()

        item['esf_cgreen'] = response.xpath(
            '//*[@class="maincon"]/div[1]/div[2]/div[2]/span[2]/text()').get()
        yield item
