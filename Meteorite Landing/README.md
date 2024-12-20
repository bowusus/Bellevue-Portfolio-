# Project Title: Meteorite Landings Data Cleaning and Scraping
## Author: Bernard Owusu Sefah
## Overview:
This project focuses on cleaning meteorite landings datasets, handling missing values, and removing inconsistencies. It further involves web scraping of population data to provide accurate and usable insights for analysis.

## Key Components:
Data Cleaning:

Standardized column headers (lowercase, underscores).
Handled missing values in critical columns (mass_(g), year, reclat, reclong).
Converted data types for consistency (year as integer, mass_(g) as float).
Removed duplicates.
Outliers in mass_(g) were capped at the 99th percentile for better data integrity.
Web Scraping:

Extracted population data from worldpopulationreview.com.
Parsed HTML tables using BeautifulSoup.
Cleaned and formatted rows for columns like city names, population statistics, and growth rates.
Ethical Implications:

Ethical handling of data transformations to avoid misrepresentation.
Transparent documentation of methods.
Preserved original data for validation.

## Files and Outputs:
Input: Meteorite_Landings_20240614.csv
Output: Cleaned_Meteorite_Landings.csv
Scraped Population Data: Stored in a DataFrame.
