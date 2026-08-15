**Week 8**

*Notebook: 06\_evaluation.ipynb*

Preprocessed Data

* Load ‘preprocssed\_data.csv’ from last week  
* Includes encoded additional location features (CountyOrParish, City)

Additional Evaluation Metrics

* Add mean absolute percentage error (MAPE) from Scikit-Learn

Summarize Results

* Evaluate all models and summarize metrics in table  
* Plot predicted vs. actual closing price for XGBoost and LightGBM

|  | R2 | MAE | RMSE | Median Absolute Error | MAPE | MDAPE |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **Linear Regression** | 0.7855 | $276432.90 | $451337.67 | $179265.56 | 25.82% | 18.54% |
| **Decision Tree** | 0.7836 | $226204.29 | $453373.17 | $100000.00 | 16.58% | 10.75% |
| **Random Forest** | 0.8384 | $215286.69 | $391737.28 | $108563.37 | 17.03% | 11.38% |
| **XGBoost** | 0.8983 | $161116.51 | $310791.95 | $77964.00 | 12.27% | 8.47% |
| **LightGBM** | 0.9047 | $160612.56 | $300871.88 | $79023.08 | 12.31% | 8.76% |

Analyze Price Bands

* Divide data into price bands based on ClosePrice  
* Evaluate model performances for each price band

Linear Regression

|  | R2 | MAE | RMSE | Median Absolute Error | MAPE | MDAPE | N |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **\<$500K** | \-8.1815 | $174315.44 | $226390.11 | $143560.12 | 46.43% | 37.70% | 1635 |
| **500K–1M** | \-2.6322 | $196955.27 | $264880.79 | $152540.44 | 27.29% | 20.48% | 4897 |
| **1M–2M** | \-0.4782 | $240226.62 | $328916.87 | $183727.17 | 17.29% | 13.36% | 3750 |
| **$2M+** | 0.2905 | $706474.87 | $993823.51 | $503552.51 | 20.24% | 17.39% | 1609 |

Decision Tree

|  | R2 | MAE | RMSE | Median Absolute Error | MAPE | MDAPE | N |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **\<$500K** | \-3.3249 | $70967.01 | $155377.94 | $40000.00 | 18.86% | 10.34% | 1635 |
| **500K–1M** | \-0.9597 | $101148.66 | $194563.35 | $63000.00 | 13.46% | 8.57% | 4897 |
| **1M–2M** | \-1.1036 | $249413.68 | $392383.85 | $169000.00 | 17.44% | 12.46% | 3750 |
| **$2M+** | 0.2669 | $710464.78 | $1010185.82 | $500000.00 | 21.74% | 16.85% | 1609 |

Random Forest

|  | R2 | MAE | RMSE | Median Absolute Error | MAPE | MDAPE | N |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **\<$500K** | \-3.0884 | $87531.31 | $151070.61 | $46761.87 | 24.04% | 12.24% | 1635 |
| **500K–1M** | \-0.5140 | $110782.02 | $171013.73 | $68840.68 | 14.97% | 9.51% | 4897 |
| **1M–2M** | \-0.2595 | $221416.17 | $303610.91 | $167762.96 | 15.58% | 12.29% | 3750 |
| **$2M+** | 0.4203 | $648881.42 | $898367.45 | $480144.74 | 19.58% | 16.32% | 1609 |

XGBoost

|  | R2 | MAE | RMSE | Median Absolute Error | MAPE | MDAPE | N |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **\<$500K** | \-1.3233 | $60579.73 | $113880.86 | $36704.19 | 16.54% | 9.27% | 1635 |
| **500K–1M** | 0.3044 | $76449.76 | $115914.41 | $52142.19 | 10.28% | 7.10% | 4897 |
| **1M–2M** | 0.1998 | $167879.76 | $242001.69 | $122321.12 | 11.82% | 8.96% | 3750 |
| **$2M+** | 0.6241 | $505198.88 | $723378.64 | $358442.00 | 15.04% | 12.28% | 1609 |

LightGBM

|  | R2 | MAE | RMSE | Median Absolute Error | MAPE | MDAPE | N |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **\<$500K** | \-0.6813 | $59756.78 | $96876.69 | $38622.81 | 16.36% | 9.66% | 1635 |
| **500K–1M** | 0.3131 | $77496.52 | $115192.37 | $54179.83 | 10.41% | 7.37% | 4897 |
| **1M–2M** | 0.2058 | $170061.15 | $241095.44 | $128008.21 | 11.94% | 9.36% | 3750 |
| **$2M+** | 0.6526 | $494040.95 | $695416.48 | $351371.91 | 14.85% | 12.34% | 1609 |

Price Band Analysis Results

* $2M+ price band consistently performs best across all models  
* \<$500K consistently performs worst across all models  
* Gradient boosted models (XGBoost, LightGBM) perform well across all price bands

MdAPE Price Band Analysis

|  | Linear Regression | Decision Tree | Random Forest | XGBoost | LightGBM |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **\<$500K** | 37.70% | 10.34% | 12.24% | 9.27% | 9.66% |
| **500K–1M** | 20.48% | 8.57% | 9.51% | 7.10% | 7.37% |
| **1M–2M** | 13.36% | 12.46% | 12.29% | 8.96% | 9.36% |
| **$2M+** | 17.39% | 16.85% | 16.32% | 12.28% | 12.34% |

