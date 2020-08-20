from predict import predict

data = ["3", "2", "94.5", "南向", "中层", "四新", "2016"]
unit_price, total_price = predict(data)
print(unit_price, total_price)