from src.mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import dataIngestionTrainingPipeleine
from mlProject.pipeline.stage_02_data_validation import dataValidationTrainingPipeleine
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f">>>>>>stage  {STAGE_NAME}  started<<<<<<")
    obj=dataIngestionTrainingPipeleine()
    obj.main()
    logger.info(f">>>>>>stage {STAGE_NAME} completed<<<<<<\n\nX========X")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Validation stage"

try:
    logger.info(f">>>>>>stage  {STAGE_NAME}  started<<<<<<")
    obj=dataValidationTrainingPipeleine()
    obj.main()
    logger.info(f">>>>>>stage {STAGE_NAME} completed<<<<<<\n\nX========X")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Transformation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

