import os
from src.car import logger
from src.car.entity.config_entity import DataValidationConfig
from src.car.utils.common import validate_data

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_data(self) -> bool:
        try:
            path = self.config.unzip_data_dir
            status_file = self.config.STATUS_FILE
            schema = self.config.schema

            status = True
            
            validation_schema = {}
            numeric = list(schema.input_columns.numeric.items())
            cat = list(schema.input_columns.categorical.items())
            target = list(schema.target_column)

            sch = [numeric, cat, target]

            for s in sch:
                for i in s:
                    validation_schema[i[0]] = i[1]


            data = pd.read_csv(file_path)
            cols = list(data.columns)

            status_cols = True
            status_dtype = True

            for col in validation_schema.keys():
                if col not in cols:
                    curr_status = False
                    status_cols = status_cols and curr_status
                    logger.warning(f"!!! for file {os.path.basename(file_path)} : {col} not present in data !!!")
                if data[col].dtype != validation_schema[col]:
                    curr_status = False
                    status_dtype = status_dtype and curr_status
                    logger.warning(f"!!! for file {os.path.basename(file_path)} : data mismatch for column {col} !!!")

            status = status_cols and status_dtype

            with open(status_file, "a") as file:
                file.write(f"Validation status for {path}: {status}\n")

            logger.info(f"validation status: {status}")
        
        except Exception as e:
            logger.exception(e)
            raise e           
