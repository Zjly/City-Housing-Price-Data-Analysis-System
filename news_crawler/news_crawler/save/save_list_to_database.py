import json
import re

import MySQLdb

# 新建连接
db = MySQLdb.connect("localhost", "root", "root", "house", charset="utf8")
cursor = db.cursor()

# 清空数据库内原有内容
truncate_sql = "TRUNCATE TABLE sohu_news_list"
cursor.execute(truncate_sql)

with open("../links_sohu_news_list.json", "r", encoding="utf-8") as f:
	# 加载json文件
	json_data = json.load(f)
	for data in json_data:
		title = data["title"].replace("\'", "")
		# 创建sql语句
		sql = "INSERT INTO sohu_news_list(title, link) VALUES ('%s', '%s')" % (
			data["title"], data["link"])
		cursor.execute(sql)

	try:
		db.commit()
	except:
		db.rollback()

db.close()
