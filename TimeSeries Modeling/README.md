# Time Series Modeling of US Retail Sales
## Overview
This project focuses on analyzing and predicting US Monthly Retail Sales using a time series dataset spanning from January 1992 to June 2020. The analysis implements an ARIMA model to identify trends, detect seasonality, and forecast sales. The project evaluates the performance of the ARIMA model by comparing predictions with actual sales data from July 2020 to June 2021.

## Key Features
Data Preparation:

Reshaped the data for continuous time series analysis.
Addressed missing values and ensured data consistency.
Exploratory Data Analysis:

Visualized sales trends and seasonal patterns.
Identified key events such as economic downturns and seasonal spikes.
Time Series Modeling:

Built and trained an ARIMA(5, 1, 0) model.
Evaluated model performance using RMSE and diagnostic tests.
Predictions and Visualization:

Forecasted sales for a 12-month test period.
Compared predicted values with actual sales to assess model accuracy.

## Technologies and Libraries
Programming Language: Python
Libraries:
pandas: Data manipulation and cleaning.
numpy: Numerical computations.
matplotlib: Data visualization.
statsmodels: Time series modeling (ARIMA).
scikit-learn: Performance evaluation (RMSE).

## How to Run
Prerequisites
Install Python 3.x.
Install the required libraries: 
pip install pandas numpy matplotlib statsmodels scikit-learn
Steps
Dataset:
Ensure the dataset file (us_retail_sales.csv) is available in the working directory.
Run the Script:
Execute the Python script or Jupyter Notebook to perform the following steps:
Load and clean the data.
Visualize sales trends.
Train the ARIMA model.
Forecast sales and evaluate performance.
Outputs:
Visualizations of sales trends and seasonality.
Predicted vs. actual sales comparison.
RMSE score to quantify model accuracy.

## Key Steps in the Analysis
1. Data Preparation
Reshaped the data to form a continuous time series.
Addressed missing values for the months July–December 2021 by excluding these rows.
2. Data Visualization
Trends:
Overall upward trend in retail sales.
Seasonality:
Recurring peaks around the holiday season.
Anomalies:
Sharp drops during economic crises, such as the 2008 financial crisis and the COVID-19 pandemic (2020).
3. Model Training
Built an ARIMA(5, 1, 0) model:
p=5: 5 lagged observations for autoregressive terms.
d=1: Data differenced once for stationarity.
q=0: No moving average terms.
Evaluated the model using AIC and BIC.
4. Predictions
Forecasted sales for the test period (July 2020 to June 2021).
Created a comparison table for actual vs. predicted sales.
5. Model Evaluation
RMSE: 57,006. Indicates the average deviation between actual and predicted sales.
Visualized actual vs. predicted sales using a line chart.

## Key Findings
Overall Performance:
The ARIMA model captured general trends but struggled with sudden fluctuations.
Seasonal Patterns:
The model identified holiday season spikes but underpredicted some peaks.
Areas for Improvement:
Incorporate additional exogenous variables (e.g., economic indicators) for better accuracy.

## Lessons Learned
What Worked Well:
The ARIMA model effectively identified long-term trends and seasonality.
Visualizations provided clear insights into sales patterns.
What Could Be Improved:
Experiment with other time series models (e.g., SARIMA, Prophet).
Use external variables like unemployment rates or consumer spending indices.
Outputs
Visualizations:
Monthly retail sales trends from 1992 to 2020.
Actual vs. predicted sales for the test period.
Metrics:
RMSE: 57,006.

## Author
Name: Bernard Owusu Sefah
Date: October 17, 2024
