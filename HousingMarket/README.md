# Housing Market Analysis and Prediction
## Overview
This project analyzes housing market trends, income data, and economic indicators to predict Median Sale Prices of homes in the United States. It leverages exploratory data analysis (EDA), machine learning, and clustering techniques to extract insights and build a predictive model.

The project includes:

Data Cleaning and Integration: Combines housing, income, and economic datasets into a single unified dataset.
Exploratory Data Analysis: Visualizes trends and relationships between variables.
Linear Regression Modeling: Builds and evaluates a predictive model for housing prices.
Clustering Analysis: Segments data into clusters based on income and housing price relationships.

## Data Sources
The following datasets are used:

HousingData2.csv: Contains housing price trends and inventory.
kaggle_income2.csv: Provides median and mean income data by city.
UNRATE.csv: U.S. unemployment rate data.
demand.csv: Includes economic indicators like mortgage rates, GDP, and housing demand.
City_time_series1.csv: Time series data of city-level housing metrics.
ASPUS.csv: Average sale price in the United States.

## Technologies Used
R: Programming language for data analysis and modeling.
Libraries:
dplyr, tidyr: Data manipulation and cleaning.
ggplot2: Visualization.
corrplot: Correlation heatmap.
caret: Machine learning tools.
lubridate: Date formatting and handling.
cluster: Clustering analysis.
Project Workflow

## 1. Data Preparation
Each dataset is cleaned and padded to ensure equal lengths for merging.
Key transformations include:
Conversion of income and price data to numeric formats.
Splitting of RegionName into city and state components.
Time-based formatting of city time series data.

## 2. Combining Data
The datasets are combined into a single dataframe using bind_cols.
The combined dataset includes:
Housing metrics (e.g., Median Sale Price, Homes Sold, Inventory).
Economic indicators (e.g., mortgage rates, GDP, unemployment rate).
Income data (Median and Mean Income).

## 3. Exploratory Data Analysis (EDA)
Correlation Heatmap: Visualizes relationships between variables.
Scatter Plots: Display relationships between income and housing prices.
Bar Plots: Compare regional differences in housing metrics and income.
Time Series Plots: Analyze trends over time for key metrics:
Median Sale Price
Median Income
Homes Sold

## 4. Predictive Modeling
Linear Regression
A linear regression model predicts Median Sale Price using:
Median Income
Mean Income
Unemployment Rate (UNRATE)
Consumer Price Index (CSUSHPISA)
Mortgage Rates
GDP
Other housing-related metrics.
Model Evaluation:

R-Squared: 0.9818 (explains 98.18% of the variance in housing prices).
Root Mean Squared Error (RMSE): 9.5 units, indicating reasonably accurate predictions.
Key Predictors:

CSUSHPISA: Consumer Price Index for urban consumers.
MSPUS: Monthly supply of houses in the U.S.
GDP: Gross Domestic Product.

## 5. Clustering Analysis
K-Means Clustering: Groups data into 3 clusters based on income and housing metrics.
Visualization: A scatter plot displays clusters of Median Sale Price based on Median Income.
This segmentation helps identify trends and relationships across different regions.

## Results and Insights
Key Predictors of Housing Prices:
Economic factors like CPI (CSUSHPISA), housing supply (MSPUS), and GDP significantly influence housing prices.
Model Performance:
The linear regression model explains most of the variation in housing prices, with an RMSE of 9.5, showing reasonably accurate predictions.
Trends Over Time:
Median Sale Prices, income levels, and homes sold exhibit noticeable trends over time.
Clustering Insights:
Clustering highlights distinct patterns in housing prices relative to income, providing actionable insights for regional segmentation.

## Visualizations
The following visualizations are generated:

Correlation Heatmap: Displays relationships between variables.
Scatter Plots:
Median Income vs Median Sale Price.
Mean Income vs Median Sale Price.
Bar Plots:
Median Sale Price, Median Income, and Homes Sold by Region.
Time Series Plots:
Median Sale Price, Median Income, and Homes Sold over time.
Clustering Visualization:
Segments data into clusters to identify income-price relationships.

## How to Run the Project
Install the required libraries in R:
install.packages(c("readr", "dplyr", "tidyr", "ggplot2", "corrplot", "caret", "cluster", "lubridate"))
Place the datasets in the working directory.
Run the R script step-by-step in RStudio or an R environment.
View the outputs, including visualizations, model summaries, and evaluation metrics.

