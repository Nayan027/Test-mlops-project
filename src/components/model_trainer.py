from src.entity.config_entity import ModelTrainerConfig
import pandas as pd
from sklearn.linear_model import ElasticNet
import joblib


class ModelTrainerClass:
    def __init__(self, config:ModelTrainerConfig):
        self.config = config

# My Code in cleaner manner
    def model_training(self):
        train_data_path=self.config.train_data_path
        test_data_path=self.config.test_data_path
        target_column=self.config.target_column
        alpha=self.config.alpha
        l1_ratio=self.config.l1_ratio
        model_path=self.config.model_path


        train_data = pd.read_csv(train_data_path)
        test_data = pd.read_csv(test_data_path)

        X_train = train_data.drop([target_column], axis=1)
        x_test = test_data.drop([target_column], axis=1)

        Y_train = train_data[[target_column]]
        y_test = test_data[[target_column]]

        model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
        model.fit(X_train, Y_train)

        joblib.dump(value=model, filename=model_path)




# Why double brackets matter here:
# If you wrote:           Y_train = train_data[target_column]
# → you’d get a Series (shape (n,)).

# But with:               Y_train = train_data[[target_column]]
# → you get a DataFrame (shape (n,1)).
# 
# ✅ In ML pipelines, having train_y as a DataFrame (2D) is safer, because libraries 
# like scikit-learn expect X and y to be consistent in dimensionality i.e. X.shape = (n, m) 
# and y.shape = (n, 1) instead of (n,)).
# 
# So the difference:
# [target_column] → Series shape (1D) → shape (3,)
# [[target_column]] → DataFrame shape (2D) → shape (3, 1)

# And ML pipelines prefer DataFrame shape over Series shape cause 
# Consistent 2D shape → ML models expect inputs/outputs to be 2D arrays (X: (n, m), y: (n, 1)). 
# Using a DataFrame (n,1) avoids unexpected shape errors when reshaping or stacking later.


# BAPPY KA CODE.

    # def model_training(self):
    #     train_data = pd.read_csv(self.config.train_data_path)
    #     test_data = pd.read_csv(self.config.test_data_path)

    #     train_X = train_data.drop([self.config.target_column], axis=1)
    #     test_x = test_data.drop([self.config.target_column], axis=1)

    #     train_Y = train_data[[self.config.target_column]]
    #     test_y = test_data[[self.config.target_column]]
        
    #     model = ElasticNet(alpha= self.config.alpha, l1_ratio= self.config.l1_ratio ,fit_intercept= True, random_state=42)
    #     model.fit(train_X, train_Y)

    #     joblib.dump(value=model ,filename=self.config.model_path)