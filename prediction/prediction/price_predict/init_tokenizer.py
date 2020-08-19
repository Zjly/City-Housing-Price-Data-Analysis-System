import pickle
from keras_preprocessing.text import Tokenizer


def init_tokenizer(price_data):
	"""
	初始化tokenizer
	:param price_data: dataFrame格式的价格数据
	:return:
	"""
	towards = price_data["towards"]
	floor = price_data["floor"]
	address = price_data["address"]

	save_tokenizer(towards, "towards")
	save_tokenizer(floor, "floor")
	save_tokenizer(address, "address")


def save_tokenizer(data, name):
	"""
	将tokenizer保存到文件
	:param data: 特征列
	:param name: 文件名
	:return:
	"""
	tokenizer = Tokenizer()  # 分词器
	tokenizer.fit_on_texts(data)  # 创建单词索引

	path = "./tokenizer/" + name + ".pickle"
	# 保存
	with open(path, 'wb') as handle:
		pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
