from src.entity.config_entity import DataIngestionConfig
import requests
import os
import pandas as pd
from src.utils.common import create_directories




class IngestionClass:
    def __init__(self, config: DataIngestionConfig):
        self.config=config


    def download_url_data(self):
        # Convert GitHub HTML link to raw link if necessary
        url = self.config.data_source
        local = self.config.local_store

        if "github.com" in url and "/blob/" in url:
            url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")

        # Download only if file doesn't already exist
        if not os.path.exists(local):
            response = requests.get(url)
            response.raise_for_status()  # Raise error if download failed

            with open(local, "wb") as f:
                f.write(response.content)

            print(f"CSV file downloaded and saved to: {local}")
        else:
            print("File already exists. Skipping download.")

        # Read CSV from saved file
        df = pd.read_csv(local)
        print("CSV file loaded successfully:")

        df.to_csv(local, index=False)
        print(f"CSV file saved to: {local}")
