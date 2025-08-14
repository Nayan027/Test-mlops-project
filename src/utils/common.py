import os
import yaml
from src.loggings import logger
from src.exception import CustomException
import json
import joblib
import ensure
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
import requests
import sys


# Read a yaml file content and access it in form of a dict where its keys act like attributes.
@ensure_annotations
def read_yaml(path_to_yamlfile: Path) -> ConfigBox:
    try:
        logger.info(f"Reading YAML file from: {path_to_yamlfile}")
        with open(path_to_yamlfile) as yaml_file:
            content = yaml.safe_load(yaml_file)
        logger.info("YAML file read successfully.")
        return ConfigBox(content)
    except Exception as e:
        logger.error(f"Error while reading YAML file: {e}")
        raise CustomException(e, sys)


# Create directories at will
@ensure_annotations
def create_directories(path_to_dirs: list):
    try:
        for path in path_to_dirs:
            os.makedirs(path, exist_ok=True)
            logger.info(f"Directory created or already exists: {path}")
    except Exception as e:
        logger.error(f"Error while creating directories: {e}")
        raise CustomException(e, sys)


# Saving data that's in form of a dict into a specific json file
@ensure_annotations
def save_into_json(json_path: Path, data: dict):
    try:
        with open(json_path, "w") as file:
            json.dump(data, file, indent=4)
        logger.info(f"JSON data saved successfully to {json_path}")
    except Exception as e:
        logger.error(f"Error while saving JSON file: {e}")
        raise CustomException(e, sys)


# Loading content from a json file
@ensure_annotations
def load_from_json(json_path: Path) -> ConfigBox:
    try:
        logger.info(f"Loading JSON file from: {json_path}")
        with open(json_path) as file:
            content = json.load(file)
        logger.info("JSON file loaded successfully.")
        return ConfigBox(content)
    except Exception as e:
        logger.error(f"Error while loading JSON file: {e}")
        raise CustomException(e, sys)


