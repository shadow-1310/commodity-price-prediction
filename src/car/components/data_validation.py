import os
from car import logger
from car.entity.config_entity import DataValidationConfig
from car.utils.common import validate_data
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_data(self) -> bool:
        try:
            input_path = self.config.unzip_data_dir
            status_file = self.config.STATUS_FILE
            schema = self.config.schema

            status = True
            
            validation_schema = {}
            numeric = list(schema.input_columns.numeric.items())
            cat = list(schema.input_columns.categorical.items())
            target = list(schema.target_column.items())
            logger.info(f"{numeric}\n {cat}\n {target}")

            sch = [numeric, cat, target]

            for s in sch:
                for i in s:
                    validation_schema[i[0]] = i[1]


            data = pd.read_csv(input_path)
            cols = list(data.columns)

            status_cols = True
            status_dtype = True

            for col in validation_schema.keys():
                if col not in cols:
                    curr_status = False
                    status_cols = status_cols and curr_status
                    logger.warning(f"!!! for file {os.path.basename(input_path)} : {col} not present in data !!!")
                if data[col].dtype != validation_schema[col]:
                    curr_status = False
                    status_dtype = status_dtype and curr_status
                    logger.warning(f"!!! for file {os.path.basename(input_path)} : data mismatch for column {col} !!!")

            status = status_cols and status_dtype

            with open(status_file, "a") as file:
                file.write(f"Validation status for {input_path}: {status}\n")

            logger.info(f"validation status: {status}")
        
        except Exception as e:
            logger.exception(e)
            raise e           
