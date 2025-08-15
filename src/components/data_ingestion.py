from src.entity.config_entity import DataIngestionConfig
import requests
import os





# class IngestionClass:
#     def __init__(self, config: DataIngestionConfig):
#         self.config=config


#     def download_url_data(self):
        
# # store configurations into local variables for ease in code
#         url = self.config.data_source
#         local = self.config.local_store

# # Convert GitHub HTML link to raw link if necessary
#         if "github.com" in url and "/blob/" in url:
#             url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")

#         # check if file already exist
#         if os.path.exists(local):
#             print("File already exists. Skipping download.")

#         # Download only if file doesn't already exist   
#         else:
#             response = requests.get(url)
#             response.raise_for_status()  # Raise error if download failed

#             with open(local, "wb") as f:  # write in binary mode
#                 f.write(response.content)

#             print(f"CSV file downloaded and saved to: {local}")






'''Here i tried to write the entire code myself by simply understanding it.'''

class IngestionClass:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_url_data(self):
        url = self.config.data_source

        local_data = self.config.local_store


        if "github.com" in url and "/blob/" in url:
            url=url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
        
        if os.path.exists(local_data):
            print("Local data file already exists! Skipped downloading again.")

        else:
            response=requests.get(url)
            response.raise_for_status()

            with open(local_data,"wb") as file:
                file.write(response.content)

            print("Local data file downloaded successfully!!!")