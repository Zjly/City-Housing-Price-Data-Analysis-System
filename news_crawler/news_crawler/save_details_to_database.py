import json

import MySQLdb

db = MySQLdb.connect("localhost", "root", "root", "house")
cursor = db.cursor()

# 清空数据库内原有内容
truncate_sql = "TRUNCATE TABLE sohu_news_details"
cursor.execute(truncate_sql)

with open("links_sohu_news_details.json", "r", encoding="utf-8") as f:
	json_data = json.load(f)
	for data in json_data:
		sql = "INSERT INTO sohu_news_details(title, time, content) VALUES ('%s', '%s', '%s')" % (
			data["title"], data["time"], data["content"])
		cursor.execute(sql)

	try:
		db.commit()
	except:
		db.rollback()
