from prediction.price_predict.data_processing import data_processing
from prediction.price_predict.feature_quantification import feature_quantification
from prediction.price_predict.get_data import get_data
from prediction.price_predict.get_model import get_model
from prediction.price_predict.init_tokenizer import init_tokenizer


def train_model():
	"""
	训练模型
	:return:
	"""
	price_data = get_data()
	price_data = data_processing(price_data)
	# init_tokenizer(price_data)
	x, y = feature_quantification(price_data)
	get_model(x, y)


if __name__ == '__main__':
	train_model()
