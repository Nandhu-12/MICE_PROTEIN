from mice_protein.logger import logging
from mice_protein.exception import MiceException
from mice_protein.utils import get_collection_as_dataframe
import sys,os
from mice_protein.entity import config_entity
from mice_protein.components.data_ingestion import DataIngestion

print(__name__)
if __name__=="__main__":
     try:
          training_pipeline_config = config_entity.TrainingPipelineConfig()

          #data ingestion
          data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
          print(data_ingestion_config.to_dict())
          data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
          print(data_ingestion.initiate_data_ingestion())

          
     except Exception as e:
          print(e)