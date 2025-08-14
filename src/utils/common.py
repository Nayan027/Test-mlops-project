import os
import yaml
from src.loggings import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
import requests


#Read a yaml file content and access it in form of a dict where it's keys act like attributes.
@ensure_annotations
def read_yaml(path_to_yamlfile: Path) -> ConfigBox:

    with open(path_to_yamlfile) as yaml_file:
        content = yaml.safe_load(yaml_file)

        return ConfigBox(content)
    

#Create directories at will
@ensure_annotations
def create_directories(path_to_dirs: list):

    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)


#Saving data that's in form of a dict into a specific json file
@ensure_annotations
def save_into_json(json_path: Path, data: dict):

    with open(json_path, "w") as file:
        json.dump(data, file, indent=4)


#Loading content from a json file
@ensure_annotations
def load_from_json(json_path: Path) -> ConfigBox:

    with open(json_path) as file:
        content = json.load(file)

        return ConfigBox(content)
    


"""Download CSV from URL and save to local file."""
@ensure_annotations
def download_csv(url: str, save_path: Path):

    response = requests.get(url)
    response.raise_for_status()  # raise error if download failed
    
    with open(save_path, "wb") as f:
        f.write(response.content)
    
    print(f"CSV file downloaded and saved to: {save_path}")

