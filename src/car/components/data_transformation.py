import os
import joblib
from car import logger
from car.entity.config_entity import DataTransformationConfig
# from car.utils.common import clean_data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.params = config.params

    def clean_data(self):
        config = self.config
        schema = config.schema
        
        try:
            logger.info("<<<<<<< Data Cleaning Started >>>>>>>")

            input_path = config.unzip_data_dir
            output_path = config.transformed_data_dir.clean_data

            logger.info(f"{input_path} accessed for cleaning and removing duplicates")
            df = pd.read_csv(input_path)
            null_values = df.isna().sum()
            df_temp = df.dropna()
            logger.info(f"{input_path} contained null values as follows : {null_values }")

            duplicate_values = df_temp.duplicated().sum()
            logger.info(f"{input_path} contained {duplicate_values} duplicates")
            df_temp.drop_duplicates(inplace=True)
            df_temp.reset_index(inplace=True, drop=True)
            df_temp.to_csv(output_path, index=False)

            logger.info(">>>>>>>data cleaning complete <<<<<<<<")

        except Exception as e:
            logger.exception(e)
            raise e


    def drop_minority(self):
        try:
            config = self.config
            schema = config.schema
            THRESH = self.params.data_transformation.drop_minority.thresh

            input_path = config.transformed_data_dir.clean_data
            output_path = config.transformed_data_dir.clean_data

            df = pd.read_csv(input_path)
            cols = list(schema.transformed_cols.categorical.keys())
            for col in cols:
                counts = df[col].value_counts()
                for i in counts.index:
                    if counts[i] < THRESH:
                        df = df[df[col] != i]
                        logger.info(f"Removed value: {i} in Column: {col}, as it had counts: {counts[i]}")

            df.to_csv(output_path, index=False)
            logger.info(f"New file after removing minority saved to: {output_path}")

        except Exception as e:
            logger.exception(e)
            raise e


    def split_name(self):
        try:
            config = self.config
            schema = config.schema

            input_path = config.transformed_data_dir.clean_data
            output_path = config.transformed_data_dir.clean_data

            df = pd.read_csv(input_path)

            df['company'] = df['name'].apply(lambda x:x.split()[0])
            df['model'] = (df['name'].apply(lambda x:x.split()[1:3])).str.join(' ')
            df.drop(columns=['name'], inplace=True)

            logger.info("New columns made in {input_path}: 'company' and 'model'\columns dropped in {input_path}: 'name'")
            df.to_csv(output_path, index = False)
            logger.info(f"New file saved to {output_path}")

        except Exception as e:
            logger.exception(e)
            raise e


    def train_test_split(self):
        try:
            config = self.config

            input_path = config.transformed_data_dir.clean_data
            train_path = config.transformed_data_dir.train_data
            test_path = config.transformed_data_dir.test_data

            df = pd.read_csv(input_path)

            train, test = train_test_split(df)

            train.to_csv(train_path, index=False)
            logger.info("train data saved")
            test.to_csv(test_path, index=False)
            logger.info("test data saved")

        except Exception as e:
            logger.exception(e)
            raise e


    def build_transformer(self):
        try:
            config = self.config
            schema = config.schema

            numeric_cols = list(schema.transformed_cols.numeric.keys())
            cat_cols = list(schema.transformed_cols.categorical.keys())
            target_column = list(schema.transformed_cols.target_column.keys())

            input_path = config.transformed_data_dir.train_data
            output_path = config.transformed_data_dir.transformer
            
            data = pd.read_csv(input_path).drop(columns = target_column)

            transformer = ColumnTransformer(transformers=[
                    ('ohe', OneHotEncoder(sparse_output=False, handle_unknown='ignore'), cat_cols),
                    ('scaler', MinMaxScaler(), numeric_cols)
                                                            ], remainder='passthrough')
            transformer.fit(data)

            joblib.dump(transformer, output_path)
            logger.info(f"transformer saved to {output_path}")

        except Exception as e:
            logger.exception(e)
            raise e 
