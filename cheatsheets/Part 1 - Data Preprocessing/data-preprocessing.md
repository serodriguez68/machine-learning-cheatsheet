# Pre-processing Libraries
There are a few critical libraries that are used for data preprocessing and machine learning in general.
Here is a short summary of those and what they do:
1. Numpy - Manipulation for multi-dimensional arrays and matrices.
2. Pandas - Data import and manipulation.
3. Matplotlib - Data visualization.

# Importing CSV Datasets
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

# Handling Missing Data
Missing data happens very frequently in machine learning. Options for handling missing data are:

1. **Removing the observations with missing data**
 - Pros: Very simple.
 - Cons: You lose valuable data from other columns.
  
2. **Replacing numerical missing values with the mean of the column**
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

3. **Replacing missing values using prediction (Prediction Imputation)**
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

# Encoding Categorical Data

