from keras import Sequential
from keras.layers import Dense, LSTM, Dropout
from keras.callbacks import TensorBoard


def emotion_price_model(input_list, result_list):
	"""
	模型训练
	:param input_list:
	:param result_list:
	:return:
	"""
	# 划分数据集
	train_size = int(len(input_list) * 0.9)

	x_train = input_list[:train_size]
	y_train = result_list[:train_size]

	x_test = input_list[train_size:]
	y_test = result_list[train_size:]

	model = Sequential()
	model.add(LSTM(64, activation='relu', input_shape=(6, 2), return_sequences=True))
	model.add(Dropout(0.2))
	model.add(LSTM(32, activation="relu", return_sequences=True))
	model.add(Dropout(0.2))
	model.add(LSTM(16, activation="relu", return_sequences=True))
	model.add(Dropout(0.2))
	model.add(LSTM(8, activation="relu", return_sequences=False))
	model.add(Dropout(0.2))
	model.add(Dense(1))
	model.compile(optimizer='adam', loss='mse')

	model.fit(x_train, y_train, epochs=10000, batch_size=2, validation_data=(x_test, y_test), verbose=2, shuffle=False,
			  callbacks=[TensorBoard(log_dir='./log')])
	model.save('./model.h5')

	score = model.evaluate(x_test, y_test)
	print(score)
