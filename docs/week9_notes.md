**Week 9**

*Notebook: 07\_app.ipynb*

Test Joblib/Streamlit

* Use best performing model  
  * LightGBM regressor  
    * max\_depth=9, learning\_rate=0.2, n\_estimators=1000  
  * Retrain model with simplified dataset  
    * 'LivingArea'  
    * 'BedroomsTotal'  
    * 'BathroomsTotalInteger'  
    * 'LotSizeSquareFeet'

Streamlit App

* Create [app.py](http://app.py) file  
* Import simple LightGBM model  
* Run streamlit app from terminal