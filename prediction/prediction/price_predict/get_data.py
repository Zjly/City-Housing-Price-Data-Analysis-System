import MySQLdb


def get_data():
	"""
	从数据库中取数据
	:return: 房价数据
	"""
	db = MySQLdb.connect("localhost", "root", "root", "house", charset="utf8")
	cursor = db.cursor()

	# 取出房价数据
	sql_content = "SELECT id, name, unit_price, total_price, unit_type, area, towards, floor, address, year FROM predict_house"
	cursor.execute(sql_content)
	results = cursor.fetchall()

	# 关闭数据库
	db.close()

	return results
