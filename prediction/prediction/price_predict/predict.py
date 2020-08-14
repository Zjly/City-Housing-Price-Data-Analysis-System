from keras.models import load_model

from prediction.price_predict.feature_quantification import feature_quantification
import pandas as pd
import numpy as np


def predict(data):
	"""
	预测房价
	:param data:
	:return: 房屋单价和总价
	"""
	# 对传输的数据进行处理
	data = np.array(data)
	data = pd.DataFrame(data, index=["room", "hall", "area", "towards", "floor", "address", "year"])
	data = pd.DataFrame(data.values.T, index=data.columns, columns=data.index)

	# 特征处理
	x = feature_quantification(data)
	x = x.astype('float64')

	# 加载模型
	model = load_model("./model.h5")

	# 进行预测
	total_price = model.predict(x)
	unit_price = total_price * 10000 / float(data["area"])
	return unit_price, total_price
