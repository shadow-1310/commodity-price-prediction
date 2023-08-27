from car import logger
from car.pipeline.stage1_data_ingestion import DataIngestionPipeline
from car.pipeline.stage2_data_validation import DataValidationPipeline
from car.pipeline.stage3_data_transformation import DataTransformationPipeline
from car.pipeline.stage4_model_trainer import ModelTrainerPipeline
from car.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"

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



STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"<<<<< {STAGE_NAME} started >>>>>")
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(f">>>>>> {STAGE_NAME} completed successfully <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Training Stage"

try:
    logger.info(f"<<<<< {STAGE_NAME} started >>>>>")
    obj = ModelTrainerPipeline()
    obj.main()
    logger.info(f">>>>>> {STAGE_NAME} completed successfully <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f"<<<<< {STAGE_NAME} started >>>>>")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> {STAGE_NAME} completed successfully <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e
