import os
import joblib
from car import logger
from car.entity.config_entity import ModelTrainConfig
import pandas as pd


class ModelTrainer:
    def __init__(self, config = ModelTrainConfig):
        self.config = config
        self.params = config.params
        self.schema = config.schema


    def train(self):
        train_path = self.config.train_path
        test_path = self.config.test_path
        target_col = self.schema.target_column

        output_path = self.config.model_path
        transformer_path = self.config.transformer_path

        df_train = pd.read_csv(train_path)
        df_test = pd.read_csv(test_path)

        X_train = df_train.drop(target_col, axis=1)
        X_test = df_test.
