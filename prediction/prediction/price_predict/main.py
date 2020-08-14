from prediction.price_predict.data_processing import data_processing
from prediction.price_predict.feature_quantification import feature_quantification, label_quantification
from prediction.price_predict.get_data import get_data
from prediction.price_predict.get_model import get_model
from prediction.price_predict.init_tokenizer import init_tokenizer
from prediction.price_predict.predict import predict


def train_model():
	"""
	训练模型
	:return:
	"""
	price_data = get_data()
	price_data = data_processing(price_data)
	# init_tokenizer(price_data)
	x = feature_quantification(price_data)
	y = label_quantification(price_data)
	get_model(x, y)


def model_predict():
	"""
	模型预测
	:return:
	"""
	data = ["3", "2", "94.5", "南向", "中层", "四新", "2016"]
	unit_price, total_price = predict(data)
	print(data)
	print("房屋单价: " + str(unit_price[0][0]) + "元/平方米, 房屋总价: " + str(total_price[0][0]) + "万元")


if __name__ == '__main__':
	# train_model()
	model_predict()
