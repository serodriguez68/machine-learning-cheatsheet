# Eclat

## Intuition
- Eclat is a very simple version of association "rule" learning that only uses `support`.
- The output of the algorithm is the *frequent itemsets*.
  - i.e. The sets of products that are frequently bought together and that are above a given `min_support`
  - It is like truncating at Step 2 in the [apriori algorithm](apriori.md).
  - e.g. an output will look like: `{eggs, milk, chicken}`. Note that this is NOT a rule strictly speaking.
  - The output tends to be obvious and it is heavily influenced by the high frequency items.
    - e.g. If _bread, coffee_ and _butter_ are very high frequency items, many of the *frequent itemsets* will be subsets
    of those 3 or contain one of them.
    - Output needs to be manually checked to identify some unexpected *frequent itemsets*.

See the [apriori algorithm](apriori.md) cheat sheet for the definition of `support`.

## Steps
- Step 1: Set a minimum support.
- Step 2: Find the *Frequent Itemsets*. i.e. all the itemsets having `support > min_support`.
- Step 3: Sort *Frequent Itemsets* by decreasing support.

## Code
The Udemy couse did not cover Eclat for python. Google it!