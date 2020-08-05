# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import datetime
import pymysql
from houseprice_crawler.settings import (
    db_charset, db_name, db_pwd, db_user, db_port, db_host
)
from houseprice_crawler.items import NewHouseItem, ESFHouseItem, LocationItem, InfoItem


class HousepriceCrawlerPipeline:
    def __init__(self):
        self.conn = pymysql.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            passwd=db_pwd,
            db=db_name,
            charset=db_charset
        )
        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):
        if isinstance(item, LocationItem):
            self.save_location(item)
        elif isinstance(item, NewHouseItem):
            self.save_newhouse(item)
        elif isinstance(item, ESFHouseItem):
            self.save_esf(item)
        elif isinstance(item, InfoItem):
            self.save_info(item)
        return item


    def save_location(self, item):
        provinces = item['provinces']
        cities = item['cities']
        city_dic = item['city_dic']
        for i in range(len(provinces)):
            select_sql = "select count(1) from info_location where province='%s';" % provinces[i]
            self.cursor.execute(select_sql)
            res = self.cursor.fetchone()[0]
            print('%s 爬取完成' % (provinces[i]))
            if res > 0:
                continue
            for city in cities[i]:
                sql = "insert into info_location(province, city, url) values (%s, %s, %s)"
                self.cursor.execute(sql, (provinces[i], city, city_dic[city].split(':')[1].strip('/')))
                self.conn.commit()


    def save_newhouse(self, item):
        select_sql = "select count(1) from newhouse where origin_url='%s';" % item['origin_url']
        self.cursor.execute(select_sql)
        res = self.cursor.fetchone()[0]
        if res > 0:
            return
        sql = 'insert into newhouse(province, city, district, name, address, origin_url, area, price, ' \
              'sale) ' \
              'values (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        self.cursor.execute(sql, (item['province'], item['city'], item['district'],
                                  item['name'], item['address'], item['origin_url'],
                                  item['area'], item['price'], item['sale']))
        self.conn.commit()


    def save_esf(self, item):
        select_sql = "select count(1) from esf where origin_url='%s';" % item['origin_url']
        self.cursor.execute(select_sql)
        res = self.cursor.fetchone()[0]
        if res > 0:
            return
        sql = 'insert into esf(province, city, name, rooms, floor, toward, address, origin_url, area, ' \
              'price, unit) ' \
              'values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        self.cursor.execute(sql, (item['province'], item['city'], item['name'],
                                  item['rooms'], item['floor'], item['toward'],
                                  item['address'],
                                  item['origin_url'],
                                  item['area'],
                                  item['price'],
                                  item['unit']))
        self.conn.commit()


    def save_info(self, item):
        select_sql = "select count(1) from info where domain='%s';" % item['domain']
        self.cursor.execute(select_sql)
        res = self.cursor.fetchone()[0]
        print('%s-%s信息爬取完成' % (item['province'], item['city']))
        value = [item['areaPrice'], item['esfareaPrice'], item['compareDate'], item['compareYear'],
                 item['minPrice'], item['maxPrice'], item['threeAreaPrice'],
                 item['threeEsfareaPrice'],
                 item['threeCompareDate'], item['threeCompareYear'], item['threeminPrice'],
                 item['threemaxPrice'], item['buildPriceNameList'], item['buildPriceCount'],
                 item['esfPriceNameList'], item['esfPriceCount'], item['domain'], item['new_avg'],
                 item['esf_avg'], item['new_cgreen'], item['esf_cgreen'], item['cid'], item['province'], item['city']]
        if res > 0:
            up_sql = "update info set areaPrice=%s, esfareaPrice=%s, compareDate=%s, " \
                     "compareYear=%s," \
                     "minPrice=%s, maxPrice=%s, threeAreaPrice=%s, threeEsfareaPrice=%s," \
                     "threeCompareDate=%s, threeCompareYear=%s,threeminPrice=%s, " \
                     "threemaxPrice=%s," \
                     "buildPriceNameList=%s, buildPriceCount=%s, esfPriceNameList=%s," \
                     "esfPriceCount=%s, domain=%s, new_avg=%s, esf_avg=%s, new_cgreen=%s, " \
                     "esf_cgreen=%s, cid=%s, province=%s, " \
                     "city=%s where domain=%s" \
                     ";"
            value.append(item['domain'])
            self.cursor.execute(up_sql, value)


        else:
            sql = "insert into info(areaPrice, esfareaPrice, compareDate, compareYear, minPrice, " \
                  "maxPrice, threeAreaPrice, threeEsfareaPrice, threeCompareDate, " \
                  "threeCompareYear, " \
                  "threeminPrice, threemaxPrice, buildPriceNameList, buildPriceCount, " \
                  "esfPriceNameList, esfPriceCount, domain, new_avg, esf_avg, new_cgreen, " \
                  "esf_cgreen, " \
                  "cid, province, city) values (%s, %s, %s, %s, %s, %s, " \
                  "%s, " \
                  "%s,%s, %s, %s, %s,%s, " \
                  "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (
                item['areaPrice'], item['esfareaPrice'], item['compareDate'], item['compareYear'],
                item['minPrice'], item['maxPrice'], item['threeAreaPrice'],
                item['threeEsfareaPrice'],
                item['threeCompareDate'], item['threeCompareYear'], item['threeminPrice'],
                item['threemaxPrice'], item['buildPriceNameList'], item['buildPriceCount'],
                item['esfPriceNameList'], item['esfPriceCount'], item['domain'], item['new_avg'],
                item['esf_avg'], item['new_cgreen'], item['esf_cgreen'], item['cid'], item['province'], item['city']
            ))
        self.conn.commit()



    def select_all_cities(self):
        select_sql = "select * from info_location;"
        self.cursor.execute(select_sql)
        res = self.cursor.fetchall()
        self.cursor.close()
        self.conn.close()
        return res
