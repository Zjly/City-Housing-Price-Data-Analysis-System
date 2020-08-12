from prediction.price_predict.data_processing import data_processing
from prediction.price_predict.get_data import get_data
from prediction.price_predict.get_model import get_model

price_data = get_data()
price_data = data_processing(price_data)
model = get_model(price_data)
