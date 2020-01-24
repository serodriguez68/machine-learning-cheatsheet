# K-means Clustering

## Intuition
Given a _number of clusters_, an _initialization point_ for each cluster centroid and a preferred _definition of distance_:
1. Assign each observation to the closest cluster by calculating the distance to the centroid 
using the given _definition of distance_.
2. Recalculate the centroid of each cluster averaging all the observations that belong to the cluster.
3. Repeat 1.  
 - If there are no re-assignments: stop.
 - If there are re-assignments: go to step 2.
 
 A gif is worth a million words:
 ![k-means clustering intuition](k_means_clustering_intuition.gif)


### Hyper-parameters
1. Number of clusters.
2. Definition of distance: Manhattan, euclidean, Minkowski, among many others.