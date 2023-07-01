import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = "file.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH, sep=',')
    print(f"Rows and coloumns: {df.shape}")


 #comment dataframe df to json format so that we can dump this records in mongo db 

    df.reset_index(drop=True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    # inert converted json record to mongo db 
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
