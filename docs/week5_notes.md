**Week 5**

*Notebook: 04_model_comparison.ipynb*

Data Wrangling & Preprocessing

* Imported load\_dataset(), preprocessing(), and train\_test\_split() functions defined in Week 2/Week 3

Evaluation Metrics

* Import evaluation metric functions defined in Week 4  
  * R2, MAE, RMSE, Median Absolute Error, MdAPE

Decision Tree and Random Forest Regressor Models

* Decision Tree performed worse in R2, MAE, and RMSE and slightly better than baseline in median evaluation metrics  
* Random Forest with 20 estimators  
  * Save computing power, perhaps revisit later  
* Random Forest performed better than Decision Tree but still worse than baseline in R2, MAE, RMSE  
  * Performed better than baseline in median metrics (Median Absolute Error, MdAPE)

Linear Regression

* Strengths  
  * Fast, simple  
  * Good baseline  
* Weaknesses  
  * Assumes linear relationships  
  * Sensitive to outliers  
  * Limited in ability to account for feature interactions

Decision Tree

* Strengths  
  * Accounts for nonlinear relationships  
  * Easy to interpret  
* Weaknesses  
  * Overfits data easily  
  * High variance

Random Forest

* Strengths  
  * Accounts for nonlinear relationships  
  * Better at handling outliers than a single decision tree  
* Weaknesses  
  * Slower, requires more computing power

Preliminary Results

|  | R2 | MAE | RMSE | Median Abs Error | MDAPE |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Linear Regression** | 0.4237 | $416155.72 | $1273277.03 | $249575.02 | 25.25% |
| **Decision Tree** | \-20.1151 | $352565.69 | $7707422.85 | $100000.00 | 10.88% |
| **Random Forest** | \-4.6042 | $309642.34 | $3970714.61 | $76575.53 | 8.29% |

