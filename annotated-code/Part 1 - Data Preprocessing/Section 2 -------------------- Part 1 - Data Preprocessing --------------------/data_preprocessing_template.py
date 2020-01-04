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
y = dataset.iloc[:, 3].values

# Handling Missing Data
from sklearn.impute import SimpleImputer
# SimpleImputer is a transformer to deal with missing values
# - missing_values is the placeholder for missing values on our dataset
# - strategy to replace missing values
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
X[:, 1:3] = imp_mean.fit_transform(X[:, 1:3])


# Encoding Categorical Data
## Mapping categories to numbers
# from sklearn.preprocessing import LabelEncoder
# labelencoder_X = LabelEncoder()
# X[:, 0] = labelencoder_X.fit_transform(X[:, 0])

## One-hot encoding
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(), [0])],    # The column numbers to be transformed (here is [0] but can be [0, 1, 3])
    remainder='passthrough'                         # Leave the rest of the columns untouched
)
X = ct.fit_transform(X)

## Binary encoding
from sklearn.preprocessing import LabelEncoder
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Splitting the Dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
# random_state is fixed here just to make sure the results match the ones in the udemy course,
# we wouldn't fix a random_state in regular circumstances
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 0)
