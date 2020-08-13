import keras  # 导入Keras
from keras.models import Sequential  # 导入序贯模型
from keras.layers import Dense, Dropout  # 导入全连接层
from keras.optimizers import SGD  # 导入优化函数
from keras_preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split



def feature_quantification(x):
	print(x["towards"].value_counts())
	x = x["towards"]

	tokenizer = Tokenizer()  # 分词器，处理前1000高频出现的单词
	tokenizer.fit_on_texts(x)  # 创建单词索引
	sequences = tokenizer.texts_to_sequences(x)  # 把单词转换为序列
	one_hot_results = tokenizer.texts_to_matrix(x, mode='binary')  # one_hot编码
	word_index = tokenizer.word_index  # 单词索引表



	a = keras.utils.to_categorical(x[3], 10)
	return a


def get_model(price_data):
	x = price_data[["room", "hall", "area", "towards", "floor", "address", "year"]]
	y = price_data[["unit_price"]]
	x = feature_quantification(x)

	x_train, y_train, x_test, y_test = train_test_split(x, y, test_size=0.3)

	# model = Sequential()
	# model.add(Dense(512, activation="relu"))
	# model.add(Dropout(0.2))
	# model.add(Dense(256, activation="relu"))
	# model.add(Dropout(0.2))
	# model.add(Dense(10, activation='softmax'))
	# model.compile(optimizer=SGD(), loss='categorical_crossentropy', metrics=['accuracy'])
	#
	# # 训练模型
	# model.fit(x=x_train, y=y_train, batch_size=32, epochs=100, verbose=1, callbacks=None, validation_split=0.2,
	# 		  validation_data=None, shuffle=True, class_weight=None, sample_weight=None, initial_epoch=0,
	# 		  steps_per_epoch=None, validation_steps=None)
	pass
