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
2. Definition of distance: Manhattan, Euclidean, Minkowski, among many others.

### Pitfall: The Random Initialization Trap

In a _vanilla_ implementation of the k-means algorithm, __the result of the algorithm is dependent on the
initialization points for the centroids__. The following picture shows why:

![k-means random initialization trap](k-means-random-initialization-trap.png)

#### How to combat this?
There is a variation of the algorithm called the [k-means++ algorithm](https://en.wikipedia.org/wiki/K-means%2B%2B)
which fixes this problem.

The course did not explain how it works. But, the good news is that most of the tools already implement this
variant so __we just need to make sure that we are using uses the _kmeans++_ variant__.  For example:
- R includes k-means, and the "flexclust" package can do k-means++
- Scikit-learn has a K-Means implementation that uses k-means++ by default.
- Weka contains k-means (with optional k-means++) and x-means clustering.
- Notably, at the time of this writing [Knime did not have the kmeans++ algorithm](https://forum.knime.com/t/accuracy-of-k-means-clustering/12721).