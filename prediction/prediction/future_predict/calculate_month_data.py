import pandas as pd
import numpy as np


def calculate_month_data(data):
	data = np.array(data)
	for line in data:
		line[0] = line[0][0:7]
	return data
