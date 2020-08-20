import json
import numpy as np


def data_processing(emotion_data, price_data):
	"""
	数据处理
	:param emotion_data:
	:param price_data:
	:return:
	"""
	data = []
	data_json = []
	for i in range(55):
		data.append([float(emotion_data[54 - i][3]), float(price_data[54 - i][1])])
		data_json.append([emotion_data[54 - i][0], float(emotion_data[54 - i][3]), float(price_data[54 - i][1])])

	with open("data.json", "wb") as f:
		json_str = json.dumps(data_json).encode()
		f.write(json_str)

	return data


def data_input_convert(data):
	"""
	数据输入转化Multiple Input
	:param data:
	:return:
	"""
	# 输入值1与2
	in_seq1 = []
	in_seq2 = []
	for line in data:
		in_seq1.append(line[0])
		in_seq2.append(line[1] / 100000)

	# 得到对应列表
	seq_list = [[in_seq1[i], in_seq2[i]] for i in range(len(in_seq1))]

	# 每个特征的长度
	step = 6

	# 得到输入列表
	input_list = []
	for i in range(len(seq_list) - step):
		p_list = []
		for j in range(step):
			p_list.append(np.array(seq_list[i + j]))
		input_list.append(np.array(p_list))

	# 得到结果列表
	result_list = []
	for i in range(len(seq_list) - step):
		result_list.append(in_seq2[step + i])

	# 转化为array
	input_list = np.array(input_list)
	result_list = np.array(result_list)

	return input_list, result_list
