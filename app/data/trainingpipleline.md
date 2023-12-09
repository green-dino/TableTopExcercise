Building a machine learning (ML) training pipeline in Python involves several steps. These steps include data preprocessing, model selection, training, and testing. Here's a step-by-step guide on how to create an ML training pipeline in Python:

1. **Data Preprocessing**: This is the first step in the pipeline. It involves cleaning the data, handling missing values, and transforming the data into a suitable format for the model. This step can be automated using the `ColumnTransformer` from `sklearn.compose` which allows you to specify different transformers for different columns of your data [Source 3](https://towardsdatascience.com/building-a-machine-learning-pipeline-3bba20c2352b).

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

# Define the transformers
num_transformer = StandardScaler()
cat_transformer = OneHotEncoder(sparse=False)

# Define the column transformer
preprocessor = ColumnTransformer(
   transformers=[
       ('num', num_transformer, num_cols),
       ('cat', cat_transformer, cat_cols)
   ])
```

2. **Model Selection**: This step involves choosing a suitable machine learning algorithm for your task. Scikit-learn provides several algorithms, including linear regression and random forest regression. You can experiment with these and other algorithms to see which one performs best on your data [Source 0](https://www.turing.com/kb/building-ml-pipeline-in-python-with-scikit-learn).

```python
model_name = RandomForestRegressor(random_state=42)
```

3. **Pipeline Creation**: The pipeline is created by combining the preprocessing steps and the model. This can be done using the `Pipeline` class from `sklearn.pipeline`. The pipeline is composed of a list of tuples, where each tuple contains the name of the step and the corresponding transformer or model [Source 2](https://itnext.io/best-way-to-make-an-ml-training-pipeline-in-python-691027fa220a).

```python
pipeline = Pipeline(steps=[
   ('preprocessor', preprocessor),
   ('model', model_name)
])
```

4. **Model Training**: The model is trained using the `fit()` method, which uses the training dataset. The model can then be used to make predictions on new data [Source 2](https://itnext.io/best-way-to-make-an-ml-training-pipeline-in-python-691027fa220a).

```python
pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)
```

5. **Model Evaluation**: The performance of the model can be evaluated using various metrics. For regression tasks, the root mean square error (RMSE) is a commonly used metric [Source 0](https://www.turing.com/kb/building-ml-pipeline-in-python-with-scikit-learn).

```python
from sklearn.metrics import mean_squared_error
import math

mse = mean_squared_error(y_test, predictions)
rmse = math.sqrt(mse)
```

6. **Pipeline Optimization**: The pipeline can be optimized by tuning the parameters of the model and the preprocessing steps. This can be done using the `GridSearchCV` class from `sklearn.model_selection`, which performs a grid search over the specified parameter values for an estimator [Source 4](https://machinelearningmastery.com/modeling-pipeline-optimization-with-scikit-learn/).

```python
from sklearn.model_selection import GridSearchCV

parameters = {
   'model__n_estimators': [50, 100, 200],
   'model__max_depth': [None, 10, 20, 30],
   'preprocessor__num__with_mean': [True, False],
   'preprocessor__cat__handle_unknown': ['ignore', 'error']
}

grid = GridSearchCV(pipeline, parameters, cv=5)
grid.fit(X_train, y_train)
```

By following these steps, you can create an efficient and robust ML training pipeline in Python.