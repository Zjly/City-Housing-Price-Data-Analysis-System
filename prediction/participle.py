import re
import MySQLdb
import jieba as jieba


def participle():
	# 新建连接
	db = MySQLdb.connect("localhost", "root", "root", "house", charset="utf8")
	cursor = db.cursor()

	# 取出新闻数据
	sql_content = "SELECT content FROM sohu_news_details LIMIT 10"
	cursor.execute(sql_content)
	results = cursor.fetchall()

	# 各篇新闻划分列表
	news_cut_list = []

	# 进行分词
	for news in results:
		# 取得新闻内容
		news = news[0]

		# 去除标点符号
		news = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，？、~@#￥%……&*（）《》“”:：]+", "", news)

		# 划分为句子
		sentence_list = news.split("。")

		# 一篇新闻内各个句子划分列表
		sentence_cut_list = []

		# 对每句话进行分词
		for sentence in sentence_list:
			cut = jieba.cut(sentence)
			cut_list = [i for i in cut]
			sentence_cut_list.append(cut_list)

		news_cut_list.append(sentence_cut_list)

	db.close()

	return news_cut_list
