**Week 3**

*Notebook: 02_preprocessing.ipynb*

Dataset

* Loaded all 30 datasets  
* Filtered to Residential and SingleFamilyResidence Property Types  
* Converted CloseDate to DateTime dtype

Handle Missing Values

* Drop columns not known at prediction time  
* Drop columns with null rate above 50%  
* Drop columns with no plausible relationship to ClosePrice  
  * Drop columns related to buyer or listing agent  
* Fill columns with less than 50% null rate with median or sentinel  
  * Create binary has\_hoa feature based on AssociationFee (0 if 0 or null, 1 else)  
  * Null values for ViewYN, PoolPrivateYN, FireplaceYN, AttachedGarageYN, NewConstructionYN can be reasonably assumed to be No/False  
  * Null values for certain categorical variables replaced with ‘Unknown’  
* Consider dropping columns with correlation to ClosePrice \> \-0.05  
  * PropertyType and PropertySubType have zero variance (dataset filtered)  
  * StateOrProvince has very little variance (almost all in CA)  
    * Replace StateOrProvince with binary InCalifornia variable  
* Drop rows with missing values for target variable (ClosePrice) and other important features with very little missing values  
  * LivingArea & PostalCode important for model, missing values cannot be estimated

Encoding Categorical Variables

* Flooring  
  * Multi-label encoding  
  * Remove ‘SeeRemarks’  
* MLSAreaMajor  
  * Frequency encoding  
  * Replace column with MLSAreaMajor\_freq column  
* CountyOrParish  
  * One-hot encoding  
  * Standardize capitalization  
  * Group non-counties in ‘Other’  
* Levels  
  * Multi-label encoding  
* City  
  * Group cities with less than 500 entries  
  * One-hot encoding  
* HighSchoolDistrict  
  * Group districts with less than 100 entries  
  * One-hot encoding  
* PostalCode  
  * Frequency encode PostalCode (3673 unique values)  
  * Sufficient for baseline model since MLSAreaMajor\_freq, CountyOrParish dummies, and City dummies describe location too

Train Test Split

* Use most recent month as test dataset  
* X months prior used as test dataset  
* Experiment with different values of X  
  * Adjust when testing models
