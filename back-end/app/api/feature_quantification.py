import pickle
import numpy as np
import sys


def feature_quantification(price_data):
	"""
	对特征进行处理
	:param price_data: 房价数据
	:return: 特征x
	"""
	x = price_data[["room", "hall", "area", "towards", "floor", "address", "year"]]

	# 取各个列
	towards = x["towards"]
	floor = x["floor"]
	address = x["address"]

	# 加载tokenizer并得到独热编码结果
	towards_result = load_tokenizer(towards, "towards")
	floor_result = load_tokenizer(floor, "floor")
	address_result = load_tokenizer(address, "address")

	# 各个特征的最值 后续进行均值化
	room_max = 6
	room_min = 1
	hall_max = 3
	hall_min = 0
	area_max = 353.1
	area_min = 23.0
	year_max = 2020
	year_min = 1995

	x = price_data[["room", "hall", "area", "year"]].values

	# 对数值特征进行均值化
	for line in x:
		line[0] = (int(line[0]) - room_min) / (room_max - room_min)
		line[1] = (int(line[1]) - hall_min) / (hall_max - hall_min)
		line[2] = (float(line[2]) - area_min) / (area_max - area_min)
		line[3] = (int(line[3]) - year_min) / (year_max - year_min)

	# 合并数值特征和标签特征
	x = np.hstack((x, towards_result, floor_result, address_result))

	return x


def label_quantification(price_data):
	"""
	对房价结果（标签）进行处理
	:param price_data: 房价数据
	:return: 标签y
	"""
	y = price_data[["total_price"]]
	y = y.values
	return y


def load_tokenizer(data, name):
	"""
	加载tokenizer并进行编码
	:param data: 待编码数据
	:param name: tokenizer名称
	:return: 独热编码后的特征列表
	"""
	print(sys.path)
	path = './app/api/tokenizer/' + name + '.pickle'
	with open(path, 'rb') as handle:
		tokenizer = pickle.load(handle)
		one_hot_results = tokenizer.texts_to_matrix(data, mode='binary')  # one_hot编码
		return one_hot_results
