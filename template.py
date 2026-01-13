import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

PROJECT_NAME = "Text_Summarizer"

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{PROJECT_NAME}/__init__.py',
    f'src/{PROJECT_NAME}/components/__init__.py',
    f'src/{PROJECT_NAME}/utils/__init__.py',
    f'src/{PROJECT_NAME}/utils/common.py',
    f'src/{PROJECT_NAME}/logging/__init__.py',
    f'src/{PROJECT_NAME}/config/__init__.py',
    f'src/{PROJECT_NAME}/config/configuration.py',
    f'src/{PROJECT_NAME}/pipeline/__init__.py',
    f'src/{PROJECT_NAME}/entity/__init__.py',
    f'src/{PROJECT_NAME}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb ', 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists and is not empty: {filepath}")