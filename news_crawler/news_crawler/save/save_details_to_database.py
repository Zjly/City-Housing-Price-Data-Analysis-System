import json
import re

import MySQLdb

# 新建连接
db = MySQLdb.connect("localhost", "root", "root", "house", charset="utf8")
cursor = db.cursor()

# 清空数据库内原有内容
truncate_sql = "TRUNCATE TABLE sohu_news_details"
cursor.execute(truncate_sql)

with open("../links_sohu_news_details.json", "r", encoding="utf-8") as f:
	# 加载json文件
	json_data = json.load(f)
	for data in json_data:
		# 去除'符号
		content = data["content"].replace("\'", "")
		# 去除无法存入数据库的表情符号
		content = re.compile(u'[\U00010000-\U0010ffff\\uD800-\\uDBFF\\uDC00-\\uDFFF]').sub(u'', content)

		# 创建sql语句
		sql = "INSERT INTO sohu_news_details(title, time, content) VALUES ('%s', '%s', '%s')" % (
			data["title"], data["time"], content)
		cursor.execute(sql)

	try:
		db.commit()
	except:
		db.rollback()

db.close()
