import os
import joblib
from car import logger
from car.entity.config_entity import ModelTrainConfig
import pandas as pd
from sklearn.ensemble import RandomForestRegressor


class ModelTrainer:
    def __init__(self, config = ModelTrainConfig):
        self.config = config
        self.params = config.params
        self.schema = config.schema


    def train(self):
        train_path = self.config.train_path
        test_path = self.config.test_path
        target_col = list(self.schema.target_column.keys())[0]

        output_path = self.config.model_path
        transformer_path = self.config.transformer_path

        df_train = pd.read_csv(train_path)
        df_test = pd.read_csv(test_path)

        X_train = df_train.drop(target_col, axis=1)
        X_test = df_test.drop(target_col, axis=1)

        y_train = df_train[[target_col]]
        y_test = df_test[[target_col]]

        transformer = joblib.load(transformer_path)
        X_train = transformer.transform(X_train)
        print(X_train)

        max_features = self.params.rf.max_features
        n_estimators = self.params.rf.n_estimators

        model = RandomForestRegressor(max_features=max_features, n_estimators=n_estimators, n_jobs=-1)
        model.fit(X_train, y_train)
        joblib.dump(model, output_path)
