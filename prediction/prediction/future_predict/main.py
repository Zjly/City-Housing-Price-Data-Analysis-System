import json

from prediction.future_predict.calculate_month_data import calculate_month_data
from prediction.future_predict.data_processing import data_processing, data_input_convert
from prediction.future_predict.get_model import emotion_price_model
from prediction.future_predict.get_month_data import get_month_data, get_month_price
from keras.models import load_model
import numpy as np


def train_model():
	"""
	训练模型
	:return:
	"""
	data = get_month_data()
	emotion_data = calculate_month_data(data)
	price_data = get_month_price()
	data = data_processing(emotion_data, price_data)
	input_list, result_list = data_input_convert(data)
	emotion_price_model(input_list, result_list)


def model_predict():
	"""
	模型预测
	:return:
	"""
	# 得到模型
	model = load_model("./model.h5")

	# 得到data
	data = get_month_data()
	emotion_data = calculate_month_data(data)
	price_data = get_month_price()
	data = data_processing(emotion_data, price_data)
	input_list, result_list = data_input_convert(data)

	# 对之前的月份数据进行预测
	x = np.array(input_list)
	result = model.predict(x)
	result = result * 100000

	# 结果存入json文件之中
	data_json = []
	for i in range(55):
		data_json.append([emotion_data[54 - i][0], float(emotion_data[54 - i][3]), float(price_data[54 - i][1])])
	for i in range(len(result)):
		data_json[54 - i].append(result[len(result) - 1 - i][0])

	# 预测8月的房价
	x = [np.array([0.5817877272727275, 0.58150]), np.array([0.6018337209302325, 0.58435]),
		 np.array([0.5736101206896553, 0.58605]), np.array([0.5807723733333334, 0.58352]),
		 np.array([0.5846080277777779, 0.58227]), np.array([0.5351284893617021, 0.58096])]

	x = np.array(x).reshape((1, 6, 2))
	result = model.predict(x)
	result = result * 100000

	data_json.append(["2020-08", result[0][0]])
	with open("input.json", "wb") as f:
		json_str = json.dumps(data_json).encode()
		f.write(json_str)



if __name__ == '__main__':
	# train_model()
	model_predict()
