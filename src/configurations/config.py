from src.static import *
from src.utils.common import read_yaml, create_directories
from src.entity.config_entity import DataIngestionConfig, DataValidationConfig

class ConfigManager:
    def __init__(self,
                c_fpath=config_fpath,
                s_fpath=schema_fpath,
                p_fpath=param_fpath):
        
        self.config = read_yaml(c_fpath)
        self.schema = read_yaml(s_fpath)
        self.params = read_yaml(p_fpath)

        create_directories([self.config.root_artifact])


    

    def get_ingestion_config(self) -> DataIngestionConfig: 
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        ingestion_config_object = DataIngestionConfig(
            data_source= config.data_source, 

            root_dir= config.root_dir, 
            local_store= config.local_store,
        )

        return ingestion_config_object
    


    def get_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema

        create_directories([config.root_dir])

        validation_config_object = DataValidationConfig(
            local_data= config.local_data, 

            all_schema= schema.COLUMNS, 
            
            root_dir= config.root_dir, 
            status_file= config.status_file
        )

        return validation_config_object