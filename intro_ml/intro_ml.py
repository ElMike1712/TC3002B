import pandas as pd


# LOADING DATA
melbourne_file_path = 'intro_ml/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
#print(melbourne_data.columns())

# CHOSING FEATURES
y = melbourne_data.Price

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

#print(X.describe())

# BUILDING THE MODEL
from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)

# MAKING PREDICTIONS
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))