import MySQLdb


def get_data():
	"""
	从数据库中得到数据
	:return: 新闻数据列表
	"""
	# 打开数据库
	db = MySQLdb.connect("localhost", "root", "root", "house", charset="utf8")
	cursor = db.cursor()

	# 取出新闻数据
	# sql_content = "SELECT id, title, content FROM sohu_news_details ORDER BY RAND() LIMIT 10"
	sql_content = "SELECT id, title, content FROM sohu_news_details"
	cursor.execute(sql_content)
	results = cursor.fetchall()

	# 关闭数据库
	db.close()

	return results
