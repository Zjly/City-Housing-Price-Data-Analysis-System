import re
import numpy as np

import pandas as pd


def data_processing(price_data):
	"""
	对房价数据进行处理
	:param price_data: 处理后的房价数据
	:return:
	"""
	price_data = np.array(price_data)

	for data in price_data:
		data_revise(data)

	# 转化为dataFrame
	price_data = pd.DataFrame(price_data,
							  columns=["id", "name", "unit_price", "total_price", "unit_type", "area", "towards",
									   "floor",
									   "address", "year"])

	return price_data


def data_revise(data):
	"""
	对data进行修改
	:param data:
	:return:
	"""
	# 去除floor里面的总楼层信息
	data[7] = re.compile(r'（[^>]+）', re.S).sub('', data[7])

	# 去除地址信息中的详细部分
	data[8] = re.compile(r'-[^>]+', re.S).sub('', data[8])

	# 去除year的"年建"
	data[9] = data[9].replace("年建", "")
