from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DatavalidationTrainingPipeline

STAGE_NAME = "DATA INGESTION STAGE"

#logger.info("Welcome to our custom logging")

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n")
except Exception as e:
    logger.exception(e)
    raise e
    


STAGE_NAME = "DATA VALIDATION STAGE"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DatavalidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e