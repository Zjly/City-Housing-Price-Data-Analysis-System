# 打开数据库
import MySQLdb

db = MySQLdb.connect("localhost", "root", "root", "house", charset="utf8")
cursor = db.cursor()

# 取出新闻数据
sql_content = "SELECT id, time, score FROM sohu_news_details"
cursor.execute(sql_content)
results = cursor.fetchall()

# 关闭数据库
db.close()
