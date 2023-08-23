import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from car.entity.config_entity import ModelEvaluationConfig
from car.utils.common import save_json
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        print(self.config)

    
    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    


    def log_into_mlflow(self):
        os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/shadow-1310/commodity-price-prediction.mlflow"
        os.environ["MLFLOW_TRACKING_USERNAME"] = "shadow-1310"
        os.environ["MLFLOW_TRACKING_PASSWORD"] = "b09e191de8ca102ecebcf4277b93dea9ff0e7be3"
        params = self.config.params.model_training.rf
        test_data = pd.read_csv(self.config.test_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_col], axis=1)
        transformer = joblib.load(self.config.transformer_path)
        test_x = transformer.transform(test_x)
        test_y = test_data[[self.config.target_col]]


        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        print(tracking_url_type_store)

        with mlflow.start_run():

            predicted_qualities = model.predict(test_x)

            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
            
            # Saving metrics as local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file), data=scores)

            mlflow.log_params(params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)

            mlflow.sklearn.log_model(model, "car",registered_model_name="RandomForestRegressor")

            # Model registry does not work with file store
            # if tracking_url_type_store != "file":

            #     # Register the model
            #     # There are other ways to use the Model Registry, which depends on the use case,
            #     # please refer to the doc for more information:
            #     # https://mlflow.org/docs/latest/model-registry.html#api-workflow
            #     mlflow.sklearn.log_model(model, "car",registered_model_name="RandomForestRegressor")
            # else:
            #     mlflow.sklearn.log_model(model, "car")

    
