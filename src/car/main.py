from src.car import logger
from src.car.pipeline.stage1_data_ingestion import DataIngestionPipeline
from src.car.pipeline.stage2_data_validation import DataValidationPipeline
from src.car.pipeline.stage3_data_transformation import DataTransformationPipeline
from src.car.pipeline.stage4_model_trainer import ModelTrainerPipeline
from src.car.pipeline.prediction import PredictionPipeline

STAGE_NAME = "DATA Ingestion Stage"

try:
    logger.info(f"<<<<< {STAGE_NAME} started >>>>>")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> {STAGE_NAME} completed successfully <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f"<<<<< {STAGE_NAME} started >>>>>")
    obj = DataValidationPipeline()
    obj.main()
    logger.info(f">>>>>> {STAGE_NAME} completed successfully <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e
