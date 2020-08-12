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


def save_emotion_score(emotion_data):
	"""
	将情感分析结果存入数据库
	:param emotion_data: 情感分析数据
	:return:
	"""
	# 打开数据库
	db = MySQLdb.connect("localhost", "root", "root", "house", charset="utf8")
	# db = MySQLdb.connect(host="121.36.253.244", port=3306, user="root", password="root", db="houseprice", charset="utf8")
	cursor = db.cursor()

	# 修改每条新闻的分数
	for data in emotion_data:
		sql_content = "UPDATE sohu_news_details SET score = '%f' WHERE id = '%s'" % (data[1], data[0])
		cursor.execute(sql_content)

	try:
		db.commit()
	except:
		db.rollback()

	db.close()
