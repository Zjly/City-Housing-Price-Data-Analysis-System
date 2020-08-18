from keras.models import load_model


def predict():
	"""
	模型预测
	:return:
	"""
	model = load_model("./model.h5")
	result = model.predict([[[0.650986]]])
	print(result)
