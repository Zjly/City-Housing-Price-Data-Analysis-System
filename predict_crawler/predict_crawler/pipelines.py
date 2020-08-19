# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql


class PredictCrawlerPipeline:
	def __init__(self):
		# 建立数据库连接
		self.db = pymysql.connect("localhost", "root", "root", "house", charset="utf8")
		self.cur = self.db.cursor()
		truncate_sql = "TRUNCATE TABLE predict_house"
		self.cur.execute(truncate_sql)

	def process_item(self, item, spider):
		# sql语句存入数据库
		sql = "INSERT INTO predict_house(name, unit_price, total_price, unit_type, area, towards, floor, address, year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
		self.cur.execute(sql, (
		item['name'], item['unit_price'], item['total_price'], item['unit_type'], item['area'], item['towards'],
		item['floor'], item['address'], item['year']))
		self.db.commit()
		return item

	def close_spider(self, spider):
		# 关闭数据库
		self.cur.close()
		self.db.close()
