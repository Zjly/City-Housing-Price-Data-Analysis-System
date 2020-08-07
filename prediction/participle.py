import re
import jieba as jieba


def participle(data):
	"""
	对新闻列表中的新闻进行分词
	:return: news_cut_list[news_id, sentence_cut_list] 所有新闻的分词列表 -> sentence_cut_list 单篇新闻内的分词列表 -> cut_list 单句话的分词列表
	"""
	# 各篇新闻划分列表
	news_cut_list = []

	# 进行分词
	for news in data:
		news_id = news[0]
		# 取得新闻内容
		news = news[1]

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

		news_cut_list.append([news_id, sentence_cut_list])

	return news_cut_list
