from src.mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import dataIngestiontrainingPipeleine

STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f">>>>>>stage  {STAGE_NAME}  started<<<<<<")
    obj=dataIngestiontrainingPipeleine()
    obj.main()
    logger.info(f">>>>>>stage {STAGE_NAME} completed<<<<<<\n\nX========X")
except Exception as e:
    logger.exception(e)
    raise e
