import pickle
import json
import numpy as np


class UtilOperations:
	def __init__(self):
		self.model_path = "artifacts/banglore_home_prices_model.pickle"
		self.columns_path = "artifacts/columns.json"

	def get_estimated_price(self,location,sqft,bhk,bath):
		data_columns = self.get_data_columns()
		model = None

		with open(self.model_path, 'rb') as f:
			model = pickle.load(f)
		try:
			loc_index = data_columns.index(location.lower())
		except:
			loc_index = -1

		x = np.zeros(len(data_columns))
		x[0] = sqft
		x[1] = bath
		x[2] = bhk
		if loc_index>=0:
			x[loc_index] = 1

		return round(model.predict([x])[0],2)


	def get_location_names(self):
		with open(self.columns_path, "r") as f:
			data_columns = json.load(f)['data_columns']
			locations = data_columns[3:]  # first 3 columns are sqft, bath, bhk
		return locations


	def get_data_columns(self):
		with open("artifacts/columns.json", "r") as f:
			data_columns = json.load(f)['data_columns']
		return data_columns

# if __name__ == '__main__':
# 	util = UtilOperations()
# 	print(util.get_location_names())
# 	print(util.get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
