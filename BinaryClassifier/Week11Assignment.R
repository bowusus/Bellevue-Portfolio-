# Load required libraries
library(ggplot2)
library(class)  # For efficient KNN implementation
library(tidyr)   # For data reshaping

# Exercise 1: Introduction to Machine Learning

# Read in binary and trinary classifier datasets
binary_data <- read.csv("binary-classifier-data.csv")
trinary_data <- read.csv("trinary-classifier-data.csv")

# Create scatter plots colored by label
# Binary data
ggplot(binary_data, aes(x=x, y=y, color=as.factor(label))) + 
  geom_point() + 
  ggtitle("Binary Classifier Data")

# Trinary data  
ggplot(trinary_data, aes(x=x, y=y, color=as.factor(label))) + 
  geom_point() + 
  ggtitle("Trinary Classifier Data")

# Function to fit KNN model and calculate accuracy
fit_knn <- function(data, k) {
  
  # Split data into features (x) and labels (y)
  x <- data[,2:3]
  y <- data[,1]
  
  # Fit KNN model using 'knn' function from 'class' package
  predictions <- knn(train = x, test = x, cl = y, k = k)
  
  # Calculate accuracy
  accuracy <- mean(predictions == y)
  
  return(accuracy)
}

# Fit KNN models and store accuracies for various k values
k_values <- c(3, 5, 10, 15, 20, 25)
binary_accuracies <- sapply(k_values, function(k) fit_knn(binary_data, k))
trinary_accuracies <- sapply(k_values, function(k) fit_knn(trinary_data, k))

# Create data frame for plotting
accuracy_data <- data.frame(
  k = rep(k_values, 2),
  accuracy = c(binary_accuracies, trinary_accuracies),
  data_type = rep(c("Binary", "Trinary"), each = length(k_values))
)

# Plot accuracy vs k using ggplot
accuracy_plot <- ggplot(accuracy_data, aes(x = k, y = accuracy, color = data_type, group = data_type)) +
  geom_line() +
  geom_point() +
  scale_x_continuous(breaks = k_values) +
  ylim(0, 1) +
  labs(x = "k", y = "Accuracy", color = "Data Type") +
  ggtitle("KNN Accuracy vs k") +
  theme_minimal()

print(accuracy_plot)

# Exercise 2: Clustering

# Read in clustering dataset 
cluster_data <- read.csv("clustering-data.csv")

# Scatter plot of data
ggplot(cluster_data, aes(x=x, y=y)) + 
  geom_point() + 
  ggtitle("Clustering Data")

# Function to plot clusters
plot_clusters <- function(data, centers, assignments) {
  
  # Create a data frame with cluster assignments
  data_with_clusters <- data.frame(x = data[,1], y = data[,2], cluster = as.factor(assignments))
  
  # Create a data frame with cluster centers
  centers_df <- data.frame(x = centers[,1], y = centers[,2], cluster = as.factor(1:nrow(centers)))
  
  # Create scatter plot colored by cluster
  ggplot(data_with_clusters, aes(x = x, y = y, color = cluster)) + 
    geom_point() +
    geom_point(data = centers_df, size = 5, shape = "x") +
    ggtitle(paste("K-Means Clusters (k=", nrow(centers), ")", sep=""))
}

# Fit k-means models and plot clusters
for (k in 2:12) {
  
  # Fit k-means model
  km <- kmeans(cluster_data[,1:2], centers=k)
  
  # Plot clusters
  print(plot_clusters(cluster_data, km$centers, km$cluster))
  
  # Calculate average distance to cluster centers
  avg_dist <- mean(sapply(1:nrow(cluster_data), function(i) 
    sqrt(sum((cluster_data[i,1:2] - km$centers[km$cluster[i],])^2))))
  
  cat("k=", k, "  Average Distance=", avg_dist, "\n")
}

# Function to fit k-means model and calculate average distance to cluster centers
fit_kmeans <- function(data, k) {
  
  # Fit k-means model
  km <- kmeans(data[,1:2], centers = k)
  
  # Calculate average distance to cluster centers
  avg_dist <- mean(sapply(1:nrow(data), function(i) 
    sqrt(sum((data[i,1:2] - km$centers[km$cluster[i],])^2))))
  
  return(avg_dist)
}

# Fit k-means models and calculate average distances for k=2 to 12
k_values <- 2:12
avg_dists <- sapply(k_values, function(k) fit_kmeans(cluster_data, k))

# Create data frame for plotting
elbow_data <- data.frame(k = k_values, avg_dist = avg_dists)

# Plot average distance vs k using ggplot
elbow_plot <- ggplot(elbow_data, aes(x = k, y = avg_dist)) +
  geom_line() +
  geom_point() +
  scale_x_continuous(breaks = k_values) +
  labs(x = "Number of Clusters (k)", y = "Average Distance to Center") +
  ggtitle("Average Distance vs Number of Clusters (k)") +
  theme_minimal()

print(elbow_plot)

