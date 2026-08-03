**Week 7**

Update Preprocessing

* Drop properties not in CA (23 entries)  
* Add UnifiedSchoolDistrict, PropertyAge, BedBathRatio features to preprocessed dataset  
* Train linear regression model with and without additional location features (CountyOrParish, City)  
  * Determine better preprocessed dataset  
  * Baseline model performs better with additional location features  
  * Save new preprocessed dataset

|  | R2 | MAE | RMSE | Median Absolute Error | MDAPE |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Linear Regression (with loc features)** | 0.7855 | $276432.90 | $451337.67 | $179265.56 | 18.54% |
| **Linear Regression (without loc features)** | 0.6833 | $347113.84 | $548477.69 | $227487.18 | 23.43% |

Filter Outliers/Extremes

* Create function to filter 0.5th and 99.5th percentiles

Gradient Boosting Models

* Try gradient boosting models  
* Experiment witty hyperparameters  
* GBMs create decision trees and try to improve on the mistakes made my previous trees  
* XGBoost expands trees symmetrically level by level  
* LightGBM only expands branches (leaves) that reduce error the most

XGBoost Regressor Model

* Train baseline XGBoost model (n\_estimators=100 \+ default parameters)  
* Evaluate baseline model  
  * {'R2': '0.8626', 'MAE': '$201304.65', 'RMSE': '$361265.52', 'MedianAbsoluteError': '$107817.00', 'MDAPE': '11.77%'}  
* Hyperparameter tuning  
  * max\_depth: maximum depth of each tree  
    * \[3, 5, 7\]  
    * \[7, 8, 9, 10\]  
  * learning\_rate: contribution of each new tree to overall model prediction (prevents overfitting)  
    * \[0.05, 0.1, 0.2\]  
    * \[0.2\]  
  * n\_estimators: total number of decision trees used to train model  
    * \[100, 200, 300\]  
    * \[200, 300, 400, 500\]  
  * 362 second runtime

Best performing models:

| depth | learning\_rate | n\_estimators | R2 | MAE | RMSE | Median Absolute Error | MDAPE |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 8 | 0.2 | 500 | 0.8988 | $162300.47 | $310019.39 | $79542.06 | 8.73% |
| 9 | 0.2 | 500 | 0.8983 | $161116.51 | $310791.95 | $77964.00 | 8.47% |
| 7 | 0.2 | 500 | 0.8977 | $165249.45 | $311683.78 | $81778.75 | 9.04% |
| 8 | 0.2 | 400 | 0.8974 | $164437.83 | $312155.06 | $81598.31 | 8.92% |
| 9 | 0.2 | 400 | 0.8973 | $162664.02 | $312306.72 | $79024.75 | 8.69% |

LightGBM Regressor

* Train baseline LightGBM Regressor  
  * {'R2': '0.8603', 'MAE': '$207336.68', 'RMSE': '$364275.77', 'MedianAbsoluteError': '$116149.47', 'MDAPE': '12.44%'}  
* Hyperparameter tuning  
  * max\_depth  
    * \[7, 8, 9, 10\]  
  * learning\_rate  
    * \[0.1, 0.2, 0.3\]  
  * n\_estimators  
    * \[300, 400, 500, 750, 1000\]  
  * 175 second runtime

Best performing models:

| depth | learning\_rate | n\_estimators | R2 | MAE | RMSE | Median Absolute Error | MDAPE |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 9 | 0.2 | 1000 | 0.9047 | $160612.56 | $300871.88 | $79023.08 | 8.76% |
| 7 | 0.2 | 1000 | 0.9047 | $161400.61 | $300811.22 | $80624.27 | 8.85% |
| 8 | 0.2 | 1000 | 0.9042 | $161077.87 | $301624.53 | $79796.83 | 8.82% |
| 9 | 0.2 | 800 | 0.9034 | $162737.36 | $302973.75 | $81096.39 | 8.92% |
| 10 | 0.3 | 1000 | 0.9033 | $162289.30 | $303086.21 | $80435.50 | 8.89% |

