# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the dataset
data_path = 'annotated-code/Part 1 - Data Preprocessing/Section 2 -------------------- Part 1 - Data Preprocessing --------------------/Data.csv'
dataset = pd.read_csv(data_path)
# iloc allows us to locate columns by their index in Pandas dataframes
X = dataset.iloc[:, :-1].values  # All Rows, All Columns except last one
Y = dataset.iloc[:, 3].values

# Handling Missing Data
from sklearn.impute import SimpleImputer
# SimpleImputer is a transformer to deal with missing values
# - missing_values is the placeholder for missing values on our dataset
# - strategy to replace missing values
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
X[:, 1:3] = imp_mean.fit_transform(X[:, 1:3])
