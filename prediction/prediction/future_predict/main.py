from prediction.future_predict.calculate_month_data import calculate_month_data
from prediction.future_predict.get_month_data import get_month_data

if __name__ == '__main__':
	data = get_month_data()
	data = calculate_month_data(data)
