# -*- coding: utf-8 -*-

import csv
import scrapy
import re
import time


from houseprice_crawler.items import NewHouseItem, ESFHouseItem


class PriceSpider(scrapy.Spider):
    name = 'price'
    allowed_domains = ['fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.htm']


    def parse(self, response):
        trs = response.xpath("//div[@class='outCont']//tr")
        province = None
        data = [("省份", "城市", "城市url", "新房url", "二手房url")]
        for tr in trs:
            tds = tr.xpath(".//td[not(@class)]")
            province_td = tds[0]
            province_text = province_td.xpath(".//text()").get()
            province_text = re.sub(r"\s", "", province_text)
            if province_text:
                province = province_text
            # 不管其他国家的
            if province == "其它":
                break
            city_td = tds[1]
            city_links = city_td.xpath(".//a")
            for city_link in city_links:
                city = city_link.xpath(".//text()").get()
                city_url = city_link.xpath(".//@href").get()
                # 构建新房url
                url_moudle = city_url.split(".", 1)
                scheme = url_moudle[0]
                domain = url_moudle[1]
                newhouse_url = scheme + "." + "newhouse" + "." + domain + "/house/s"
                # 构建二手房url
                esf_url = scheme + "." + "esf" + "." + domain
                if 'bj' in newhouse_url:
                    newhouse_url = "https://newhouse.fang.com/house/s"
                    esf_url = "https://esf.fang.com/"
                data.append((str(province), str(city), str(city_url), str(newhouse_url), str(esf_url)))

                yield scrapy.Request(url=newhouse_url, callback=self.parse_newhouse, meta={"info": (province, city)})
                yield scrapy.Request(url=esf_url, callback=self.parse_esf, meta={"info": (province, city)})


    def parse_newhouse(self, response):
        province, city = response.meta.get("info")
        lis = response.xpath("//div[contains(@class, 'nl_con')]/ul/li")
        for li in lis:
            name = li.xpath(".//div[@class='nlcd_name']/a/text()").get() # 为什么不直接.strip（）呢？ 因为里面有莫名其妙的None值
            if name == None:
                continue
            name = name.strip()
            # print(name)
            house_type_list = li.xpath(".//div[contains(@class,'house_type')]/a/text()").getall()
            # print(house_type_list)

            house_type_list = list(map(lambda x: re.sub(r"\s", "", x), house_type_list))
            rooms = list(filter(lambda x: x.endswith("居"), house_type_list))

            area = "".join(li.xpath(".//div[contains(@class,'house_type')]/text()").getall())
            area = re.sub(r"\s|－|/|", "", area)

            address = li.xpath(".//div[@class='address']/a/@title").get()

            district_text = "".join(li.xpath(".//div[@class='address']//text()").getall())

            district_text = re.search(r".*\[(.+)\].*", district_text)
            if district_text:
                district = district_text.group(1)

            sale = li.xpath(".//div[contains(@class,'fangyuan')]/span/text()").get()

            price = "".join(li.xpath(".//div[@class='nhouse_price']//text()").getall())
            price = re.sub(r"\s|广告", "", price)

            origin_url = li.xpath(".//div[@class='nlcd_name']/a/@href").get()

            item = NewHouseItem(province=province, city=city, name=name, rooms=rooms, area=area, address=address, district=district, sale=sale, price=price, origin_url=origin_url)

            yield item

        next_url = response.xpath("//div[@class='page']//a[@class='next'][2]/@href").get()
        if not next_url:
            next_url = response.xpath("//div[@class='page']//a[@class='next']/@href").get()

        if next_url:
            o_url = response.url.split("/", 3)
            complete_orl = o_url[0] + "//" + o_url[2] + next_url
            # print(next_url)
            # print(complete_orl)
            yield scrapy.Request(url=complete_orl, callback=self.parse_newhouse, meta={"info": (province, city)})

    """
    必须吐槽房天下 新房 网站，第五页之前没有上一页的选项，但是前段代码居然有class = ‘last’，第五页之后有了上一页，但是上一页的前端代码的class设为了next，下一页的class还是next
    ？？？？？？？？？？？？？？？？？？？？？？？？？
    一不小心莫名死循环
    """

    def parse_esf(self, response):
        province, city = response.meta.get("info")

        dls = response.xpath("//div[@class='shop_list shop_list_4']/dl")
        for dl in dls:
            item = ESFHouseItem(province=province, city=city)

            item["name"] = dl.xpath(".//p[@class='add_shop']/a/@title").get()

            infos = dl.xpath(".//p[@class='tel_shop']/text()").getall()
            infos = list(map(lambda x: re.sub(r"\s", "", x), infos))
            for info in infos:
                if '厅' in info:
                    item["rooms"] = info
                elif '层' in info:
                    item["floor"] = info
                elif '向' in info:
                    item["toward"] = info
                elif '年' in info:
                    item["year"] = info.replace("年建", "")
                elif '㎡' in info:
                    item["area"] = info.replace("㎡", "")

            item["address"] = dl.xpath(".//p[@class='add_shop']/span/text()").get()

            item["price"] = dl.xpath(".//dd[@class='price_right']/span/b/text()").get()

            item["unit"] = dl.xpath(".//dd[@class='price_right']/span[2]//text()").get()

            detail_url = dl.xpath(".//h4[@class='clearfix']/a/@href").get()
            item["origin_url"] = response.urljoin(detail_url)

            yield item

        next_url = response.xpath("//div[@class='page_al']/p/a[2]/@href").get()
        if not next_url:
            next_url = response.xpath("//div[@class='page_al']/p/a/@href").get()

        # print(next_url)
        # print(response.url)

        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_esf, meta={"info": (province, city)})