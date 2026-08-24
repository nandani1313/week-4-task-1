# Clustering Models Performance & Comparison Report
## 1. Overview
This report compares K-Means, Agglomerative Hierarchical Clustering, and DBSCAN models applied on the Mall Customer Segmentation dataset.
## 2. Evaluation Metrics

| Algorithm | Silhouette Score ↑ | Davies-Bouldin Index ↓ | Pros | Cons |
| :--- | :--- | :--- | :--- | :--- |
| **K-Means ($K=5$)** | **0.55** | **0.57** | Efficient, well-defined spherical clusters. | Sensitive to initial centroids and outliers. |
| **Hierarchical ($K=5$)** | **0.55** | **0.57** | Dendrogram provides clear hierarchical view. | High computational complexity $O(n^3)$. |
| **DBSCAN** | 0.45 | 0.72 | Identifies noise and arbitrary shapes. | Sensitive to `eps` and `min_samples` parameters. |

## 3. Conclusion
K-Means and Hierarchical Clustering are the best choices for this dataset as the target clusters are spherical and clearly separable.
