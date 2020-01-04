# Data Preprocessing

## Pre-processing Libraries
There are a few critical libraries that are used for data preprocessing and machine learning in general.
Here is a short summary of those and what they do:
1. Numpy - Manipulation for multi-dimensional arrays and matrices.
2. Pandas - Data import and manipulation.
3. Matplotlib - Data visualization.

## Importing CSV Datasets
- We use pandas to import tabular CSV datasets. The imported data is held in
a pandas `dataframe`.
- We then split the `dataframe` into _independent_ and _dependent_ variables
to proceed with any supervised ML task.
```python
dataset = pd.read_csv('some/data/path/data.csv')
# iloc allows us to locate columns by their index in Pandas dataframes
X = dataset.iloc[:, :-1].values  # All Rows, All Columns except last one
Y = dataset.iloc[:, 3].values
```

## Handling Missing Data
Missing data happens very frequently in machine learning. Options for handling missing data are:

### Removing the observations with missing data
 - Pros: Very simple.
 - Cons: You lose valuable data from other columns.
  
### Replacing numerical missing values with the mean of the column
 - Pros: Simple. Keeps the data from other columns.
 - Cons: A bit arbitrary. Do not use when you have a lot of missing data. Not applicable to categorical data.
 - There are other strategies in addition to `mean` (e.g. `most_frequent`). These other strategies
  can also make sense depending on the context.
```python
from sklearn.impute import SimpleImputer
# SimpleImputer is a transformer to deal with missing values
# - missing_values is the placeholder for missing values on our dataset
# - strategy to replace missing values
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
X[:, 1:3] = imp_mean.fit_transform(X[:, 1:3])
```

### Replacing missing values using prediction (Prediction Imputation)
 - Intuition: 
     - Use your column with missing data as a dependent variable.
     - Split your dataset into 2 sets "Training" and "Missing", where "Training" contains all data __without__ missing values on the
     dependent variable and "Missing" contains all data where the dependent variable contains missing values.
     - Train a ML model on the "Training" set and use it to fill in the missing values on the "Missing" set. 
     Typically a simple model like k-NN is used.
     - Your new data set will be "Training" + "Predicted Missing"
     - Note that the above usage of Train / "Missing" data is DIFFERENT to what you would do on a regular ML case in which a
     labelled Test is used to assess performance and avoid overfitting. In Prediction Imputation we are more
     relaxed and don't really sub-divide the labelled data into Train/Test or do k-fold cross validation. However, we
     could do this if we wanted to.
  - Pros: Much more statistically sound approach that takes into account the other variables. Handles missing values
  in both __numerical__ and __categorical__ variables.
  - Cons: It is more complex. You may run into "chicken and egg" issues if you have multiple columns with missing values.

## Encoding Categorical Data
**Why we need to do this:**  ML models are based on mathematical models that do not support anything that is not a number.
Therefore, we need to express categorical data as numbers somehow. 

### Mapping categories to numbers
e.g. France => 0, Spain => 1, UK => 2

**WARNING:** This typically does NOT make sense since it forces the ML algorithms to think that there is some sort
of order and a sense magnitude between categories. e.g. `France < Spain < UK` and `Spain * 2 = UK`. 

This _may_ make sense for categorical values that imply some sort of order (like T-shirt sizes), but even under those
circumstances the sense of magnitude (`small * 3 = large`) is questionable.

```python
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
``` 

### One-hot encoding
This is typically what should be used with non-binary categorical variables.
```python
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(), [0])],    # The column numbers to be transformed (here is [0] but can be [0, 1, 3])
    remainder='passthrough'                         # Leave the rest of the columns untouched
)
X = ct.fit_transform(X)
```

### Binary encoding
When the categorical value is binary (e.g. True, False), then transformation to 0 and 1 is ok.
```python
from sklearn.preprocessing import LabelEncoder
y = ['Yes', 'No', 'Yes']
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
```

## Splitting the Dataset into the Training set and Test set
- Train / Test splitting is done to assess performance and overfitting.
- Ideally, the performance on the Test set is very similar than the one on the Training set.
- The test set is usually around 20% to 25% of the whole dataset.
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```