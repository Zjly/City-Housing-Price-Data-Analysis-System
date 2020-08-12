import math

from emotion.emotion_word import pos_envalute, pos_emotion, most_degree, very_degree, more_degree, ish_degree, \
	least_degree, neg_degree, neg_envalute, neg_emotion


def emotion_analysis(news_cut_list):
	"""
	情感分析
	:param news_cut_list:
	:return:
	"""
	emotion_data = []
	for sentence_cut_list in news_cut_list:
		news_id = sentence_cut_list[0]
		news_title = sentence_cut_list[1]
		news_sentence_cut = sentence_cut_list[2]

		# 计算标题情感得分
		title_score = emotion_calculate(news_title)
		title_score = score_mapping(title_score)

		# 计算内容情感得分
		content_score = 0
		# sentence_list为单句中的分词列表
		for sentence_list in news_sentence_cut:
			# 单句分数统计
			sentence_score = emotion_calculate(sentence_list)
			content_score += sentence_score

		content_score = content_score / len(news_sentence_cut)
		content_score = score_mapping(content_score)

		news_score = title_score * 0.2 + content_score * 0.8
		emotion_data.append([news_id, news_score])

	return emotion_data


def emotion_calculate(sentence_list):
	"""
	情感值计算
	:param sentence_list: 单句分词列表
	:return: 单句情感分数
	"""
	sentence_score = 0

	# 对每一个词语进行分析
	for i in range(len(sentence_list)):
		# 取前中后三个词语
		if i != 0:
			last_word = sentence_list[i - 1]
		else:
			last_word = None
		current_word = sentence_list[i]
		if i != len(sentence_list) - 1:
			next_word = sentence_list[i + 1]
		else:
			next_word = None

		# 词性为积极
		if current_word in (pos_envalute or pos_emotion):
			score = 0
			# 判断前一词语 得到程度副词评分
			score += get_degree_score(last_word)

			# 不是程度副词
			if get_degree_score(last_word) == 0:
				# 判断是否为消极词
				if (last_word in (neg_envalute or neg_emotion)) or (next_word in (neg_envalute or neg_emotion)):
					score += -1
				else:
					score += 1

			sentence_score += score

		# 词性为消极
		elif current_word in (neg_envalute or neg_emotion):
			score = 0
			# 判断前一词语 得到程度副词评分
			score += -get_degree_score(last_word)

			# 不是程度副词
			if get_degree_score(last_word) == 0:
				score += -1

			sentence_score += score * math.e

	return sentence_score


def get_degree_score(word):
	"""
	得到词语程度副词的分数
	:param word: 当前词语
	:return: 程度副词的分数
	"""
	if word in most_degree:
		return 3
	elif word in very_degree:
		return 2
	elif word in more_degree:
		return 1.5
	elif word in ish_degree:
		return 0.75
	elif word in least_degree:
		return 0.5
	elif word in neg_degree:
		return -1
	else:
		return 0


def score_mapping(score):
	"""
	将情感得分映射到(0, 1)之间
	:param score: 情感得分
	:return: 映射结果
	"""
	return 1 / (1 + math.pow(math.e, -score))
