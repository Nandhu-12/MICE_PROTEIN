from mice_protein.logger import logging
from mice_protein.exception import MiceException
from mice_protein import utils
import pandas as pd
import numpy as np
import os,sys
from mice_protein.entity import config_entity
from mice_protein.entity import artifact_entity
from sklearn.model_selection import train_test_split


class DataIngestion:
    def __init__ (self,data_ingestion_config : config_entity.DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            return (e, sys)


    def initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:
        try:
            logging.info(f"Importing collection data as pandas dataframe")
            df:pd.DataFrame = utils.get_collection_as_dataframe(DATABASE= self.data_ingestion_config.DATABASE,
                                                                COLLECTION= self.data_ingestion_config.COLLECTION)
            
            logging.info(f"replacing na values to np.NaN")
            df.replace(to_replace = "na", value = np.NAN, inplace = True)

            logging.info(f"creating feature store dir")
            feature_store_dir = os.path.dirname(self.data_ingestion_config.feature_store_filepath)
            os.makedirs(feature_store_dir,exist_ok = True)

            logging.info(f"storing df in feature store dir")
            df.to_csv(path_or_buf=self.data_ingestion_config.feature_store_filepath, header = True, index=False)

            logging.info(f"splitting df to train and test")
            train_df, test_df = train_test_split(df,test_size = self.data_ingestion_config.test_size)

            logging.info(f"creating dataset dir")
            dataset_dir = os.path.dirname(self.data_ingestion_config.train_filepath)
            os.makedirs(dataset_dir,exist_ok = True)

            logging.info(f"saving train and test df to dataset dir")
            train_df.to_csv(path_or_buf = self.data_ingestion_config.train_filepath, index = False, header = True)
            test_df.to_csv(path_or_buf = self.data_ingestion_config.test_filepath, index = False, header = True)

            logging.info(f"preparing artifact")
            data_ingestion_artifact = artifact_entity.DataIngestionArtifact(
                feature_store_filepath = self.data_ingestion_config.feature_store_filepath,
                train_filepath = self.data_ingestion_config.train_filepath,
                test_filepath = self.data_ingestion_config.test_filepath
            )
            return data_ingestion_artifact

        except Exception as e:
            raise SensorException(e, sys)