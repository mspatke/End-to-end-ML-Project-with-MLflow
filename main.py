from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "DATA INGESTION STAGE"

#logger.info("Welcome to our custom logging")

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e