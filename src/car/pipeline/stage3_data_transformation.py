from src.car.entity.config_entity import DataTransformationConfig
from src.car import logger
from src.car.components.data_transformation import DataTransformation
from src.car.config.configuration import ConfigurationManager

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        
        data_transformation = DataTransformation(config = data_transformation_config)
        data_transformation.clean_data()
        data_transformation.drop_minority()
        data_transformation.split_name()
        data_transformation.train_test_split()
        data_transformation.build_transformer()


if __name__ == '__main__':
    try:
        logger.info(f"<<<<< {STAGE_NAME} started >>>>>")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed successfully <<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e

