import numpy as np


def calculate_month_data(data):
	"""
	计算每月的情感值
	:param data:
	:return:
	"""
	# 去除日期的天信息
	data = np.array(data)
	for line in data:
		line[0] = line[0][0:7]

	# 建立月份列表
	months = []
	for line in data:
		if not line[0] in months:
			months.append(line[0])

	# 初始化统计列表
	data_total = []
	for month in months:
		data_total.append([month, 0, 0, 0])

	# 计算每月情感值
	for line in data:
		for month_data in data_total:
			if month_data[0] == line[0]:
				month_data[1] += float(line[1])
				month_data[2] += 1

	# 取每月情感平均值
	for month_data in data_total:
		month_data[3] = month_data[1] / month_data[2]

	return data_total
