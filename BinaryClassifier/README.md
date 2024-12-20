# Machine Learning and Clustering

## Overview

This project explores two essential machine learning techniques: K-Nearest Neighbors (KNN) for classification and K-Means Clustering for unsupervised learning. It includes analyses on binary and trinary classification datasets and clustering datasets to identify patterns and optimal clustering solutions.

The primary objectives are:

To implement KNN and evaluate its accuracy across various datasets.
To use K-Means Clustering and determine the optimal number of clusters using the "elbow method."

## Technologies and Libraries
Programming Language: R
Libraries:
ggplot2: For creating scatter plots and visualizations.
class: For efficient KNN implementation.
tidyr: For data reshaping.

## Structure
Classification with KNN
Datasets:
Binary Classifier Dataset:
Consists of two classes (labels 0 and 1).
Scatter plot visualizes the decision boundary challenges.
Trinary Classifier Dataset:
Consists of three classes (labels 0, 1, and 2).

## Methodology:
KNN Implementation:
Function fit_knn() calculates accuracy using the KNN algorithm.
Tested with multiple values of k (3, 5, 10, 15, 20, 25).
Accuracy Evaluation:
Plotted accuracy vs. k to observe trends for both datasets.

## Key Insights:
The KNN classifier outperformed logistic regression due to its ability to model non-linear relationships.
Optimal performance for binary classification achieved with k=25 (accuracy: 74.1%).
For trinary classification, the highest accuracy was 63.2% at k=25.
Exercise 2: Clustering with K-Means
Dataset:
Clustering Dataset:
Contains 2D points used to form clusters.
Methodology:
K-Means Implementation:
Applied K-Means clustering for k=2 to k=12.
Plotted clusters and calculated average distances from data points to their respective cluster centers.
Elbow Method:
Plotted average distance vs. k to identify the optimal number of clusters (elbow point).
Key Insights:
The elbow point was observed at k=4 to k=6, indicating the optimal number of clusters.

## How to Run
Prerequisites:
Install R and RStudio.
Install required libraries:
R
install.packages(c("ggplot2", "class", "tidyr"))

## Datasets:
Ensure the following datasets are in your working directory:
binary-classifier-data.csv
trinary-classifier-data.csv
clustering-data.csv
Steps:
Run the R script or notebook sequentially to:
Visualize the data.
Train KNN models and evaluate accuracy.
Perform K-Means clustering and determine the elbow point.

## Outputs
Scatter Plots:
Visual representation of binary and trinary classification datasets.
Clustered data points with cluster centers.
Accuracy Plot:
KNN accuracy vs. k for binary and trinary classification datasets.
Elbow Plot:
Average distance vs. k for K-Means clustering to identify the optimal number of clusters.

## Lessons Learned
Model Selection:
KNN is effective for datasets with non-linear decision boundaries, while logistic regression struggles with such patterns.
Clustering:
The elbow method provides a practical approach to selecting the optimal number of clusters.
Trade-offs:
Smaller k values in KNN risk overfitting, while larger k values smooth out noise at the cost of missing local patterns.

## Author
Name: Bernard Owusu Sefah
Date: 2024-05-26
