# Marked Basked Optimisation using Apriori Rule Learning

# We are going to use this implementation of the `apriori` algorithm: https://github.com/ymoch/apyori
# For this case, the source code is directly included in the same folder as this file.

# Importing the libraries
import pandas as pd


# Import the dataset
data_path = 'annotated-code/Part 5 - Association Rule Learning/Section 28 - Apriori/Market_Basket_Optimisation.csv'
dataset_frame = pd.read_csv(data_path, header=None)  # The data has no headers
# The Apyori algorithm expects a list of lists, not a dataframe
transactions = []
for row in dataset_frame.values:
    transactions.append([item for item in row if not pd.isnull(item)])


# Use the Apyori library
import sys # needed in this particular project to find the baked in apyori library
sys.path.insert(1, 'annotated-code/Part 5 - Association Rule Learning/Section 28 - Apriori')
from apyori import apriori
rules_generator = apriori(transactions, min_support=0.003, min_confidence=0.2, min_lift=3)
# Rules are lazily evaluated and generated here
# The rules returned by apyori are not ordered in any way
unordered_rules = list(rules_generator)


# Clean and sort the rules
# Apyori returns the rules in a messy data structure, this cleans it up
cleaned_rules = []
for rule in unordered_rules:
    cleaned_rules.append({
        'items_base': rule.ordered_statistics[0].items_base,
        'items_add': rule.ordered_statistics[0].items_add,
        'support': rule.support,
        'confidence': rule.ordered_statistics[0].confidence,
        'lift': rule.ordered_statistics[0].lift
    })
from operator import itemgetter
cleaned_sorted_rules = sorted(cleaned_rules, key=itemgetter('lift'), reverse=True)

# Store them in a dataframe for easier visualization
rules_df = pd.DataFrame(cleaned_sorted_rules, columns=['items_base', 'items_add', 'support', 'confidence', 'lift'])