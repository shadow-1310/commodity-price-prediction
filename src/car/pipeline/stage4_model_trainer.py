from car.entity.config_entity import ModelTrainConfig
from car import logger
from car.components.model_trainer import ModelTrainer
from car.config.configuration import ConfigurationManager

STAGE_NAME = "Model Training Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_train_config = config.get_model_train_config()
        
        model_trainer = ModelTrainer(config = model_train_config)
        model_trainer.train()

if __name__ == '__main__':
    try:
        logger.info(f"<<<<< {STAGE_NAME} started >>>>>")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed successfully <<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e

