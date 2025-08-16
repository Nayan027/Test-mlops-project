# from src import loggings
from src.configurations.config import ConfigManager
from src.components.data_ingestion import IngestionClass
from src.components.data_validation import ValidationClass
from src.components.data_transformation import DataTransformation
# from src.components.model_trainer import ModelTrainer
# from src.components.model_evaluation import ModelEvaluation
from pathlib import Path


# ========== Stage 1 ==========
class DataIngestionTrainingPipeline:
    def main(self):
        config = ConfigManager()
        data_ingestion_config = config.get_ingestion_config()
        data_ingestion = IngestionClass(config=data_ingestion_config)
        data_ingestion.download_url_data()


# # ========== Stage 2 ==========
class DataValidationTrainingPipeline:
    def main(self):
        config = ConfigManager()
        data_validation_config = config.get_validation_config()
        data_validation = ValidationClass(config=data_validation_config)
        data_validation.validate_columns()


# # ========== Stage 3 ==========
class DataTransformationTrainingPipeline:
    def main(self):
        with open(Path("artifacts/data_validation/status_file.txt"), "r") as f:
            status = f.read().strip()

        if "True" in status:
            config = ConfigManager()
            data_transformation_config = config.get_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.split_data()
        else:
            raise Exception("Your data schema is not valid")


# # ========== Stage 4 ==========
# class ModelTrainerTrainingPipeline:
#     def main(self):
#         config = ConfigManager()
#         model_trainer_config = config.get_model_trainer_config()
#         model_trainer = ModelTrainer(config=model_trainer_config)
#         model_trainer.train()


# # ========== Stage 5 ==========
# class ModelEvaluationTrainingPipeline:
#     def main(self):
#         config = ConfigManager()
#         model_evaluation_config = config.get_model_evaluation_config()
#         model_evaluation = ModelEvaluation(config=model_evaluation_config)
#         model_evaluation.log_into_mlflow()


# # ============================
# Run Pipeline Sequentially
# ============================
if __name__ == "__main__":
    # loggings.info(">>>>> Data Ingestion stage started <<<<<")
    DataIngestionTrainingPipeline().main()
    # loggings.info(">>>>> Data Ingestion stage completed <<<<<\n")

#     loggings.info(">>>>> Data Validation stage started <<<<<")
    DataValidationTrainingPipeline().main()
#     loggings.info(">>>>> Data Validation stage completed <<<<<\n")

#     loggings.info(">>>>> Data Transformation stage started <<<<<")
    DataTransformationTrainingPipeline().main()
#     loggings.info(">>>>> Data Transformation stage completed <<<<<\n")

#     loggings.info(">>>>> Model Trainer stage started <<<<<")
#     ModelTrainerTrainingPipeline().main()
#     loggings.info(">>>>> Model Trainer stage completed <<<<<\n")

#     loggings.info(">>>>> Model Evaluation stage started <<<<<")
#     ModelEvaluationTrainingPipeline().main()
#     loggings.info(">>>>> Model Evaluation stage completed <<<<<\n")
