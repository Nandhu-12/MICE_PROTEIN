import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE = 'MICE-PROTEIN-EXPRESSION'
COLLECTION = 'Mice-Protein'
DATA_FILE_PATH="/config/workspace/MICE_PROTEIN.csv"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    #Convert dataframe to json so that we can dump these record in mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    #insert converted json record to mongo db
    mongo_client[DATABASE][COLLECTION].insert_many(json_record)