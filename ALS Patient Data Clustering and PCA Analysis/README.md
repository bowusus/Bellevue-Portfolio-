# ALS Patient Data Clustering and PCA Analysis
## Overview
This project applies K-means clustering and Principal Component Analysis (PCA) to an anonymized dataset of ALS (Amyotrophic Lateral Sclerosis) patients. The aim is to uncover meaningful patterns in the data and categorize patients into distinct clusters based on their clinical and physiological characteristics. The analysis provides insights that can guide future research into ALS progression and potential interventions.

## Key Features
Data Cleaning:

Removed irrelevant columns (e.g., ID, SubjectID) to focus on features directly related to ALS progression.
Standardized the data using StandardScaler for optimal clustering performance.
K-means Clustering:

Evaluated clustering performance for 2–10 clusters using silhouette scores.
Identified the optimal number of clusters as 2, based on the highest silhouette score.
PCA Transformation:

Reduced the dataset to two principal components for visualization.
Plotted clusters in 2D space to assess separation and clustering quality.

## Technologies Used
Programming Language: Python
Libraries:
pandas: Data manipulation and preprocessing.
numpy: Numerical computations.
scikit-learn: Clustering algorithms, scaling, and PCA.
matplotlib: Data visualization.

## How to Run the Project
Prerequisites
Install Python 3.x.
Install the required Python libraries:
pip install pandas numpy scikit-learn matplotlib
Steps:
Prepare the Dataset:
Ensure the dataset file als_data.csv is in the project directory.
Run the Code:
Execute the Python script or Jupyter Notebook to perform the following steps:
Clean and scale the data.
Determine the optimal number of clusters.
Apply K-means clustering and visualize the results using PCA.
Outputs:
Silhouette score plot for determining the optimal number of clusters.
PCA scatter plot showing clusters in 2D space.

## Key Steps in the Analysis
1. Data Cleaning
Removed non-ALS-related columns (ID, SubjectID).
Kept relevant features, such as ALS-related scores and physiological measures.
2. Data Scaling
Used StandardScaler to normalize the data, ensuring features are on the same scale.
3. Silhouette Analysis
Calculated silhouette scores for cluster counts ranging from 2 to 10.
Determined the optimal number of clusters to be 2.
4. K-means Clustering
Applied the K-means algorithm with n_clusters=2.
Assigned each patient to one of the two clusters.
5. PCA Transformation and Visualization
Reduced the dataset dimensions to 2 using PCA.
Visualized the clusters with a 2D scatter plot, where:
Yellow points represent Cluster 0.
Purple points represent Cluster 1.

## Key Findings
Optimal Clusters:
The silhouette score plot confirmed that 2 clusters provided the most distinct separation in the dataset.
Cluster Assignments:
Patients were divided into two clusters, representing distinct profiles or ALS progression patterns.
PCA Insights:
The primary separation between clusters was along PCA Feature 1, indicating it captures the most significant variance in the data.

## Lessons Learned
What Worked Well:
PCA effectively reduced dimensionality, enabling clear visualization of the clusters.
Silhouette scores provided a reliable method for choosing the optimal number of clusters.
What Could Be Improved:
Investigating the specific characteristics of each cluster to better understand the patterns.
Incorporating additional features, such as demographic or genetic data, for deeper analysis.

## Future Directions
Cluster Analysis:
Examine the characteristics of each cluster to determine distinguishing factors.
Use clustering results to tailor potential ALS treatments or interventions.
Feature Engineering:
Explore new features that may enhance clustering quality and interpretability.
Advanced Methods:
Experiment with other clustering techniques, such as hierarchical clustering or DBSCAN.

## Author
Name: Bernard Owusu Sefah
Date: September 18, 2024
