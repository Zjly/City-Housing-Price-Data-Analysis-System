import re
import numpy as np

import pandas as pd


def data_processing(price_data):
	"""
	对房价数据进行处理
	:param price_data: 处理后的房价数据
	:return:
	"""
	# 从tuple转化为ndarray
	price_data = np.array(price_data)

	# 建立data列表
	data_list = []
	for data in price_data:
		data = data_revise(data)

		if data is not None:
			data_list.append(data)

	# 转化为dataFrame
	price_data = pd.DataFrame(data_list,
							  columns=["id", "name", "unit_price", "total_price", "room", "hall", "area", "towards",
									   "floor",
									   "address", "year"])

	return price_data


def data_revise(data):
	"""
	对data进行修改
	:param data:
	:return:
	"""
	data = data.tolist()

	# 去除floor里面的总楼层信息
	data[7] = re.compile(r'（[^>]+）', re.S).sub('', data[7])

	# 去除地址信息中的详细部分
	data[8] = re.compile(r'-[^>]+', re.S).sub('', data[8])

	# 去除year的"年建"
	data[9] = data[9].replace("年建", "")

	# 将字符变量转化为数值变量
	data[2] = int(data[2])
	data[3] = float(data[3])
	data[5] = float(data[5])
	data[9] = int(data[9])

	# 排除年份
	if data[9] > 2020 or data[9] < 1995:
		return None

	# 将X室X厅分解
	rooms = data[4][0]
	halls = data[4][2]
	data[4] = rooms
	data.insert(5, halls)

	# 将字符变量转化为数值变量
	data[4] = int(data[4])
	data[5] = int(data[5])

	return data
