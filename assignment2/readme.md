Install
  - pandas
  - scikit-learn
  - matplotlib
  - seaborn

Ploted usage_kwh vs Load_type boxplot to analyzed the outlier. Light_load having a highest overlap as compaer to other Load-type data.

Calculate the power fector and KVA as new feature in feature engineering.

Measure the performance of the model using Logostic Regression, Random Foreset Classifier, Decision Tree and XGBoost.

XGBoost is having the best performance.

After doing feature engineering performance input:

|               | precision | Recall  | f1-score | support |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 0             | 0.97  |  0.95  | 0.96  | 3574  |
| 1             | 0.76  |  0.80  | 0.78  | 1499  |
| 2             | 0.78  |  0.77  | 0.77  | 1936  |
| accuracy      |       |        |  0.87  | 7009 |
| macro avg     | 0.83  |  0.84  | 0.84  | 7009  |  
| weighted avg  | 0.87  |  0.87  | 0.87  | 7009  |
          
