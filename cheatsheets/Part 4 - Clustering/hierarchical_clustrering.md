# Hierarchical Clustering

## Intuition
TODO

Compared to K-means, Hierarchical clustering is generally slower, as it needs to know the distances between all pairs 
of clusters on each iteration, which at the start is all pairs of data points. 

## Applications
Taken from: Data Science for Business Provost

-  Very useful for data exploration. It allows the data analyst to see the groupings (the “landscape” of data similarity) 
before deciding on the number of clusters to extract.
    - Clipping the dendograms at a particular `y`, allows analysts to choose the number of clusters they want and
    visualize the content of the remaining clusters.
- Outlier detection: Points that cluster very high up in the dendogram by themselves can be considered outliers.
- "Find a similar Whiskey". If we had a dendogram of all whiskeys hierarchically clustered by flavour, given one whiskey you
could recommend a similar one following the dendogram.
