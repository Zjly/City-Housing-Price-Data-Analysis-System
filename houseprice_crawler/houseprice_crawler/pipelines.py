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
from houseprice_crawler.items import NewHouseItem, ESFHouseItem


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
        if isinstance(item, NewHouseItem):
            self.save_newhouse(item)
        elif isinstance(item, ESFHouseItem):
            self.save_esf(item)
        return item


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
