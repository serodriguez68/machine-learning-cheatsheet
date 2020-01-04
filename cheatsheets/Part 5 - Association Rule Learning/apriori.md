# Apriori

## Intuition
- People who bought X also bought Y
- People who watched X also watched Y
- People who did X also did Y

Here is the typical shape of the data: 
![Apriori intuition](./apriori-intuition.png)

### Mathematical Components
#### Support

How likely it is for a random person to buy `Item`. 

`support(Item) = #_transactions_containing_Item / #_of_transactions`
 

#### Confidence

Assuming we are testing the rule `Item1 -> Item2`, how likely it is for a person that bought `Item1` to buy `Item2`.

`confidence(Item1 -> Item2) = #_transactions_containing_Item1_and_Item2 / #_of_transactions_containing_Item1 = P(Item2 | Item1)`

#### Lift

How much more likely is it for person that bought `Item1` to buy `Item2`, compared to how likely is it to buy `Item2` randomly.

`lift(Item1 -> Item2) = confidence(Item1 -> Item2) / support(Item2)`

- A `lift = 1` in the rule `Item1 -> Item2` means that there is no improvement in the probability of buying `Item2` given
that a person has selected `Item1`.
- A `lift > 1` means that people that bought `Item1` are more likely to buy `Item2` than a random person.
- A `lift < 1` means that people that bought `Item1` are less likely to buy `Item2` than a random person.


### Steps

Among all the possible items we sell / movies we offer, we want to find the rules that have the highest (or lowest) lift
so that we can exploit that knowledge.

The `Apriori` algorithm does this for not just pairs, but also higher order associations like `Bread & Cheese -> Ham`. 

In a naive implementation, `Apriori` would be very slow algorithm because in principle it would need to go through 
all the possible combinations of n-order rules. 
Luckily, the algorithm is smarter than that and is able o prune the search space if we give it a minimum support and confidence.

- Step 1: Set a minimum support and confidence.
- Step 2: Take all the subsets in transactions having `support > min_support`. 
  - e.g. If there are only a few transactions for `ItemRare`, then don't bother trying to find rules for it. 
- Step 3: Take all the rules of these subsets having `confidence > min_confidence`.
  - Prune out rules that don't have strong signals.
- Step 4: Sort rules by decreasing lift.
  - The rule with the highest lift is the strongest one.
  - We typically take the top 5 or top 10 and act on them.
  
### Recommender Systems
`Apriori` is a simple way of creating a basic recommender systems. However, world-class recommender systems
use much more complex models that may use `apriori` data as part of their features. 