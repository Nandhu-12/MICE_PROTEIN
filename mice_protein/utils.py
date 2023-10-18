import pandas as pd
import numpy as np
import os,sys
from mice_protein.logger import logging
from mice_protein.exception import MiceException
from mice_protein.config import mongo_client
import yaml
import dill

def get_collection_as_dataframe(DATABASE:str, COLLECTION:str)->pd.DataFrame:
    try:
        #reading data
        logging.info(f"reading from {DATABASE} database and {COLLECTION} collection")
        df = pd.DataFrame(mongo_client[DATABASE][COLLECTION].find())

        #dropping id col
        logging.info(f"dropping {'_id'} column from dataset")
        if '_id' in df.columns:
            df.drop("_id",axis = 1,inplace = True)

        logging.info(f"shape of dataset is : {df.shape}")
        return df

    except Exception as e:
        raise MiceException(e,sys)