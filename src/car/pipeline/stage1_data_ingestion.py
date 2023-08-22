from src.car.config.configuration import ConfigurationManager
from src.car.components.data_ingestion import DataIngestion
import src.car import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip()


if __name__ == '__main__':
    try:
        logger.info(f"<<<<< {STAGE_NAME} started >>>>>")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed successfully <<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e

