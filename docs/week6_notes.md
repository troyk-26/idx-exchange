**Week 6**

*Notebook: 04_model_comparison_updated.ipynb*

Update/Improve Preprocessing

* Remove impossible values (convert to null)  
  * Latitude and Longitude  
    * Latitude values outside \-90 to 90  
    * Longitude values outside \-180 to 180  
  * LivingArea  
    * Cannot have value of 0  
  * ParkingTotal  
    * Remove values outside 0 to 100  
* GarageSpaces redundant since we have ParkingTotal variable  
  * Create has\_garage variable and drop GarageSpaces  
* Some location variables redundant due to Latitude and Longitude  
  * Remove PostalCode frequency encoding and drop PostalCode  
  * Drop MLSAreaMajor  
* Add option to keep one-hot encoding of other location variables  
  * CountyOrParish  
  * City  
  * HighSchoolDistrict

Filter Outliers

* ClosePrice data heavily right skewed  
* Compute 0.5th and 99.5th percentiles on train dataset  
* Apply these thresholds to test dataset  
* Filter both train and test datasets with these thresholds  
* Still right skewed after filter but not as drastic

Updated Preprocessing Results

* R2 drastically improved, median metrics similar after filtering extremes  
* Encoding additional location features improves prediction accuracy

|  | R2 | MAE | RMSE | Median Abs Error | MDAPE |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Linear Regression** | 0.7710 | $285079.05 | $466404.36 | $183143.09 | 19.08% |
| **Decision Tree** | 0.7700 | $229750.90 | $467413.64 | $100000.00 | 10.71% |
| **Random Forest** | 0.8425 | $210082.44 | $386840.01 | $105350.04 | 11.20% |
| **Linear Regression (No Location Encoding)** | 0.3386 | $515402.76 | $1363385.76 | $323764.86 | 32.02% |
| **Decision Tree (No Location Encoding)** | 0.2873 | $292465.07 | $1415304.35 | $100000.00 | 11.11% |
| **Random Forest (No Location Encoding)** | 0.0135 | $290433.48 | $1665099.19 | $111592.96 | 11.77% |

Feature Importance

* Before additional feature engineering  
  * Decision Tree and Random Forest models have identical top 10 for feature importance  
  * Top 4:  
    * BathroomsTotalInteger, LivingArea, Longitude, Latitude

Feature Engineering: School Districts

* Download California School Districts GeoJSON  
* Assign property to school district based on Latitude and Longitude features  
* One-hot encode UnifiedSchoolDistricts column  
* Slight improvement in evaluation metrics for each model (Linear Regression, Decision Tree, Random Forest)

|  | R2 | MAE | RMSE | Median Abs Error | MDAPE |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Linear Regression** | 0.7850 | $277208.23 | $451899.29 | $179863.95 | 18.53% |
| **Decision Tree** | 0.7812 | $225425.69 | $455836.21 | $100000.00 | 10.67% |
| **Random Forest** | 0.8432 | $210935.00 | $385900.91 | $106070.34 | 11.21% |

Feature Engineering: Property Age & Bed/Bath Ratio

* Subtract year built from close date for property age  
* Divide BedroomsTotal by BathroomsTotalInteger  
  * Handle divide by zero values
