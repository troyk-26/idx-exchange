**Week 4**

Data Wrangling & Preprocessing

* Imported load\_dataset(), preprocessing(), and train\_test\_split() functions defined in Week 2/Week 3

Linear Regression Model

* Defined Median Absolute Percentage Error (MdAPE)  
* Evaluate model on R2 score, mean absolute error (MAE), mean squared error (RMSE), median absolute error, median absolute percentage error (MdAPE)  
* No cross validation (mixes data from different months)  
* Evaluated on different number of months for train dataset  
  * train\_months \= \[6, 12, 15, 18, 20, 25, 30, 35, 40\]  
* 35-month training dataset had best evaluation metrics but 25 and 30 months both scored reasonably well with less training information