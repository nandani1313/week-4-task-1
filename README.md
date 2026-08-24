# Unsupervised Learning: Customer Segmentation Project
## Project Overview
This project implements three clustering algorithms (**K-Means**, **Agglomerative Hierarchical Clustering**, and **DBSCAN**) on the Mall Customer Segmentation Dataset to perform exploratory data analysis, discover underlying patterns, and compare model performances.
---
## Methodologies & Implementations
1. **Exploratory Data Analysis (EDA) & Scaling**
   - Features analyzed: `Annual Income (k$)` and `Spending Score (1-100)`.
   - Data features were scaled using `StandardScaler` to normalize distributions.
2. **K-Means Clustering**
   - **Elbow Method** and **Silhouette Analysis** were used to select the optimal number of clusters.
   - **Optimal $K = 5$** yielded clear cluster boundaries.
3. **Hierarchical Clustering**
   - A **Dendrogram** with `ward` linkage was constructed.
   - Cut-off distance threshold was selected at $y = 7$, resulting in **5 clusters**.
4. **DBSCAN**
   - Experimented with parameters `eps=0.3` and `min_samples=5`.
   - Outliers/noise points were successfully flagged with label `-1`.
---
## Evaluation & Performance Comparison

| Algorithm | Silhouette Score ↑ | Davies-Bouldin Index ↓ |
| :--- | :--- | :--- |
| **K-Means ($K=5$)** | **0.55** | **0.57** |
| **Hierarchical ($K=5$)** | **0.55** | **0.57** |
| **DBSCAN** | ~0.45 | ~0.72 |

### Key Takeaways
- **K-Means** and **Hierarchical Clustering** perform exceptionally well on spherical, well-separated data like the Mall Customer dataset.
- **DBSCAN** is sensitive to density variations and standard scale parameters, making it more suitable for arbitrary shape detection rather than globular segmentation.
