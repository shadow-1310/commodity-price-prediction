import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = ['car', 'laptop']

list_of_files = [
        ".github.workflows/.gitkeep",
        "Dockerfile",
        "requirements.txt",
        "setup.py",
        "README.md",
        f"src/{project_name[0]}/__init__.py",
        f"src/{project_name[0]}/components/__init__.py",
        f"src/{project_name[0]}/utils/__init__.py",
        f"src/{project_name[0]}/utils/common.py",
        f"src/{project_name[0]}/config/configuration.py",
        f"src/{project_name[0]}/config/__init__.py",
        f"src/{project_name[0]}/pipeline/__init__.py",
        f"src/{project_name[0]}/entity/config_entity.py",
        f"src/{project_name[0]}/entity/__init__.py",
        f"src/{project_name[0]}/constants/__init__.py",
        f"config/{project_name[0]}/config.yaml",
        f"config/{project_name[0]}/schema.yaml",
        f"config/{project_name[0]}/params.yaml",
        f"src/{project_name[0]}/main.py",
        f"research/{project_name[0]}/test.ipynb",
        f"src/{project_name[1]}/__init__.py",
        f"src/{project_name[1]}/components/__init__.py",
        f"src/{project_name[1]}/utils/__init__.py",
        f"src/{project_name[1]}/utils/common.py",
        f"src/{project_name[1]}/config/configuration.py",
        f"src/{project_name[1]}/config/__init__.py",
        f"src/{project_name[1]}/pipeline/__init__.py",
        f"src/{project_name[1]}/entity/config_entity.py",
        f"src/{project_name[1]}/entity/__init__.py",
        f"src/{project_name[1]}/constants/__init__.py",
        f"config/{project_name[1]}/config.yaml",
        f"config/{project_name[1]}/schema.yaml",
        f"config/{project_name[1]}/params.yaml",
        f"src/{project_name[1]}/main.py",
        f"research/{project_name[1]}/test.ipynb",
        ]


for filepath in list_of_files:
    #uncomment the following line in case of Windows OS
    # filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Directory created: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass

        logging.info(f"Empty file created: {filepath}")

    else:
        logging.info(f"{filename} already exists")

