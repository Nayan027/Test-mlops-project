from src.entity.config_entity import TransformationConfig
import pandas as pd
from sklearn.model_selection import train_test_split
# import os

class DataTransformation:
    def __init__(self, config:TransformationConfig):
        self.config = config

    def transformation(self):
        pass

# Below is the code i came up with on my own to excuse the os methods,

    def split_data(self):
        local_data = self.config.local_data
        train_data_path = self.config.train_data_path
        test_data_path = self.config.test_data_path
        split_ratio = self.config.split_ratio
# Above the variables are used to ease our code and so we dont have to write long stuff.

# Reading csv data into a dataframe
        data = pd.read_csv(local_data)
# Applying train-test split with split ratio defined in params.yaml
        train, test = train_test_split(data, test_size=split_ratio, random_state=42)
# Saving train and test data in local paths mentioned in config.yaml
        train.to_csv(train_data_path,index=False)
        test.to_csv(test_data_path, index=False)

        print(train.shape)
        print(test.shape)


# Bappy ka code.
    # def data_split(self):
    #     local_data = self.config.local_data      #BETTER LOOKING CODE.


    #     data = pd.read_csv(local_data)
    #     train, test = train_test_split(data, test_size=0.20, random_state=42)

    #     train.to_csv(os.path.join(self.config.root_dir,"train.csv"), index=False)
    #     test.to_csv(os.path.join(self.config.root_dir,"test.csv"), index=False)

    #     print(train.shape)
    #     print(test.shape)

