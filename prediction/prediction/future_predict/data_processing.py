def data_processing(emotion_data, price_data):
	"""
	数据处理
	:param emotion_data:
	:param price_data:
	:return:
	"""
	data = []
	for i in range(55):
		data.append([float(emotion_data[54-i][3]), float(price_data[54-i][1])])

	return data
