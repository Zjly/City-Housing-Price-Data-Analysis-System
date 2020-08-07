def emotion_analysis(news_cut_list):
	"""
	情感分析
	:param news_cut_list:
	:return:
	"""
	for sentence_cut_list in news_cut_list:
		news_id = sentence_cut_list[0]
		news_sentence_cut = sentence_cut_list[1]
		for sentence_list in news_sentence_cut:
			pass


def emotion_calculate(sentence_list):
	"""
	情感值计算
	:param sentence_list:
	:return:
	"""
	pass
