from src.car import logger
from src.car.utils.common import get_size
import zipfile
from urllib import request
from src.car.entity.config_entity import (DataIngestionConfig)
import os
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded!!! with the details \n{headers}")
        else:
            logger.info(f"File already exists of size : {get_size(Path(self.config.local_data_file))}")

    def extract_zip(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as z:
            z.extractall(unzip_path)
