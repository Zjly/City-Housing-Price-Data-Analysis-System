def get_month_data():
	"""
	得到新闻情感数据
	:return:
	"""
	# 打开数据库
	import MySQLdb

	db = MySQLdb.connect("localhost", "root", "root", "house", charset="utf8")
	cursor = db.cursor()

	# 取出新闻数据
	sql_content = "SELECT time, score FROM sohu_news_details"
	cursor.execute(sql_content)
	results = cursor.fetchall()

	# 关闭数据库
	db.close()

	return results


def get_month_price():
	"""
	得到月价格数据
	:return:
	"""
	# 打开数据库
	import MySQLdb

	db = MySQLdb.connect("localhost", "root", "root", "house", charset="utf8")
	cursor = db.cursor()

	# 取出新闻数据
	sql_content = "SELECT time, price FROM beijing_price"
	cursor.execute(sql_content)
	results = cursor.fetchall()

	# 关闭数据库
	db.close()

	return results
