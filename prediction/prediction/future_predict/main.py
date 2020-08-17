from prediction.future_predict.calculate_month_data import calculate_month_data
from prediction.future_predict.data_processing import data_processing
from prediction.future_predict.emotion_price_predict import emotion_price_model
from prediction.future_predict.get_month_data import get_month_data, get_month_price
from prediction.future_predict.predict import predict


def train_model():
	"""
	训练模型
	:return:
	"""
	data = get_month_data()
	emotion_data = calculate_month_data(data)
	price_data = get_month_price()
	data = data_processing(emotion_data, price_data)
	emotion_price_model(data)


def model_predict():
	"""
	模型预测
	:return:
	"""
	predict()


if __name__ == '__main__':
	# train_model()
	model_predict()
