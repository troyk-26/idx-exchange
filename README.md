# IDX-Exchange
IDX Exchange Data Science Internship 2026
California Property Close Price Prediction Model

## Project Overview

This repository contains work completed during the internship involving analysis of CRMLS data. The objective is to explore the dataset and prepare it for machine learning models that predict residential property sale prices.

## Repository Structure

```
.
├── docs/
│   └── week1_notes.md
│   └── week2_notes.md
│   └── week3_notes.md
│   └── week4_notes.md
│   └── week5_notes.md
├── notebooks/
|   └── 01_exploration.ipynb
|   └── 02_preprocessing.ipynb
|   └── 03_baseline_model.ipynb
|   └── 04_model_comparison.ipynb
|   └── 04_model_comparison_updated.ipynb
├── .gitignore
└── README.md
```


## Dataset

The analysis is performed using 31 months of CRMLS sold property data from 30 datasets. The most recent month is used as the test dataset and the 30 months immediately preceding contain the training data for the predictive models. The notebooks assume the dataset has already been downloaded and is available locally.

## Week 1

- Established access to the project dataset
- Reviewed the CRMLS metadata documentation
- Documented the purpose of key dataset columns

## Week 2

- Loaded twelve months of CRMLS data into pandas
- Filtered records to:
  - PropertyType = Residential
  - PropertySubType = SingleFamilyResidence
- Performed exploratory data analysis (EDA) on:
  - ClosePrice
  - LivingArea
  - BedroomsTotal
  - BathroomsTotalInteger
  - LotSizeArea

## Week 3
 
- Defined preprocessing function
  - Handled missing values (dropped columns or filled missing values)
  - Encoded categorical variables (multi-label/one-hot/frequency)
- Defined train-test split function
  - Most recent month is test dataset
  - Adjustable parameter specifying number of months immediately preceding most recent month to use for training dataset

## Week 4

- Loaded dataset, preprocessing, and train-test split functions
- Trained linear regression models
  - Experimented with varying numbers of months for train dataset
- Used five metrics to evaluate linear regression models
  - R<sup>2</sup>, MAE, RMSE, Median Absolute Error, MdAPE
 
## Week 5

- Trained decision tree and random forest models
- Compared tree model performance to baseline linear regression performance

## Software

- Python
- pandas
- matplotlib
- Seaborn
- Scikit-learn
- Jupyter Lab/Jupyter Notebook

## Running the Project

1. Download the required CRMLS dataset (not included in this repository)
2. Update the file path in notebooks if necessary
3. Run the notebooks to reproduce the exploratory data analysis, preprocessing, data wrangling, and model creation.
