# Predicting Customer Churn in the Telecom Industry

## Overview

This project focuses on predicting customer churn in the telecom industry using machine learning models. Churn prediction is crucial for retaining customers, reducing revenue loss, and designing effective retention strategies. By analyzing the "Telecom Churn Dataset," this project identifies patterns and insights that influence customer behavior and churn rates.

## Features

Exploratory Data Analysis (EDA): Understanding the relationships between features like monthly charges, data usage, and churn status.

Feature Engineering: Development of features such as "DataOverageRatio" to capture the impact of additional charges.

Machine Learning Models: Implementation of Logistic Regression, Random Forest, and Gradient Boosting Machines (GBM) to predict churn.

Visualization: Interactive visualizations, including scatter plots, histograms, and correlation heatmaps, to present insights.

## Tools and Technologies

Python: Core programming language.

Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn.

Jupyter Notebook: Interactive development environment for coding and analysis.

Data Description

Source: Kaggle Telecom Churn Dataset.

## Key Features:

Churn: Indicates whether a customer churned (1) or not (0).

MonthlyCharge: The monthly billing amount.

CustServCalls: Number of customer service calls made.

DataUsage: Amount of data consumed.

ContractRenewal: Whether the customer renewed their contract.

## Methodology

Data Preprocessing:

Handled outliers in features such as MonthlyCharge and OverageFee using the interquartile range (IQR) method.

Encoded categorical variables like ContractRenewal and DataPlan into binary columns.

Scaled numerical features using StandardScaler to ensure uniformity.

Model Training:

Logistic Regression: A baseline model for interpretability.

Random Forest: Captured feature importance and non-linear relationships.

Gradient Boosting Machines (GBM): Achieved the best balance between accuracy and recall.

Evaluation Metrics:

Precision, Recall, and F1-Score.

ROC-AUC Score for model comparison.

## Results

Best Performing Model: Gradient Boosting Machines.

F1-Score: 0.76 for churners.

ROC-AUC: 0.91.

Key Features Influencing Churn:

High MonthlyCharge and CustServCalls increase churn likelihood.

Recent ContractRenewal significantly reduces churn risk.

## Visualizations

Scatter Plot: Monthly Charge vs Data Usage, with churn status as the hue.

Correlation Matrix: Highlights relationships between key features.

Feature Importance: Bar charts for Random Forest and GBM models.

Confusion Matrices: Performance summaries for all models.

## How to Run

Clone the repository.

git clone [https://github.com/bowusus/Telecom-Churn-Prediction.git](https://github.com/bowusus/Bellevue-Portfolio-/tree/main/Predicting%20Churn)

Navigate to the project directory.

cd Telecom-Churn-Prediction

Install required dependencies.

pip install -r requirements.txt

Open and run the Jupyter Notebook.

jupyter notebook churn_analysis.ipynb

## Insights and Recommendations

Enhance Customer Service: Frequent customer service calls correlate with churn. Improve service quality to reduce unresolved issues.

Address Billing Concerns: High MonthlyCharge and OverageFee drive churn. Offer competitive pricing and educate customers about reducing overage fees.

Proactively Engage High-Risk Customers: Use predictive analytics to identify churn-prone customers and target them with personalized retention offers.

Promote Contract Renewals: Customers who renew contracts are less likely to churn. Provide incentives for early renewals.

## Ethical Considerations

Bias Mitigation: Ensured fairness in model predictions by auditing outputs.

Data Privacy: Adhered to strict anonymization practices and ensured compliance with data protection regulations.

Transparency: Communicated findings clearly to stakeholders without obscuring technical details.

## Author

Bernard Owusu Sefah [GitHub](https://github.com/bowusus) | [LinkedIn](https://www.linkedin.com/in/bernard-owusu-sefah-137188171/)
