from keras.models import Sequential  # 导入序贯模型
from keras.layers import Dense, Dropout  # 导入全连接层
from keras.optimizers import SGD  # 导入优化函数
from sklearn.model_selection import train_test_split
from keras.wrappers.scikit_learn import KerasRegressor


def get_model(x, y):
	"""
	训练模型
	:param x:
	:param y:
	:return:
	"""
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

	model = Sequential()
	model.add(Dense(512, activation='relu', input_shape=(x_train.shape[1], )))
	model.add(Dropout(0.2))
	model.add(Dense(256, activation="relu"))
	model.add(Dropout(0.2))
	model.add(Dense(128, activation="relu"))
	model.add(Dropout(0.2))
	model.add(Dense(64, activation="relu"))
	model.add(Dropout(0.2))
	model.add(Dense(1))
	model.compile(loss='mean_squared_error', optimizer='adam')

	# 训练模型
	model.fit(x=x_train, y=y_train, batch_size=16, epochs=10, verbose=1, callbacks=None, validation_split=0.2,
			  validation_data=None, shuffle=True, class_weight=None, sample_weight=None, initial_epoch=0,
			  steps_per_epoch=None, validation_steps=None)

	score = model.evaluate(x_test, y_test, batch_size=16)
	print(score)

	return model
