# Read Parquet database
import pandas as pd
path = "./week4/inclass_activities/Sample_data_2.parquet"
df = pd.read_parquet(path)
print(df.shape[0])
print(len(df))