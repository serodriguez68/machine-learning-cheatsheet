# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd

# Import the Dataset
data_path = 'annotated-code/Part 4 - Clustering/Section 24 - K-Means Clustering/Mall_Customers.csv'
dataset = pd.read_csv(data_path)
# In this example we will run clustering with only 2 variables so that we can visualize them.
X = dataset.iloc[:, [3, 4]].values  # Get all rows for columns 3 (annual income) and 4 (spending score)

# Use the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
# Try with 10 number of clusters
for i in range(1, 11):
    # random_state is fixed in this example to make sure the results match with the course
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)  # WCSS is called inertia_ in sklearn

plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()
n_clusters_opt = 5 # By eyeballing the graph, we conclude that the optimal number of clusters is 5

# Apply k-means to the dataset using the optimal number of clusters
kmeans = KMeans(n_clusters=n_clusters_opt, init='k-means++', max_iter=300, random_state=0)
# kmeans.fit_predict returns the an array with shape [n_samples, 1] with the cluster to where each observation belongs
# e.g. [0, 2, ...] means [cluster0, cluster2]. Note the cluster numbering is 0 based.
y_kmeans = kmeans.fit_predict(X)


# Visualizing the Clusters using a scatter plot (only works for 2D)
# Plotting high-dimensional problems can be done using dimensionality reduction techniques like PCA or LDA
colors = ['red', 'blue', 'green', 'cyan', 'magenta']
for cluster_num in range(0, n_clusters_opt):
    # X[y_kmeans == cluster_num, i] =>  get all rows in which y_kmeans == cluster_num from X (and the i-th column)
    plt.scatter(
        X[y_kmeans == cluster_num, 0],
        X[y_kmeans == cluster_num, 1],
        s=100,
        c=colors[cluster_num],
        label='Cluster ' + str(cluster_num + 1)
    )
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('Clusters of Clients')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (0-100)')
plt.legend()
plt.show()
