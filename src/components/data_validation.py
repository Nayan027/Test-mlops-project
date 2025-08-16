import os
from src.entity.config_entity import DataValidationConfig
import pandas as pd


class ValidationClass:
    def __init__(self, config: DataValidationConfig):
        self.config=config


# Refined and simpler code cause we faced a lil problem in logic. Reason stated below.

    def validate_columns(self) -> bool:

        local_data = self.config.local_data

        all_schema = self.config.all_schema
        status_file = self.config.status_file

        df = pd.read_csv(local_data)
        columns = list(df.columns)

        validation_status = set(columns) == set(all_schema)

        with open(status_file,"w") as f:
            f.write(f"validation status is: {validation_status}\n")

            f.write(f"\nexpected columns: {list(all_schema)}\n")
            f.write(f"\ncolumns found: {columns}")

        return validation_status
    


#     def validate_columns(self) -> bool:

#         local_data=self.config.local_data
# #        root_dir=self.config.root_dir      #didnt come to use so we can just not use it for cleaner code
#         status_file=self.config.status_file
#         all_schema=self.config.all_schema

#         validation_status = None

#         df = pd.read_csv(local_data)
#         columns = list(df.columns)

# # Use if order-insensitive-validation 
#         validation_status = set(all_schema) == set(columns)
# # Set Equality Neither one checks through the other — both are converted into sets, 
# # and Python checks if the two sets are equal.
# # order-sensitive-validation: Use If you also care about column order, not just column names
#         # validation_status = columns == list(all_schema)


#         with open(status_file,"w") as f:
#             f.write(f"validation status is: {validation_status}")
# # Extra info.
#             f.write(f"\nExpected: {list(all_schema)}\n")
#             f.write(f"Found: {columns}\n")

#         return validation_status
    



# Code given by Bappy

    # def validate_columns(self) -> bool:
    #     validation_status=None

    #     data = pd.read_csv(self.config.local_data)
    #     all_columns = list(data.columns)

    #     all_schema = self.config.all_schema.keys()

    #     for col in all_columns:
    #         if col not in all_schema:
    #             validation_status = False

    #             with open(self.config.status_file, "w") as file:
    #                 file.write(f"validation status:{validation_status}")
                    

    #         else:
    #             validation_status = True
    #             with open(self.config.status_file, "w") as file:
    #                 file.write(f"validation status:{validation_status}")
                     
    #     return validation_status




# This code below is that i have come up with a better understanding and a cleaner structure.

    # def validate_columns(self) -> bool:

    #     local_data=self.config.local_data
    #     root_dir=self.config.root_dir
    #     status_file=self.config.status_file
    #     all_schema=self.config.all_schema

    #     validation_status = None

    #     df = pd.read_csv(local_data)
    #     columns = list(df.columns)

    #     for cols in columns:
    #         if cols in all_schema:
    #             validation_status = True

    #             with open(status_file,"w") as f:
    #                 f.write(f"validation status is: {validation_status}")

    #         else:
    #             validation_status= False
    #             with open(status_file, "w") as f:
    #                 f.write(f"validation status: {validation_status}")

    #     return validation_status



# Now iss code k saath main problem ye thi ki ye open file wala funcn ek loop mein chl rha hai.
# Ye write mode mein bhi hai now since its inside a loop ye hrr baar restart ho jata h when
# iterating over each column uss wajah se ye "w" mode bhi restart ho jata h everytime therefore:
# 
# The file is opened in write mode ("w") inside the loop → every iteration overwrites the file. 
# So only the last column’s validation result will remain in the status file.

# Also, validation_status will only reflect the result of the last column checked. That means if the 
# first 4 columns were correct and the last one failed, the function will return False — but if the 
# last column was correct and one earlier was wrong, the function will incorrectly return True.