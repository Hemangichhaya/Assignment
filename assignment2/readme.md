Install
  - pandas
  - scikit-learn
  - matplotlib
  - seaborn

Ploted usage_kwh vs Load_type boxplot to analyzed the outlier. Light_load having a highest overlap as compaer to other Load-type data.

Data consist of imbalance across classes SMOTE function is used to do oversampling.

Calculate the power fector, kVAh, kw and KVA as new feature in feature engineering.

Measure the performance of the model using Logostic Regression, Random Foreset Classifier, Decision Tree and XGBoost.

XGBoost is having the best performance.

|               | precision | Recall  | f1-score | support |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 0             | 0.99  |  0.97  | 0.98  | 3576  |
| 1             | 0.91  |  0.95  | 0.93  | 1500  |
| 2             | 0.92  |  0.93  | 0.93  | 1932  |
| accuracy      |       |        | 0.95  | 7008 |
| macro avg     | 0.94  |  0.95  | 0.95  | 7008  |  
| weighted avg  | 0.96  |  0.95  | 0.95  | 7008  |
          
