from keras import Sequential
from keras.layers import Dense, LSTM, Dropout
from pandas import np


def emotion_price_model(data):
	"""
	模型训练
	:param data:
	:return:
	"""
	data = np.array(data)

	# 将数据转化为LSTM所接受的三维格式
	x_train = data[:52, 0].reshape((52, 1, 1))
	y_train = data[:52, 1].reshape((52, 1, 1))

	x_valid = data[53:, 0].reshape((2, 1, 1))
	y_valid = data[53:, 1].reshape((2, 1, 1))

	model = Sequential()
	model.add(LSTM(50, activation='relu', input_shape=(x_train.shape[1], x_train.shape[1]), return_sequences=True))
	model.add(Dropout(0.2))
	model.add(LSTM(32, activation="relu", return_sequences=True))
	model.add(Dropout(0.2))
	model.add(LSTM(16, activation="relu", return_sequences=True))
	model.add(Dropout(0.2))
	model.add(LSTM(8, activation="relu",  return_sequences=True))
	model.add(Dropout(0.2))
	model.add(Dense(1))
	model.compile(optimizer='adam', loss='mse')

	model.fit(x_train, y_train, epochs=1000, batch_size=2, validation_data=(x_valid, y_valid), verbose=2, shuffle=False)

	model.save('./model.h5')
